#!/usr/bin/env python

import Queue
import argparse
import csv
import multiprocessing
import os
import sys
import threading
import time

from PyQt5.QtCore import QSettings, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QTextCursor, QPalette, QColor, QGuiApplication
from PyQt5.QtWidgets import *

import AboutDialog
import MainInterface
import SettingsDialog
from ADBInterface import ADBInterface
from GovernorControler import GovernorController
from PIDTool import PIDTool
from SysLoggerInterface import SysLogger
from SystemMetrics import SystemMetrics
from TraceCMDParser import TracecmdProcessor
from TraceProcessor import TraceProcessor
from Tracer import Tracer

__author__ = "Alex Hoffman"
__copyright__ = "Copyright 2019, Alex Hoffman"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Hoffman"
__email__ = "alex.hoffman@tum.de"
__status__ = "Beta"

parser = argparse.ArgumentParser()

parser.add_argument(
    "-c",
    "--commandline",
    required=False,
    help="Enables the use of command line arguments",
)
parser.add_argument("-a",
                    "--app",
                    required=False,
                    help="Specifies the name of the game to be traced")
parser.add_argument("-d",
                    "--duration",
                    required=False,
                    type=float,
                    help="The duration to trace")
parser.add_argument("-e",
                    "--events",
                    required=False,
                    help="Events that are to be traced")
parser.add_argument("-s",
                    "--skip-clear",
                    action="store_true",
                    help="Skip clearing trace settings")
parser.add_argument(
    "-g",
    "--draw",
    action="store_true",
    help="Enables the drawing of the generated graph",
)
parser.add_argument(
    "-te",
    "--test",
    action="store_true",
    help="Tests only a few hundred events to speed up testing",
)
parser.add_argument(
    "-sub",
    "--subgraph",
    action="store_true",
    help="Enable the drawing of node subgraphs",
)
parser.add_argument(
    "-p",
    "--preamble",
    required=False,
    help=
    "Specifies the number of seconds that be discarded at the begining of tracing",
)

args = parser.parse_args()


class AboutDialog(QDialog, AboutDialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)


