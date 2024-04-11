from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from window import Ui_MainWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculate_1.clicked.connect(self.task_1)
        self.ui.calculate_2.clicked.connect(self.task_2)
        self.ui.calculate_3.clicked.connect(self.task_3)
        self.ui.calculate_4.clicked.connect(self.task_4)
        self.ui.calculate_5.clicked.connect(self.task_5)
        self.ui.calcul_task4.clicked.connect(self.calcul_task4)
        self.ui.calcul_task5.clicked.connect(self.calcul_task5)
        self.ui.lineEdit_N.textChanged.connect(self.generate_table)
        self.ui.calculate_6.clicked.connect(self.task_6)

    def task_1(self):
        input_text_1 = self.ui.lineEdit_N1.text()
        input_text_2 = self.ui.lineEdit_t1.text()
        input_text_3 = self.ui.lineEdit_nt1.text()

        try:
            N = float(input_text_1)
            t = float(input_text_2)
            n = float(input_text_3)

            if N <= 0:
                raise ValueError("N должно быть больше нуля")
            if t <= 0:
                raise ValueError("t должно быть больше нуля")
            if n <= 0:
                raise ValueError("n должно быть больше нуля")
            if n >= N:
                raise ValueError("n должно быть меньше N")

            n_t = N - n
            P = n_t / N
            result = 1 - P
            self.ui.result_label1.setText(str(round(result, 2)))

        except ValueError as e:
            error_label = ''
            if input_text_1 == '':
                error_label = 'N1'
            elif input_text_2 == '':
                error_label = 't1'
            elif input_text_3 == '':
                error_label = 'nt1'

            self.ui.result_label1.setText("Некорректный ввод в поле " + error_label + ": " + str(e))
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректный ввод в поле " + error_label + ": " + str(e))

    def task_2(self):
        input_text_1 = self.ui.lineEdit_N2.text()
        input_text_2 = self.ui.lineEdit_t2.text()
        input_text_3 = self.ui.lineEdit_deltat1.text()
        input_text_4 = self.ui.lineEdit_nt2.text()
        input_text_5 = self.ui.lineEdit_deltatnt1.text()

        error_label = ''

        try:
            N = float(input_text_1)
            t = float(input_text_2)
            delta_t = float(input_text_3)
            n = float(input_text_4)
            delta_n_t1 = float(input_text_5)

            if N <= 0:
                raise ValueError("N должно быть больше нуля")
            if t <= 0:
                raise ValueError("t должно быть больше нуля")
            if n < 0:
                raise ValueError("n должно быть больше или равно нулю")
            if delta_t <= 0:
                raise ValueError("delta_n_t1 должно быть больше нуля")
            if delta_n_t1 <= 0:
                raise ValueError("delta_n_t1 должно быть больше или равно нулю")
            F = delta_n_t1 / (N * delta_t)
            L = delta_n_t1 / (delta_t * (N - n))
            result = f"F: {str(F)}" + "\t\t" + f"L: {str(L)}"
            self.ui.result_label2.setText(result)

        except ValueError as e:
            if input_text_1 == '':
                error_label = 'N1'
            elif input_text_2 == '':
                error_label = 't'
            elif input_text_3 == '':
                error_label = 'delta_t'
            elif input_text_4 == '':
                error_label = 'nt'
            elif input_text_5 == '':
                error_label = 'delta_n_t1'

            self.ui.result_label2.setText("Некорректный ввод в поле " + error_label + ": " + str(e))
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректный ввод в поле " + error_label + ": " + str(e))

    def task_3(self):
        input_text_1 = self.ui.lineEdit_N3.text()
        input_text_2 = self.ui.lineEdit_t3.text()
        input_text_3 = self.ui.lineEdit_nt3.text()
        input_text_4 = self.ui.lineEdit_deltat2.text()
        input_text_5 = self.ui.lineEdit_deltatnt3.text()
        error_label = ''
        try:
            N = float(input_text_1)
            t = float(input_text_2)
            n = float(input_text_3)
            delta_t = float(input_text_4)
            delta_n_t2 = float(input_text_5)

            if N <= 0:
                raise ValueError("N должно быть больше нуля")
            if t <= 0:
                raise ValueError("t должно быть больше нуля")
            if delta_t <= 0:
                raise ValueError("delta_t должно быть больше нуля")
            if delta_n_t2 <= 0:
                raise ValueError("delta_n_t2 должно быть больше нуля")

            p1 = n / N
            p2 = delta_n_t2 / N
            F = p2 / delta_t
            L = p1 / delta_n_t2
            result = f"F: {str(F)}" + "\t\t" + f"L: {str(L)}"
            self.ui.result_label3.setText(result)

        except ValueError as e:
            if input_text_1 == '':
                error_label = 'N'
            elif input_text_2 == '':
                error_label = 't'
            elif input_text_3 == '':
                error_label = 'n'
            elif input_text_4 == '':
                error_label = 'delta_t'
            elif input_text_5 == '':
                error_label = 'delta_n_t2'
            self.ui.result_label3.setText("Некорректный ввод в поле " + error_label + ": " + str(e))
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректный ввод в поле " + error_label + ": " + str(e))

    def task_4(self):
        num_text = self.ui.lineEdit_ti.text()
        if not num_text.isdigit():
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректный ввод в поле 'ti'")
            return

        num = int(num_text)
        if num < 1 or num > 10:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число должно быть от 1 до 10")
            return

        # Удаляем предыдущие QLineEdit, если они есть
        for i in reversed(range(self.ui.gridLayout_1.count())):
            widget = self.ui.gridLayout_1.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QLineEdit):
                self.ui.gridLayout_1.removeWidget(widget)
                widget.deleteLater()

        self.line_edits = []

        # Создаем новые QLineEdit
        for i in range(num):
            line_edit = QtWidgets.QLineEdit()
            self.ui.gridLayout_1.addWidget(line_edit, i, 0)
            self.line_edits.append(line_edit)

        self.set_cell_style()
        self.ui.result_label4.setText("")


    def set_cell_style(self):
        style = (
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"
            "border-radius: 5px;"
            "border-color: rgb(255, 255, 255);"
            "border: 1px solid #000000;"
        )

        for i in range(self.ui.gridLayout_1.rowCount()):
            for j in range(self.ui.gridLayout_1.columnCount()):
                widget = self.ui.gridLayout_1.itemAtPosition(i, j)
                if widget is not None:
                    widget.widget().setStyleSheet(style)
                    widget.widget().setAlignment(QtCore.Qt.AlignCenter)


    def calcul_task4(self):
        try:
            total = 0
            # count = 0

            for line_edit in self.line_edits:
                value_text = line_edit.text()
                if value_text:
                    value = float(value_text)
                    total += value
            result = round(total / 60, 2)

            self.ui.result_label4.setText(str(result))
        except:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректное значение! Повторите ввод ")
            return

    def task_5(self):
        num_text = self.ui.lineEdit_ti_2.text()
        if not num_text.isdigit():
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректный ввод в поле 'ti'")
            return

        num = int(num_text)
        if num < 1 or num > 10:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число должно быть от 1 до 10")
            return

        # Удаляем предыдущие QLineEdit, если они есть
        for i in reversed(range(self.ui.gridLayout_3.count())):
            widget = self.ui.gridLayout_3.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QLineEdit):
                self.ui.gridLayout_3.removeWidget(widget)
                widget.deleteLater()

        self.line_edits = []

        # Создаем новые QLineEdit
        for i in range(num):
            line_edit = QtWidgets.QLineEdit()
            self.ui.gridLayout_3.addWidget(line_edit, i, 0)
            self.line_edits.append(line_edit)

        self.set_cell_style_2()
        self.ui.result_label5.setText("")

    def set_cell_style_2(self):
        style = (
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"
            "border-radius: 5px;"
            "border-color: rgb(255, 255, 255);"
            "border: 1px solid #000000;"
        )
        for i in range(self.ui.gridLayout_3.rowCount()):
            for j in range(self.ui.gridLayout_3.columnCount()):
                widget = self.ui.gridLayout_3.itemAtPosition(i, j)
                if widget is not None:
                    widget.widget().setStyleSheet(style)
                    widget.widget().setAlignment(QtCore.Qt.AlignCenter)

    def calcul_task5(self):
        try:
            total = 0
            # count = 0

            for line_edit in self.line_edits:
                value_text = line_edit.text()
                if value_text:
                    value = float(value_text)
                    total += value
            result = round(total / 60, 2)

            self.ui.result_label5.setText(str(result))
        except:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Некорректное значение! Повторите ввод ")
            return

    def generate_table(self, value):
        try:
            value = int(value)
            self.clear_table()
            self.line_edits = []

            for i in range(value):
                start = i * 5
                end = (i + 1) * 5
                label = QtWidgets.QLabel(f"{start}-{end}")
                line_edit = QtWidgets.QLineEdit()

                self.ui.gridLayout4.addWidget(label, i, 0)
                self.ui.gridLayout4.addWidget(line_edit, i, 1)

                self.line_edits.append(line_edit)
        except:
            return

    def clear_table(self):
        while self.ui.gridLayout4.count():
            item = self.ui.gridLayout4.takeAt(0)
            widget = item.widget()
            widget.setParent(None)
            widget.deleteLater()

    def task_6(self):
        try:
            total = 0
            count = 0
            k = 0

            for line_edit in self.line_edits:
                value_text = line_edit.text()
                if value_text:
                    value = float(value_text)
                    total += ((k * 5 + 2.5) * value)
                    k += 1
                    count += value

            if count > 0:
                result = total / count
                self.ui.result_label6.setText(str(result))
            else:
                self.ui.result_label6.setText("")
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Обнаружены недопустимые символы")
            return

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec())

create_app()