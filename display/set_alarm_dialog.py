# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\set_alarm_dialog.ui'
#
# Created: Tue Nov 24 22:06:35 2015
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonBox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.timeEdit = QtGui.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(180, 50, 431, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(51)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet(_fromUtf8("QTimeEdit::down-button {width:80px}\n"
"QTimeEdit::up-button {width:80px}"))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 290, 771, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radio_sun = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_sun.setFont(font)
        self.radio_sun.setObjectName(_fromUtf8("radio_sun"))
        self.horizontalLayout.addWidget(self.radio_sun)
        self.radio_man = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_man.setFont(font)
        self.radio_man.setObjectName(_fromUtf8("radio_man"))
        self.horizontalLayout.addWidget(self.radio_man)
        self.radio_tue = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_tue.setFont(font)
        self.radio_tue.setObjectName(_fromUtf8("radio_tue"))
        self.horizontalLayout.addWidget(self.radio_tue)
        self.radio_wed = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_wed.setFont(font)
        self.radio_wed.setObjectName(_fromUtf8("radio_wed"))
        self.horizontalLayout.addWidget(self.radio_wed)
        self.radio_thu = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_thu.setFont(font)
        self.radio_thu.setObjectName(_fromUtf8("radio_thu"))
        self.horizontalLayout.addWidget(self.radio_thu)
        self.radio_fri = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_fri.setFont(font)
        self.radio_fri.setObjectName(_fromUtf8("radio_fri"))
        self.horizontalLayout.addWidget(self.radio_fri)
        self.radio_sat = QtGui.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radio_sat.setFont(font)
        self.radio_sat.setObjectName(_fromUtf8("radio_sat"))
        self.horizontalLayout.addWidget(self.radio_sat)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 97, 93, 91))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.radio_sun.setText(_translate("Dialog", "Søn", None))
        self.radio_man.setText(_translate("Dialog", "Man", None))
        self.radio_tue.setText(_translate("Dialog", "Tirs", None))
        self.radio_wed.setText(_translate("Dialog", "Ons", None))
        self.radio_thu.setText(_translate("Dialog", "Tors", None))
        self.radio_fri.setText(_translate("Dialog", "Fre", None))
        self.radio_sat.setText(_translate("Dialog", "Lør", None))