class SettingsMenu(QDialog, SettingsDialog.Ui_DialogSettings):
    def __init__(self, settings, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        self.settings = settings

        # Application
        self.lineEditApplicationName.setText(
            settings.value("DefaultApplication", defaultValue=""))
        self.doubleSpinBoxDuration.setValue(
            float(settings.value("DefaultDuration", defaultValue=0.0)))
        self.doubleSpinBoxPreamble.setValue(
            float(settings.value("DefaultPreamble", defaultValue=0.0)))
        self.checkBoxDrawGraph.setChecked(
            bool(int(settings.value("DefaultDrawGraph", defaultValue=0))))
        self.checkBoxWakeUp.setChecked(
            bool(int(settings.value("DefaultEventWakeUp", defaultValue=0))))
        self.checkBoxSchedSwitch.setChecked(
            bool(int(settings.value("DefaultEventSchedSwitch",
                                    defaultValue=1))))
        self.checkBoxCPUIdle.setChecked(
            bool(int(settings.value("DefaultEventCPUIdle", defaultValue=0))))
        self.checkBoxBinderTransaction.setChecked(
            bool(
                int(
                    settings.value("DefaultEventBinderTransaction",
                                   defaultValue=1))))
        self.checkBoxSyslogger.setChecked(
            bool(int(settings.value("DefaultEventSyslogger", defaultValue=1))))
        self.radioButtonMultiThreaded.setChecked(
            bool(int(settings.value("OptimizeWithThreads", defaultValue=1))))
        self.radioButtonMultiProcessing.setChecked(
            bool(int(settings.value("OptimizeWithProcesses", defaultValue=1))))
        self.radioButtonNonthreaded.setChecked(
            bool(int(settings.value("OptimizeNone", defaultValue=1))))
        self.checkBoxUseUIConsole.setChecked(
            bool(int(settings.value("UseUIConsole", defaultValue=1))))

        # Syslogger
        self.spinBoxCPU.setValue(
            int(settings.value("DefaultSysloggerCPU", defaultValue=2)))
        self.spinBoxInterval.setValue(
            int(settings.value("DefaultSysloggerInterval", defaultValue=5)))
        self.checkBoxCPUInfo.setChecked(
            bool(int(settings.value("DefaultSysloggerCPUInfo",
                                    defaultValue=1))))
        self.checkBoxCPUFrequency.setChecked(
            bool(int(settings.value("DefaultSysloggerCPUFreq",
                                    defaultValue=1))))
        self.checkBoxPower.setChecked(
            bool(int(settings.value("DefaultSysloggerPower", defaultValue=1))))
        self.checkBoxMali.setChecked(
            bool(int(settings.value("DefaultSysloggerMali", defaultValue=1))))
        self.checkBoxTemp.setChecked(
            bool(int(settings.value("DefaultSysloggerTemp", defaultValue=1))))
        self.checkBoxNetwork.setChecked(
            bool(int(settings.value("DefaultSysloggerNetwork",
                                    defaultValue=0))))

    def sysloggerstart_clicked(self):
        pass

    def sysloggersetup_clicked(self):
        pass

    def sysloggerstop_clicked(self):
        pass

    def sysloggerfinish_clicked(self):
        pass

    def sysloggerpull_clicked(self):
        if self.lineEditSyslogPullFilename.text():
            pull_location = (self.lineEditSyslogPullFolder.text() + "/" +
                             self.lineEditSyslogPullFilename.text())
        else:
            pull_location = self.lineEditSyslogPullFolder.text() + "/trace.dat"
        try:
            adb = ADBInterface()
            adb.pull_file("/data/local/tmp/trace.dat", pull_location)
        except Exception, e:
            QMessageBox.critical(
                self, "Error",
                "Pulling file via ADB failed\n\n Error: {}".format(e))
            raise Exception(e)
            self.close()

    def sysloggerpullfile_clicked(self):
        options = QFileDialog.Options()
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        filename = dialog.getExistingDirectory(self, options=options)
        self.lineEditSyslogPullFolder.setText(filename)

    def sysloggerfiletoconvert_clicked(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*)",
            options=options)
        self.lineEditConvertSource.setText(filename)

    def sysloggerfiletoconvertdestination_clicked(self):
        options = QFileDialog.Options()
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        filename = dialog.getExistingDirectory(self, options=options)
        self.lineEditConvertDestination.setText(filename)

    def sysloggerconverttrace_clicked(self):
        error = False
        error_str = "The following required parameters are missing:\n\n"
        if not self.lineEditConvertSource.text():
            error = True
            error_str += "Application Name\n"
        if self.lineEditConvertDestination.text():
            error = True
            error_str += "Duration"

        if error:
            QMessageBox.warning(self, "Error", error_str, QMessageBox.Ok)

        if not os.path.isfile(self.lineEditConvertSource.text()):
            QMessageBox.critical(self, "Error",
                                 "The trace source file does not exist",
                                 QMessageBox.Ok)

        os.system("trace_conv.py -i " + self.lineEditConvertSource.text() +
                  " -o " + self.lineEditConvertDestination.text())
        QMessageBox.information(self, "Trace convert",
                                "Converting trace complete", QMessageBox.Ok)

    def accept(self):

        # Application
        self.settings.setValue("DefaultApplication",
                               self.lineEditApplicationName.text())
        self.settings.setValue("DefaultDuration",
                               self.doubleSpinBoxDuration.value())
        self.settings.setValue("DefaultPreamble",
                               self.doubleSpinBoxPreamble.value())
        self.settings.setValue("DefaultDrawGraph",
                               int(self.checkBoxDrawGraph.isChecked()))
        self.settings.setValue("DefaultEventSchedSwitch",
                               int(self.checkBoxSchedSwitch.isChecked()))
        self.settings.setValue("DefaultEventCPUIdle",
                               int(self.checkBoxCPUIdle.isChecked()))
        self.settings.setValue(
            "DefaultEventBinderTransaction",
            int(self.checkBoxBinderTransaction.isChecked()),
        )
        self.settings.setValue("DefaultEventSyslogger",
                               int(self.checkBoxSyslogger.isChecked()))
        self.settings.setValue("DefaultEventWakeUp",
                               int(self.checkBoxWakeUp.isChecked()))
        self.settings.setValue("OptimizeWithThreads",
                               int(self.radioButtonMultiThreaded.isChecked()))
        self.settings.setValue(
            "OptimizeWithProcesses",
            int(self.radioButtonMultiProcessing.isChecked()))
        self.settings.setValue("OptimizeNone",
                               int(self.radioButtonNonthreaded.isChecked()))
        self.settings.setValue("UseUIConsole",
                               int(self.checkBoxUseUIConsole.isChecked()))

        # Syslogger
        self.settings.setValue("DefaultSysloggerCPU", self.spinBoxCPU.value())
        self.settings.setValue("DefaultSysloggerInterval",
                               self.spinBoxInterval.value())
        self.settings.setValue("DefaultSysloggerCPUInfo",
                               int(self.checkBoxCPUInfo.isChecked()))
        self.settings.setValue("DefaultSysloggerCPUFreq",
                               int(self.checkBoxCPUFrequency.isChecked()))
        self.settings.setValue("DefaultSysloggerPower",
                               int(self.checkBoxPower.isChecked()))
        self.settings.setValue("DefaultSysloggerMali",
                               int(self.checkBoxMali.isChecked()))
        self.settings.setValue("DefaultSysloggerTemp",
                               int(self.checkBoxTemp.isChecked()))
        self.settings.setValue("DefaultSysloggerNetwork",
                               int(self.checkBoxNetwork.isChecked()))

        super(SettingsMenu, self).accept()

    def reject(self):
        super(SettingsMenu, self).reject()


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        sys.stdout.flush()
        sys.stderr.flush()


