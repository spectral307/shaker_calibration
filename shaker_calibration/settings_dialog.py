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

        self.__ui.displacement_transform_checkbox.setChecked(
            self.__settings.value("transform_into_displacement_sensitivity", type=bool))

        self.__ui.accel_ptp_transform_checkbox.setChecked(
            self.__settings.value("transform_into_accel_ptp_sens", type=bool))

        extra_f = self.__settings.value("extra_f", type=list)
        self.__ui.extra_f_lineedit.setText(",".join(extra_f))

    def accept(self):
        self.__settings.setValue("transform_into_velocity_sensitivity",
                                 self.__ui.velocity_transform_checkbox.isChecked())

        self.__settings.setValue("transform_into_displacement_sensitivity",
                                 self.__ui.displacement_transform_checkbox.isChecked())

        self.__settings.setValue("transform_into_accel_ptp_sens",
                                 self.__ui.accel_ptp_transform_checkbox.isChecked())

        extra_f = []
        extra_f_text = self.__ui.extra_f_lineedit.text().strip()
        extra_f_strs = extra_f_text.split(",")
        if not (len(extra_f_strs) == 1 and extra_f_strs[0] == ""):
            try:
                for val in extra_f_strs:
                    extra_f.append(int(val))
            except ValueError:
                QMessageBox().critical(self, "Ошибка",
                                       "Дополнительные частоты должны быть целыми числами, разделёнными запятой.")
                return
        self.__settings.setValue("extra_f", extra_f)

        return super().accept()
