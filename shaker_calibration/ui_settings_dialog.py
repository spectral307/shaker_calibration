# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 160)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.velocity_transform_checkbox = QtWidgets.QCheckBox(SettingsDialog)
        self.velocity_transform_checkbox.setGeometry(QtCore.QRect(20, 20, 291, 20))
        self.velocity_transform_checkbox.setObjectName("velocity_transform_checkbox")
        self.extra_f_label = QtWidgets.QLabel(SettingsDialog)
        self.extra_f_label.setGeometry(QtCore.QRect(20, 50, 361, 16))
        self.extra_f_label.setObjectName("extra_f_label")
        self.extra_f_lineedit = QtWidgets.QLineEdit(SettingsDialog)
        self.extra_f_lineedit.setGeometry(QtCore.QRect(20, 70, 361, 22))
        self.extra_f_lineedit.setObjectName("extra_f_lineedit")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(SettingsDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Настройки"))
        self.velocity_transform_checkbox.setText(_translate("SettingsDialog", "Преобразовать в чувствительность по скорости"))
        self.extra_f_label.setText(_translate("SettingsDialog", "Интерполировать на дополнительных частотах (через запятую):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsDialog = QtWidgets.QDialog()
    ui = Ui_SettingsDialog()
    ui.setupUi(SettingsDialog)
    SettingsDialog.show()
    sys.exit(app.exec())