class MainInterface(QMainWindow, MainInterface.Ui_MainWindow):
    results_path = ""
    changed_progress = pyqtSignal(int)
    changed_test_count = pyqtSignal(str)
    changed_test_progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setupUi(self)
        self.show()

        self.buttonkilladb()

        self.setupbuttons()
        self.setupmenu()

        self.settings = None
        self.setupsettings()
        self.getsettings()

        console_colour = QPalette(QColor(255, 255, 255, 255),
                                  QColor(0, 0, 0, 255))
        self.textEditConsole.setPalette(console_colour)
        self.UI_console = bool(
            int(self.settings.value("UseUIConsole", defaultValue=1)))
        if self.UI_console:
            sys.stdout = EmittingStream(textWritten=self.normal_output_written)
            sys.stderr = EmittingStream(textWritten=self.normal_output_written)
        else:
            self.textEditConsole.setText(
                "Standard console being used, this console can be enabled in the settings "
                "menu")

        # Persistant settings
        self.checkBoxSkipTracing.setChecked(
            bool(int(self.settings.value("SkipTracing", defaultValue=0))))
        self.checkBoxSkipTracing.stateChanged.connect(
            self.save_persistent_settings)

        # Threading
        self.jobs = []
        self.console_queue = Queue.Queue()
        self.console_task = threading.Thread(target=self.console,
                                             args=()).start()
        self.debug_task = None
        self.changed_progress.connect(self.progressBar.setValue)
        self.changed_test_count.connect(self.labelTestsCompleted.setText)
        self.changed_test_progress.connect(
            self.progressBarTestsCompleted.setValue)

        self.results_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "results/")
        self.trace_file = None
        self.results_file = None
        self.graph_file = None
        self.binder_log_file = None
        self.binder_log = []

        self.application_name = None
        self.events = []
        self.duration = 0  # TODO defaults
        self.events_to_process = 0
        self.preamble = 2
        self.graph = False
        self.subgraph = False
        self.skip_tracing = False
        self.pid = None

        # Governor control
        self.governorRadioButtons = []
        # try:
        #     self.adb = ADBInterface()
        # except Exception, e:
        #     print("Could not open an ADB connection to device")
        #     self.close()
        #     sys.exit()

        self.governor_controller = GovernorController()
        self.governor = self.setup_governors()

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        for job in self.jobs:
            job.terminate()

        self.console_task._stop_event.set()

    def save_persistent_settings(self):
        self.settings.setValue("SkipTracing",
                               int(self.checkBoxSkipTracing.isChecked()))

    def setup_governors(self):
        governors = self.governor_controller.get_governors()
        current_governor = self.governor_controller.get_current_governor()

        self.labelCurrentLittleGovernor.setText(str(current_governor[0]))
        self.labelCurrentBigGovernor.setText(str(current_governor[1]))

        for governor in governors:
            rb = QRadioButton(governor)

            self.governorRadioButtons.append(rb)

            if governor == current_governor[0]:
                rb.setChecked(True)
            else:
                rb.setChecked(False)
            rb.clicked.connect(lambda: self.governor_changed())
            self.verticalLayoutGovernors.addWidget(rb)

        self.update_frequency_display()

        self.pushButtonSetLittleFreqs.clicked.connect(
            self.set_little_frequencies)
        self.pushButtonResetLittleFreqs.clicked.connect(
            self.reset_little_frequencies)
        self.pushButtonSetBigFreqs.clicked.connect(self.set_big_frequencies)
        self.pushButtonResetBigFreqs.clicked.connect(
            self.reset_big_frequencies)

        return str(current_governor[0])

    def update_frequency_display(self):
        little_min = str(self.governor_controller.get_min_freq(0))
        little_max = str(self.governor_controller.get_max_freq(0))
        self.labelLittleMinFreq.setText(little_min)
        self.labelLittleMaxFreq.setText(little_max)
        self.lineEditLittleMinFreq.setText(little_min)
        self.lineEditLittleMaxFreq.setText(little_max)
        big_min = str(self.governor_controller.get_min_freq(4))
        big_max = str(self.governor_controller.get_max_freq(4))
        self.labelBigMinFreq.setText(big_min)
        self.labelBigMaxFreq.setText(big_max)
        self.lineEditBigMinFreq.setText(big_min)
        self.lineEditBigMaxFreq.setText(big_max)

    def set_little_frequencies(self):
        self.governor_controller.set_min_freq(
            0, self.lineEditLittleMinFreq.text())
        self.governor_controller.set_max_freq(
            0, self.lineEditLittleMaxFreq.text())
        self.update_frequency_display()

    def set_big_frequencies(self):
        self.governor_controller.set_min_freq(4,
                                              self.lineEditBigMinFreq.text())
        self.governor_controller.set_max_freq(4,
                                              self.lineEditBigMaxFreq.text())
        self.update_frequency_display()

    def reset_little_frequencies(self):
        self.governor_controller.reset_cpu_frequencies(0)
        self.update_frequency_display()

    def reset_big_frequencies(self):
        self.governor_controller.reset_cpu_frequencies(4)
        self.update_frequency_display()

    def governor_changed(self):
        new_governor = ""

        for rb in self.governorRadioButtons:
            if rb.isChecked():
                new_governor = rb.text()
                break

        self.governor_controller.set_governor(new_governor)
        self.labelCurrentLittleGovernor.setText(new_governor)
        self.labelCurrentBigGovernor.setText(new_governor)
        self.governor = str(new_governor)

    def console(self):
        cursor = self.textEditConsole.textCursor()
        while True:
            try:
                new_line = self.console_queue.get()
                cursor.movePosition(QTextCursor.End)
                cursor.insertText(new_line)
                self.textEditConsole.setTextCursor(cursor)
                self.textEditConsole.ensureCursorVisible()
            except Exception, e:
                print("Updating console failed, %s" % e)

    def normal_output_written(self, text):
        try:
            self.console_queue.put(str(text))
        except Exception, e:
            print("Writing to UI console failed, %s" % e)

    def getsettings(self):
        self.lineEditApplicationName.setText(
            self.settings.value("DefaultApplication", defaultValue=""))
        self.doubleSpinBoxDuration.setValue(
            float(self.settings.value("DefaultDuration", defaultValue=0.0)))
        self.doubleSpinBoxPreamble.setValue(
            float(self.settings.value("DefaultPreamble", defaultValue=0.0)))
        if float(self.settings.value("DefaultPreamble",
                                     defaultValue=0.0)) != 0.0:
            self.checkBoxPreamble.setChecked(True)
        self.checkBoxDrawGraph.setChecked(
            bool(int(self.settings.value("DefaultDrawGraph", defaultValue=0))))
        self.checkBoxWakeUp.setChecked(
            bool(int(self.settings.value("DefaultEventWakeUp",
                                         defaultValue=0))))
        self.checkBoxSchedSwitch.setChecked(
            bool(
                int(
                    self.settings.value("DefaultEventSchedSwitch",
                                        defaultValue=1))))
        self.checkBoxCPUIdle.setChecked(
            bool(
                int(self.settings.value("DefaultEventCPUIdle",
                                        defaultValue=0))))
        self.checkBoxBinderTransaction.setChecked(
            bool(
                int(
                    self.settings.value("DefaultEventBinderTransaction",
                                        defaultValue=1))))
        self.checkBoxSyslogger.setChecked(
            bool(
                int(
                    self.settings.value("DefaultEventSyslogger",
                                        defaultValue=1))))

    def setupsettings(self):
        self.settings = QSettings("HoffSoft", "Android Energy Debugger")

    def setupbuttons(self):
        self.pushButtonRun.clicked.connect(self.buttonrun)
        self.pushButtonKillADB.clicked.connect(self.buttonkilladb)
        self.pushButtonDisplayResults.clicked.connect(self.openresults)
        self.pushButtonDisplayOptimizations.clicked.connect(
            self.openoptimizations)
        self.pushButtonDisplayBinderLog.clicked.connect(self.openbinderlog)

    def setupmenu(self):
        self.actionOpenResults.triggered.connect(self.openresults)
        self.actionOpenBinderLog.triggered.connect(self.openbinderlog)
        self.actionOpenSettings.triggered.connect(self.opensettingsmenu)
        self.actionAbout.triggered.connect(self.openaboutdialog)

    def openallresults(self, subdir=None):
        self.openresults(subdir)
        self.openoptimizations(subdir)

    def openresults(self, subdir=None):
        self.openfile(self.tableWidgetResults, "_results.csv", subdir=subdir)

    def openoptimizations(self, subdir=None):
        self.openfile(self.tableWidgetOptimizations,
                      "_optimizations.csv",
                      subdir=subdir)

    def openfile(self, table_widget, file_suffix, subdir=None):
        if not table_widget:
            return

        table_widget.setRowCount(0)

        if self.lineEditApplicationName.text() is None:
            QMessageBox.warning(self, "Error", "Application is not specified",
                                QMessageBox.Ok)
            return

        self.application_name = self.lineEditApplicationName.text()
        if self.application_name == "":
            return
        if subdir is not None:
            results_filename = os.path.join(
                self.results_path,
                subdir + self.application_name + file_suffix)
        else:
            results_filename = os.path.join(
                self.results_path, self.application_name + file_suffix)

        try:
            col_count = 0
            row_count = 0
            with open(results_filename, "r") as fileInput:
                for row in csv.reader(fileInput):
                    row_count += 1
                    if len(row) > col_count:
                        col_count = len(row)

                fileInput.seek(0)
                table_widget.setColumnCount(col_count)
                table_widget.setRowCount(row_count)

                for i, row in enumerate(csv.reader(fileInput)):
                    for j, col in enumerate(row):
                        table_widget.setItem(i, j, QTableWidgetItem(col))
        except Exception, e:
            QMessageBox.warning(self, "Error", "{}".format(e), QMessageBox.Ok)

    def opensettingsmenu(self):
        settings_menu = SettingsMenu(self.settings)
        try:
            settings_menu.exec_()
        except Exception, e:
            print(e)
            self.close()
            sys.exit()

    def openaboutdialog(self):
        dialog = AboutDialog()
        dialog.exec_()

    def opengraph(self):
        pass

    def openbinderlog(self):
        if self.lineEditApplicationName.text() is None:
            QMessageBox.warning(self, "Error", "Application is not specified",
                                QMessageBox.Ok)
            return

        self.application_name = self.lineEditApplicationName.text()

        try:
            self.binder_log_file = open(
                os.path.join(self.results_path,
                             self.application_name + ".tlog"), "r")
        except Exception:
            QMessageBox.warning(self, "Error", "Binder log does not exist",
                                QMessageBox.Ok)
            return

        self.binder_log = []
        for line in self.binder_log_file:
            self.binder_log.append(line)
            self.textBrowserBinderLog.append(line)

        self.textBrowserBinderLog.verticalScrollBar().setValue(0)

    def checkrun(self):

        error = False
        error_str = "The following required parameters are missing:\n\n"
        if not self.lineEditApplicationName.text():
            error = True
            error_str += "Application Name\n"
        if self.doubleSpinBoxDuration.value() == 0.0:
            error = True
            error_str += "Duration"

        if error:
            raise Exception(error_str)

        return error

    def buttonrun(self):
        try:
            self.checkrun()

            if self.lineEditAppPID.text() != "":
                self.pid = self.lineEditAppPID.text()

            self.application_name = self.lineEditApplicationName.text()
            self.duration = self.doubleSpinBoxDuration.value()
            self.events = []
            if self.checkBoxBinderTransaction.isCheckable():
                self.events.append("binder_transaction")
            if self.checkBoxCPUIdle.isChecked():
                self.events.append("cpu_idle")
            if self.checkBoxSchedSwitch.isChecked():
                self.events.append("sched_switch")
            if self.checkBoxSyslogger.isChecked():
                self.events.append("sys_logger")
            if self.checkBoxWakeUp.isChecked():
                self.events.append("sched_wakeup")
            if self.checkBoxEvents.isChecked():
                self.events_to_process = self.spinBoxEvents.value()
            else:
                self.events_to_process = 0
            self.preamble = self.doubleSpinBoxPreamble.value()
            self.subgraph = self.checkBoxSubGraph.isChecked()
            self.graph = self.checkBoxDrawGraph.isChecked()
            self.skip_tracing = self.checkBoxSkipTracing.isChecked()

            if (self.checkBoxTestAutomation.isChecked()
                ):  # TODO allow test automation to be multithreaded
                no_of_tests = self.spinBoxNoOfTests.value()
                test_start_value = self.spinBoxStartTestValue.value()

                self.labelTestsCompleted.setText("0")
                self.progressBarTestsCompleted.setValue(0)

                for x in range(test_start_value,
                               test_start_value + no_of_tests):
                    try:
                        buttonrunprocess(self.application_name,
                                         self.governor[0],
                                         self.duration,
                                         self.events,
                                         self.events_to_process,
                                         self.preamble,
                                         self.subgraph,
                                         self.graph,
                                         self.skip_tracing,
                                         progress_signal=self.changed_progress,
                                         open_func=self.openallresults,
                                         subdir=self.application_name + "/" +
                                         self.governor + "/" + str(x) + "/",
                                         pid=self.pid)
                        if self.checkBoxTestAutomationPrompt.isChecked():
                            QMessageBox.information(
                                self,
                                "Test finished",
                                "Press OK to continue",
                                QMessageBox.Ok,
                            )
                        self.changed_test_count.emit(
                            str(x - test_start_value + 1))
                        self.changed_test_progress.emit(
                            round(
                                float(x - test_start_value + 1) /
                                float(no_of_tests) * 100))
                    except Exception, e:
                        print("test failed, retrying")
                        x -= 1
            else:
                if bool(
                        int(
                            self.settings.value("OptimizeWithThreads",
                                                defaultValue=1))):
                    print("Running debugger with multithreading")

                    if self.debug_task:
                        try:
                            self.debug_task.terminate()
                        except Exception:
                            print("Could not terminate current debug task")
                            return
                    self.debug_task = QDebuggerThread(
                        self.application_name,
                        self.governor[0],
                        self.duration,
                        self.events,
                        self.events_to_process,
                        self.preamble,
                        self.subgraph,
                        self.graph,
                        self.skip_tracing,
                        self.openallresults,
                    )
                    self.debug_task.changed_progress.connect(
                        self.progressBar.setValue)
                    self.debug_task.start()
                elif bool(
                        int(
                            self.settings.value("OptimizeWithProcesses",
                                                defaultValue=1))):
                    print(
                        "Running debugger with multiprocessing, outputing to system console"
                    )
                    # Separate processes means that the generated process cannot access the UI console created in the
                    # main program's process
                    sys.stdout = sys.__stdout__
                    sys.stderr = sys.__stderr__
                    proc = multiprocessing.Process(
                        target=buttonrunprocess,
                        args=(
                            self.application_name,
                            self.governor[0],
                            self.duration,
                            self.events,
                            self.events_to_process,
                            self.preamble,
                            self.subgraph,
                            self.graph,
                            self.skip_tracing,
                            self.changed_progress,
                            self.openallresults,
                        ),
                    )
                    self.jobs.append(proc)
                    proc.start()
                    if self.UI_console:
                        sys.stdout = EmittingStream(
                            textWritten=self.normal_output_written)
                        sys.stderr = EmittingStream(
                            textWritten=self.normal_output_written)
                else:
                    buttonrunprocess(
                        self.application_name,
                        self.governor[0],
                        self.duration,
                        self.events,
                        self.events_to_process,
                        self.preamble,
                        self.subgraph,
                        self.graph,
                        self.skip_tracing,
                        progress_signal=self.changed_progress,
                        open_func=self.openallresults,
                    )

        except Exception, e:
            QMessageBox.critical(self, "Error", e, QMessageBox.Ok)

    @staticmethod
    def buttonkilladb():
        os.system("killall adb")


