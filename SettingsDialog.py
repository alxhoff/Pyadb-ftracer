# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSettings(object):
    def setupUi(self, DialogSettings):
        DialogSettings.setObjectName("DialogSettings")
        DialogSettings.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DialogSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditApplicationName = QtWidgets.QLineEdit(DialogSettings)
        self.lineEditApplicationName.setObjectName("lineEditApplicationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditApplicationName)
        self.label_2 = QtWidgets.QLabel(DialogSettings)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBoxDuration = QtWidgets.QDoubleSpinBox(DialogSettings)
        self.doubleSpinBoxDuration.setObjectName("doubleSpinBoxDuration")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxDuration)
        self.label_3 = QtWidgets.QLabel(DialogSettings)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxPreamble = QtWidgets.QDoubleSpinBox(DialogSettings)
        self.doubleSpinBoxPreamble.setObjectName("doubleSpinBoxPreamble")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxPreamble)
        self.label_4 = QtWidgets.QLabel(DialogSettings)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.frame = QtWidgets.QFrame(DialogSettings)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxSyslogger = QtWidgets.QCheckBox(self.frame)
        self.checkBoxSyslogger.setObjectName("checkBoxSyslogger")
        self.verticalLayout_2.addWidget(self.checkBoxSyslogger)
        self.checkBoxBinderTransaction = QtWidgets.QCheckBox(self.frame)
        self.checkBoxBinderTransaction.setObjectName("checkBoxBinderTransaction")
        self.verticalLayout_2.addWidget(self.checkBoxBinderTransaction)
        self.checkBoxSchedSwitch = QtWidgets.QCheckBox(self.frame)
        self.checkBoxSchedSwitch.setObjectName("checkBoxSchedSwitch")
        self.verticalLayout_2.addWidget(self.checkBoxSchedSwitch)
        self.checkBoxCPUIdle = QtWidgets.QCheckBox(self.frame)
        self.checkBoxCPUIdle.setObjectName("checkBoxCPUIdle")
        self.verticalLayout_2.addWidget(self.checkBoxCPUIdle)
        self.checkBoxWakeUp = QtWidgets.QCheckBox(self.frame)
        self.checkBoxWakeUp.setObjectName("checkBoxWakeUp")
        self.verticalLayout_2.addWidget(self.checkBoxWakeUp)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.label_5 = QtWidgets.QLabel(DialogSettings)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.checkBoxDrawGraph = QtWidgets.QCheckBox(DialogSettings)
        self.checkBoxDrawGraph.setObjectName("checkBoxDrawGraph")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBoxDrawGraph)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogSettings)
        self.buttonBox.accepted.connect(DialogSettings.accept)
        self.buttonBox.rejected.connect(DialogSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSettings)

    def retranslateUi(self, DialogSettings):
        _translate = QtCore.QCoreApplication.translate
        DialogSettings.setWindowTitle(_translate("DialogSettings", "Settings"))
        self.label.setText(_translate("DialogSettings", "Default Application Name"))
        self.label_2.setText(_translate("DialogSettings", "Default Duration"))
        self.label_3.setText(_translate("DialogSettings", "Default Preamble"))
        self.label_4.setText(_translate("DialogSettings", "Default Events"))
        self.checkBoxSyslogger.setText(_translate("DialogSettings", "Syslogger"))
        self.checkBoxBinderTransaction.setText(_translate("DialogSettings", "Binder Transaction"))
        self.checkBoxSchedSwitch.setText(_translate("DialogSettings", "Sched Switch"))
        self.checkBoxCPUIdle.setText(_translate("DialogSettings", "CPU Idle"))
        self.checkBoxWakeUp.setText(_translate("DialogSettings", "Wake Up"))
        self.label_5.setText(_translate("DialogSettings", "Draw Graph by  Default"))
        self.checkBoxDrawGraph.setText(_translate("DialogSettings", "Draw Graph"))
