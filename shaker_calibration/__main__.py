from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings, QDir
from os.path import exists
import sys
from .main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("shaker_calibration")
    app.setOrganizationName("GTLab")
    app.setOrganizationDomain("gtlab.pro")

    settings = QSettings()

    default_dir = "F:\\3. Метрология"
    if not exists(default_dir):
        default_dir = QDir.home().absolutePath()

    if settings.value("afc_report_dir") is None:
        settings.setValue(
            "afc_report_dir", default_dir)

    if settings.value("acref_dir") is None:
        settings.setValue(
            "acref_dir", default_dir)

    if settings.value("use_same_afc_report_and_acref_dir") is None:
        settings.setValue("use_same_afc_report_and_acref_dir", False)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