def buttonrunprocess(
        application_name,
        governor,
        duration,
        events,
        events_to_process,
        preamble,
        subgraph,
        graph,
        skip_tracing,
        progress_signal=None,
        open_func=None,
        subdir=None,
        pid=None,
):

    try:
        current_debugger = EnergyDebugger(application=application_name,
                                          governor=governor,
                                          duration=duration,
                                          events=events,
                                          event_count=events_to_process,
                                          preamble=preamble,
                                          graph=graph,
                                          subgraph=subgraph,
                                          skip_tracing=skip_tracing,
                                          progress_signal=progress_signal,
                                          results_subdir=subdir,
                                          pid=pid)
        current_debugger.run()
        if open_func is not None:
            open_func(subdir)
    except Exception, e:
        print("Error: {}".format(e))

    print(" ------ FINISHED ------")


class QDebuggerThread(QThread):
    changed_progress = pyqtSignal(int)

    def __init__(
            self,
            application_name,
            governor,
            duration,
            events,
            events_to_process,
            preamble,
            subgraph,
            graph,
            skip_tracing,
            open_func,
    ):
        QThread.__init__(self)
        self.application_name = application_name
        self.governor = governor
        self.duration = duration
        self.events = events
        self.events_to_process = events_to_process
        self.preamble = preamble
        self.subgraph = subgraph
        self.graph = graph
        self.skip_tracing = skip_tracing
        self.open_func = open_func

    def run(self):
        buttonrunprocess(
            self.application_name,
            self.governor,
            self.duration,
            self.events,
            self.events_to_process,
            self.preamble,
            self.subgraph,
            self.graph,
            self.skip_tracing,
            self.changed_progress,
            self.open_func,
        )


