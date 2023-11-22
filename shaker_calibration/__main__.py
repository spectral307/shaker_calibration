from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings, QDir
import sys
from .main_window import MainWindow


def init_settings(settings: QSettings):
    default_dir = QDir.home().absolutePath()

    if settings.value("transform_into_velocity_sensitivity") is None:
        settings.setValue("transform_into_velocity_sensitivity", False)

    if settings.value("transform_into_displacement_sensitivity") is None:
        settings.setValue("transform_into_displacement_sensitivity", False)

    if settings.value("extra_fi") is None:
        settings.setValue("extra_fi", [])

    if settings.value("default_afc_report_dir") is None:
        settings.setValue(
            "default_afc_report_dir", default_dir)

    if settings.value("default_afcref_dir") is None:
        settings.setValue(
            "default_afcref_dir", default_dir)

    if settings.value("use_same_default_afc_report_and_afcref_dir") is None:
        settings.setValue("use_same_default_afc_report_and_afcref_dir", False)


def clear_settings(settings: QSettings):
    settings.clear()


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("shaker_calibration")
    app.setOrganizationName("GTLab")
    app.setOrganizationDomain("gtlab.pro")

    settings = QSettings()

    init_settings(settings)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
