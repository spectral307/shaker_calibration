from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt6.QtCore import QSettings
from openpyxl import load_workbook
from os.path import dirname, basename, join, splitext
from .ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        # self.setFixedSize(self.size())

        self.__ui.open_afc_report_action.triggered.connect(
            self.open_afc_report)
        self.__ui.exit_action.triggered.connect(self.exit)

    def open_afc_report(self):
        settings = QSettings()

        afc_report_dir = settings.value("afc_report_dir")

        res = QFileDialog.getOpenFileName(
            self, "Открыть протокол АЧХ",
            afc_report_dir, "Файлы xlsm (*.xlsm)")

        afc_report_path = res[0]
        if not afc_report_path:
            return

        new_afc_report_dir = dirname(afc_report_path)
        afc_report_filename = basename(afc_report_path)
        if new_afc_report_dir != afc_report_dir:
            settings.setValue("afc_report_dir", new_afc_report_dir)

        wb = load_workbook(afc_report_path)
        ws = wb["data"]

        cur_row = 2
        cur_col = 5

        f = []
        while value := ws.cell(cur_row, cur_col).value:
            f.append(value)
            cur_row += 1

        cur_row = 2
        cur_col += 1

        s = []
        while value := ws.cell(cur_row, cur_col).value:
            s.append(value)
            cur_row += 1

        if len(f) != len(s):
            raise BaseException(
                "Длина вектора частоты не равна длине вектора чувствительности")

        if settings.value("use_same_afc_report_and_acref_dir", type=bool):
            acref_dir = new_afc_report_dir
        else:
            acref_dir = settings.value("acref_dir")

        default_acref_path = join(acref_dir, splitext(
            afc_report_filename)[0] + ".acref")

        res = QFileDialog.getSaveFileName(
            self, "Сохранить acref-файл",
            default_acref_path, "Файлы acref (*.acref)")

        acref_path = res[0]
        if not acref_path:
            return

        new_acref_dir = dirname(acref_path)
        # acref_filename = basename(acref_path)

        if new_acref_dir == new_afc_report_dir:
            settings.setValue("use_same_afc_report_and_acref_dir", True)
        else:
            settings.setValue("use_same_afc_report_and_acref_dir", False)
            if new_acref_dir != settings.value("acref_dir"):
                settings.setValue("acref_dir", new_acref_dir)

        with open(acref_path, "w") as file:
            file.writelines([
                "<?xml version=\"1.0\" encoding=\"windows-1251\"?>\n",
                "<afc_ref>\n",
                "<table>\n",
                "<column width=\"100\"/>\n",
                "<column width=\"100\"/>\n"
            ])

            for i, v in enumerate(f):
                file.write(
                    f"<row frequency=\"{f[i]}\" sensitivity=\"{s[i]}\"/>\n")

            file.writelines([
                "</table>\n",
                "</afc_ref>\n"
            ])

        self.__ui.statusbar.showMessage(f"{acref_path} сохранен")

    def exit(self):
        QApplication.quit()