class CommandInterface:
    def __init__(self):
        pass

    def checkrun(self):
        if not args.app:
            return False
        if not args.duration:
            return False

    def run(self):
        pass


class EnergyDebugger:
    def __init__(self,
                 application,
                 governor,
                 duration,
                 events,
                 event_count,
                 preamble,
                 graph,
                 subgraph,
                 skip_tracing,
                 progress_signal,
                 results_subdir,
                 pid=None):
        self.adb = ADBInterface()
        self.application = application
        self.governor = governor
        self.duration = duration
        self.events = []
        self.event_count = event_count
        self.preamble = preamble
        self.graph = graph
        self.subgraph = subgraph
        self.tc_processor = None
        self.skip_tracing = skip_tracing
        self.progress_signal = progress_signal
        self.results_subdir = results_subdir
        self.pid = pid
        """ Required objects for tracking system metrics and interfacing with a target system, connected
        via an ADB connection.
        """

        start_time = time.time()
        try:
            self.pid_tool = PIDTool(self.adb, self.application, self.pid)
        except Exception, e:
            raise Exception("Trace failed: {}".format(e))
        print("PIDs gathered --- %s Sec" % (time.time() - start_time))
        start_time = time.time()
        self.trace_processor = TraceProcessor(self.pid_tool, self.application)
        print("Trace processor created --- %s Sec" %
              (time.time() - start_time))
        start_time = time.time()
        self.sys_metrics = SystemMetrics(self.adb)
        print("System metrics initialized --- %s Sec" %
              (time.time() - start_time))
        """ The tracer object stores the configuration for the ftrace trace that is to be performed on the
        target system.
        """

        start_time = time.time()
        self.tracer = Tracer(
            adb_device=self.adb,
            name=application,
            metrics=self.sys_metrics,
            events=events,
            duration=duration,
        )
        print("Tracer created --- %s Sec" % (time.time() - start_time))

        if self.duration > 6:
            print "WARNING: Running traces over 6 seconds can cause issue due to data loss from trace buffer size " "limitations"
            QMessageBox.warning(
                self,
                "Warning",
                "Running traces over 6 seconds can cause issue due to data loss from trace buffer "
                "size limitations",
                QMessageBox.Ok,
            )

        start_time = time.time()
        self.sys_logger = SysLogger(self.adb)
        print("Syslogger created --- %s Sec" % (time.time() - start_time))

    def normalOutputWritten(self, text):
        cursor = self.textEditConsole.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEditConsole.setTextCursor(cursor)
        self.textEditConsole.ensureCursorVisible()

    def clear(self):
        # TODO
        pass

    def run(self):
        """ Entry point into the debugging tool.
        """
        """ As the energy debugger depends on the custom trace points implemented in the syslogger module,
        it must be loaded before tracing begins. It must then be unloaded and finished before the results
        are pulled from the target system.
        """
        start_time = time.time()

        if not self.skip_tracing:
            self.sys_logger.start()
            self.tracer.run_tracer(self.preamble, args.skip_clear)
            self.sys_logger.stop()
            try:
                self.tracer.get_trace_results()
            except Exception, e:
                print("Getting trace results failed, %s" % e)
        """ The tracecmd data pulled (.dat suffix) is then iterated through and the trace events are systematically
        processed. Results are generated into a CSV file, saved to the working directory under the same name as the 
        target
        application with the suffix _results.csv.
        """

        print "Creating trace processor"
        try:
            dat_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "results/" + self.application + ".dat",
            )
            self.tc_processor = TracecmdProcessor(dat_path, self.preamble)
            self.tc_processor.print_event_count()
        except Exception, e:
            print("Creating trace processor failed, %s" % e)

        try:
            self.trace_processor.process_trace(
                governor=self.governor,
                progress_signal=self.progress_signal,
                metrics=self.sys_metrics,
                tracecmd=self.tc_processor,
                duration=self.duration,
                draw=self.graph,
                test=self.event_count,
                subgraph=self.subgraph,
                subdir=self.results_subdir,
            )
        except Exception, e:
            raise Exception(e)

        print "Run took a total of %s seconds to run" % (time.time() -
                                                         start_time)


if __name__ == "__main__":
    if not args.commandline:
        app = QApplication(sys.argv)
        interface = MainInterface()
        sys.exit(app.exec_())
    else:
        app = CommandInterface()
        app.run()
