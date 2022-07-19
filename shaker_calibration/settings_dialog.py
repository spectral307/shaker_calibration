from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QSettings
from .ui.ui_settings_dialog import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__ui = Ui_SettingsDialog()
        self.__ui.setupUi(self)

        self.setFixedSize(self.size())

        self.__settings = QSettings()

        self.__ui.velocity_transform_checkbox.setChecked(
            self.__settings.value("transform_into_velocity_sensitivity", type=bool))

        extra_f = self.__settings.value("extra_f", type=list)
        self.__ui.extra_f_lineedit.setText(",".join(extra_f))

    def accept(self):
        self.__settings.setValue("transform_into_velocity_sensitivity",
                                 self.__ui.velocity_transform_checkbox.isChecked())

        extra_f_text = self.__ui.extra_f_lineedit.text()
        if extra_f_text:
            extra_f_strs = extra_f_text.split(",")
            try:
                extra_f = [int(val) for val in extra_f_strs]
            except ValueError:
                QMessageBox().critical(self, "Ошибка",
                                       "Дополнительные частоты должны быть целыми числами, разделёнными запятой.")
                return
        else:
            extra_f = []
        self.__settings.setValue("extra_f", extra_f)

        return super().accept()
