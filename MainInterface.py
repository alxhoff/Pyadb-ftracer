# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 714))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameTraceOptions = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTraceOptions.sizePolicy().hasHeightForWidth())
        self.frameTraceOptions.setSizePolicy(sizePolicy)
        self.frameTraceOptions.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameTraceOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTraceOptions.setObjectName("frameTraceOptions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameTraceOptions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frameTraceOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frameTraceOptions)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEditApplicationName = QtWidgets.QLineEdit(self.frameTraceOptions)
        self.lineEditApplicationName.setObjectName("lineEditApplicationName")
        self.horizontalLayout_3.addWidget(self.lineEditApplicationName)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frameTraceOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.doubleSpinBoxDuration = QtWidgets.QDoubleSpinBox(self.frameTraceOptions)
        self.doubleSpinBoxDuration.setObjectName("doubleSpinBoxDuration")
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxDuration)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBoxDrawGraph = QtWidgets.QCheckBox(self.frameTraceOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxDrawGraph.sizePolicy().hasHeightForWidth())
        self.checkBoxDrawGraph.setSizePolicy(sizePolicy)
        self.checkBoxDrawGraph.setObjectName("checkBoxDrawGraph")
        self.horizontalLayout_8.addWidget(self.checkBoxDrawGraph)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addWidget(self.frameTraceOptions)
        self.frameEvents = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameEvents.sizePolicy().hasHeightForWidth())
        self.frameEvents.setSizePolicy(sizePolicy)
        self.frameEvents.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameEvents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEvents.setObjectName("frameEvents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameEvents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frameEvents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxSyslogger = QtWidgets.QCheckBox(self.frameEvents)
        self.checkBoxSyslogger.setChecked(True)
        self.checkBoxSyslogger.setObjectName("checkBoxSyslogger")
        self.gridLayout.addWidget(self.checkBoxSyslogger, 0, 0, 1, 1)
        self.pushButtonEventReset = QtWidgets.QPushButton(self.frameEvents)
        self.pushButtonEventReset.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButtonEventReset.setBaseSize(QtCore.QSize(0, 0))
        self.pushButtonEventReset.setObjectName("pushButtonEventReset")
        self.gridLayout.addWidget(self.pushButtonEventReset, 3, 0, 1, 2)
        self.checkBoxWakeUp = QtWidgets.QCheckBox(self.frameEvents)
        self.checkBoxWakeUp.setObjectName("checkBoxWakeUp")
        self.gridLayout.addWidget(self.checkBoxWakeUp, 2, 0, 1, 1)
        self.checkBoxSchedSwitch = QtWidgets.QCheckBox(self.frameEvents)
        self.checkBoxSchedSwitch.setChecked(True)
        self.checkBoxSchedSwitch.setObjectName("checkBoxSchedSwitch")
        self.gridLayout.addWidget(self.checkBoxSchedSwitch, 1, 0, 1, 1)
        self.checkBoxCPUIdle = QtWidgets.QCheckBox(self.frameEvents)
        self.checkBoxCPUIdle.setObjectName("checkBoxCPUIdle")
        self.gridLayout.addWidget(self.checkBoxCPUIdle, 1, 1, 1, 1)
        self.checkBoxBinderTransaction = QtWidgets.QCheckBox(self.frameEvents)
        self.checkBoxBinderTransaction.setChecked(True)
        self.checkBoxBinderTransaction.setObjectName("checkBoxBinderTransaction")
        self.gridLayout.addWidget(self.checkBoxBinderTransaction, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.frameEvents)
        self.frameDisplayOptions = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameDisplayOptions.sizePolicy().hasHeightForWidth())
        self.frameDisplayOptions.setSizePolicy(sizePolicy)
        self.frameDisplayOptions.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDisplayOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDisplayOptions.setObjectName("frameDisplayOptions")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frameDisplayOptions)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frameDisplayOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBoxDisplayGraph = QtWidgets.QCheckBox(self.frameDisplayOptions)
        self.checkBoxDisplayGraph.setObjectName("checkBoxDisplayGraph")
        self.gridLayout_2.addWidget(self.checkBoxDisplayGraph, 0, 1, 1, 1)
        self.checkBoxDisplayResults = QtWidgets.QCheckBox(self.frameDisplayOptions)
        self.checkBoxDisplayResults.setChecked(True)
        self.checkBoxDisplayResults.setObjectName("checkBoxDisplayResults")
        self.gridLayout_2.addWidget(self.checkBoxDisplayResults, 0, 0, 1, 1)
        self.checkBoxDisplayBinderLog = QtWidgets.QCheckBox(self.frameDisplayOptions)
        self.checkBoxDisplayBinderLog.setObjectName("checkBoxDisplayBinderLog")
        self.gridLayout_2.addWidget(self.checkBoxDisplayBinderLog, 1, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.frameDisplayOptions)
        self.frameDebugOptions = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameDebugOptions.sizePolicy().hasHeightForWidth())
        self.frameDebugOptions.setSizePolicy(sizePolicy)
        self.frameDebugOptions.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDebugOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDebugOptions.setObjectName("frameDebugOptions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameDebugOptions)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frameDebugOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBoxEvents = QtWidgets.QCheckBox(self.frameDebugOptions)
        self.checkBoxEvents.setObjectName("checkBoxEvents")
        self.horizontalLayout_5.addWidget(self.checkBoxEvents)
        self.spinBoxEvents = QtWidgets.QSpinBox(self.frameDebugOptions)
        self.spinBoxEvents.setMaximum(1000000)
        self.spinBoxEvents.setProperty("value", 300)
        self.spinBoxEvents.setObjectName("spinBoxEvents")
        self.horizontalLayout_5.addWidget(self.spinBoxEvents)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBoxPreamble = QtWidgets.QCheckBox(self.frameDebugOptions)
        self.checkBoxPreamble.setObjectName("checkBoxPreamble")
        self.horizontalLayout_6.addWidget(self.checkBoxPreamble)
        self.doubleSpinBoxPreamble = QtWidgets.QDoubleSpinBox(self.frameDebugOptions)
        self.doubleSpinBoxPreamble.setObjectName("doubleSpinBoxPreamble")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxPreamble)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.checkBoxSubGraph = QtWidgets.QCheckBox(self.frameDebugOptions)
        self.checkBoxSubGraph.setObjectName("checkBoxSubGraph")
        self.verticalLayout_3.addWidget(self.checkBoxSubGraph)
        self.checkBoxSkipTracing = QtWidgets.QCheckBox(self.frameDebugOptions)
        self.checkBoxSkipTracing.setObjectName("checkBoxSkipTracing")
        self.verticalLayout_3.addWidget(self.checkBoxSkipTracing)
        self.verticalLayout_2.addWidget(self.frameDebugOptions)
        self.frameProgress = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameProgress.sizePolicy().hasHeightForWidth())
        self.frameProgress.setSizePolicy(sizePolicy)
        self.frameProgress.setFrameShape(QtWidgets.QFrame.Box)
        self.frameProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameProgress.setObjectName("frameProgress")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameProgress)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frameProgress)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.frameProgress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.progressBar = QtWidgets.QProgressBar(self.frameProgress)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_11.addWidget(self.progressBar)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.label_7 = QtWidgets.QLabel(self.frameProgress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.textEditConsole = QtWidgets.QTextEdit(self.frameProgress)
        self.textEditConsole.setAutoFillBackground(True)
        self.textEditConsole.setObjectName("textEditConsole")
        self.verticalLayout_6.addWidget(self.textEditConsole)
        self.verticalLayout_2.addWidget(self.frameProgress)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonRun = QtWidgets.QPushButton(self.frame)
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.horizontalLayout_2.addWidget(self.pushButtonRun)
        self.pushButtonKillADB = QtWidgets.QPushButton(self.frame)
        self.pushButtonKillADB.setObjectName("pushButtonKillADB")
        self.horizontalLayout_2.addWidget(self.pushButtonKillADB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidgetShow = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetShow.sizePolicy().hasHeightForWidth())
        self.tabWidgetShow.setSizePolicy(sizePolicy)
        self.tabWidgetShow.setObjectName("tabWidgetShow")
        self.tabResults = QtWidgets.QWidget()
        self.tabResults.setObjectName("tabResults")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabResults)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tableWidgetResults = QtWidgets.QTableWidget(self.tabResults)
        self.tableWidgetResults.setObjectName("tableWidgetResults")
        self.tableWidgetResults.setColumnCount(0)
        self.tableWidgetResults.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidgetResults)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButtonDisplayResults = QtWidgets.QPushButton(self.tabResults)
        self.pushButtonDisplayResults.setObjectName("pushButtonDisplayResults")
        self.horizontalLayout_7.addWidget(self.pushButtonDisplayResults, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tabWidgetShow.addTab(self.tabResults, "")
        self.tabGraph = QtWidgets.QWidget()
        self.tabGraph.setObjectName("tabGraph")
        self.tabWidgetShow.addTab(self.tabGraph, "")
        self.tabBinderLog = QtWidgets.QWidget()
        self.tabBinderLog.setObjectName("tabBinderLog")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabBinderLog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.tabBinderLog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabBinderLog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_2)
        self.pushButtonRunBinderFilter = QtWidgets.QPushButton(self.tabBinderLog)
        self.pushButtonRunBinderFilter.setObjectName("pushButtonRunBinderFilter")
        self.horizontalLayout_10.addWidget(self.pushButtonRunBinderFilter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.textBrowserBinderLog = QtWidgets.QTextBrowser(self.tabBinderLog)
        self.textBrowserBinderLog.setObjectName("textBrowserBinderLog")
        self.verticalLayout_7.addWidget(self.textBrowserBinderLog)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButtonDisplayBinderLog = QtWidgets.QPushButton(self.tabBinderLog)
        self.pushButtonDisplayBinderLog.setObjectName("pushButtonDisplayBinderLog")
        self.horizontalLayout_9.addWidget(self.pushButtonDisplayBinderLog, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.tabWidgetShow.addTab(self.tabBinderLog, "")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 19))
        self.menubar.setObjectName("menubar")
        self.menuFike = QtWidgets.QMenu(self.menubar)
        self.menuFike.setObjectName("menuFike")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setShortcut("")
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon1)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_Graph = QtWidgets.QAction(MainWindow)
        self.actionOpen_Graph.setObjectName("actionOpen_Graph")
        self.actionOpen_Graph_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_Graph_2.setObjectName("actionOpen_Graph_2")
        self.actionOpenGraph = QtWidgets.QAction(MainWindow)
        self.actionOpenGraph.setObjectName("actionOpenGraph")
        self.actionOpenSettings = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenSettings.setIcon(icon2)
        self.actionOpenSettings.setObjectName("actionOpenSettings")
        self.actionOpenBinderLog = QtWidgets.QAction(MainWindow)
        self.actionOpenBinderLog.setObjectName("actionOpenBinderLog")
        self.actionOpenTrace = QtWidgets.QAction(MainWindow)
        self.actionOpenTrace.setObjectName("actionOpenTrace")
        self.actionOpenResults = QtWidgets.QAction(MainWindow)
        self.actionOpenResults.setObjectName("actionOpenResults")
        self.actionQuitProgram = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuitProgram.setIcon(icon3)
        self.actionQuitProgram.setObjectName("actionQuitProgram")
        self.menuFike.addSeparator()
        self.menuFike.addSeparator()
        self.menuFike.addAction(self.actionOpenGraph)
        self.menuFike.addAction(self.actionOpenBinderLog)
        self.menuFike.addAction(self.actionOpenResults)
        self.menuFike.addAction(self.actionOpenSettings)
        self.menuFike.addAction(self.actionQuitProgram)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFike.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetShow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Android Energy Debugger"))
        self.label_6.setText(_translate("MainWindow", "<b>Trace</b>"))
        self.label.setText(_translate("MainWindow", "Application:"))
        self.label_3.setText(_translate("MainWindow", "Trace Duration:"))
        self.checkBoxDrawGraph.setText(_translate("MainWindow", "Draw Graph File (.dot)"))
        self.label_5.setText(_translate("MainWindow", "<b>Events</b>"))
        self.checkBoxSyslogger.setText(_translate("MainWindow", "Syslogger"))
        self.pushButtonEventReset.setText(_translate("MainWindow", "Default Events"))
        self.checkBoxWakeUp.setText(_translate("MainWindow", "Wake Up"))
        self.checkBoxSchedSwitch.setText(_translate("MainWindow", "Sched Switch"))
        self.checkBoxCPUIdle.setText(_translate("MainWindow", "CPU Idle"))
        self.checkBoxBinderTransaction.setText(_translate("MainWindow", "Binder Transaction"))
        self.label_9.setText(_translate("MainWindow", "<b>Display Options</b>"))
        self.checkBoxDisplayGraph.setText(_translate("MainWindow", "Graph"))
        self.checkBoxDisplayResults.setText(_translate("MainWindow", "Results"))
        self.checkBoxDisplayBinderLog.setText(_translate("MainWindow", "Binder Log"))
        self.label_2.setText(_translate("MainWindow", "<b>Debug Options</b>"))
        self.checkBoxEvents.setText(_translate("MainWindow", "Events to Process"))
        self.checkBoxPreamble.setText(_translate("MainWindow", "Custom Preamble"))
        self.checkBoxSubGraph.setText(_translate("MainWindow", "Draw Node Sub-graphs"))
        self.checkBoxSkipTracing.setText(_translate("MainWindow", "Skip tracing (assumed previously done)"))
        self.label_10.setText(_translate("MainWindow", "Multithreading only"))
        self.label_4.setText(_translate("MainWindow", "Progress"))
        self.label_7.setText(_translate("MainWindow", "Console"))
        self.pushButtonRun.setText(_translate("MainWindow", "Run"))
        self.pushButtonKillADB.setText(_translate("MainWindow", "Manually Kill ADB"))
        self.pushButtonDisplayResults.setText(_translate("MainWindow", "Display Results"))
        self.tabWidgetShow.setTabText(self.tabWidgetShow.indexOf(self.tabResults), _translate("MainWindow", "Results"))
        self.tabWidgetShow.setTabText(self.tabWidgetShow.indexOf(self.tabGraph), _translate("MainWindow", "Graph"))
        self.label_8.setText(_translate("MainWindow", "Filter:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Search for lines containing...."))
        self.pushButtonRunBinderFilter.setText(_translate("MainWindow", "Run"))
        self.pushButtonDisplayBinderLog.setText(_translate("MainWindow", "Display Log"))
        self.tabWidgetShow.setTabText(self.tabWidgetShow.indexOf(self.tabBinderLog), _translate("MainWindow", "Binder Log"))
        self.menuFike.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_Graph.setText(_translate("MainWindow", "Open Graph"))
        self.actionOpen_Graph_2.setText(_translate("MainWindow", "Open Graph"))
        self.actionOpenGraph.setText(_translate("MainWindow", "Open Graph"))
        self.actionOpenGraph.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpenSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpenBinderLog.setText(_translate("MainWindow", "Open Binder Log"))
        self.actionOpenTrace.setText(_translate("MainWindow", "Open Trace"))
        self.actionOpenResults.setText(_translate("MainWindow", "Open Results"))
        self.actionQuitProgram.setText(_translate("MainWindow", "Quit"))
        self.actionQuitProgram.setShortcut(_translate("MainWindow", "Ctrl+Q"))
