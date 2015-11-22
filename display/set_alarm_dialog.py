# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\set_alarm_dialog.ui'
#
# Created: Sun Nov 22 07:42:17 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 480)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(520, 411, 251, 51))
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.timeEdit = QtGui.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(180, 50, 431, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(51)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 290, 771, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.horizontalLayout.addWidget(self.radioButton_8)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 100, 90, 90))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.radioButton.setText(_translate("Dialog", "Søn", None))
        self.radioButton_2.setText(_translate("Dialog", "Man", None))
        self.radioButton_3.setText(_translate("Dialog", "Tirs", None))
        self.radioButton_4.setText(_translate("Dialog", "Ons", None))
        self.radioButton_5.setText(_translate("Dialog", "Tors", None))
        self.radioButton_6.setText(_translate("Dialog", "Fre", None))
        self.radioButton_7.setText(_translate("Dialog", "Lør", None))
        self.radioButton_8.setText(_translate("Dialog", "UkeD", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))

