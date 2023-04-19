import random
import string

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                             QSpinBox, QCheckBox, QMessageBox)
from PyQt6.QtCore import Qt

# Создаем главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор паролей")
        self.setGeometry(0, 0, 300, 250)
        self.setMinimumSize(300, 250)
        self.setMaximumSize(300, 250)
        self.setCentralWidget(PasswordGenerator())  # Устанавливаем виджет, создадим его позже.


# Создаем виджет
class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.main_vertical_layout = QVBoxLayout()
        self.setLayout(self.main_vertical_layout)

        # Создаем главный текст
        self.main_label = QLabel('Генератор паролей')
        self.main_vertical_layout.addWidget(self.main_label)
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Создаем панель выбора длины пароля
        self.up_horizontal_layout = QHBoxLayout()
        self.main_vertical_layout.addLayout(self.up_horizontal_layout)
        self.len_label = QLabel('Длина пароля:')
        self.len_spin = QSpinBox()
        self.len_spin.setRange(4, 28)
        self.len_spin.setValue(8)
        self.up_horizontal_layout.addWidget(self.len_label)
        self.up_horizontal_layout.addWidget(self.len_spin)

        # Создаем панель выбора параметров для пароля
        self.letters_checkbox = QCheckBox("Использовать строчные буквы")
        self.letters_checkbox.setChecked(True)
        self.uppercase_checkbox = QCheckBox("Использовать заглавные буквы")
        self.digits_checkbox = QCheckBox("Использовать цифры")
        self.special_chars_checkbox = QCheckBox("Использовать специальные символы")
        self.main_vertical_layout.addWidget(self.letters_checkbox)
        self.main_vertical_layout.addWidget(self.uppercase_checkbox)
        self.main_vertical_layout.addWidget(self.digits_checkbox)
        self.main_vertical_layout.addWidget(self.special_chars_checkbox)
        self.result_label = QLabel('')
        self.main_vertical_layout.addWidget(self.result_label)

        # Создаем панель с двумя горизонтальными кнопками
        self.bottom_layout = QHBoxLayout()
        self.main_vertical_layout.addLayout(self.bottom_layout)
        self.generate_button = QPushButton('Сгенерировать')
        self.copy_button = QPushButton('Скопировать')
        self.copy_button.setEnabled(False)
        self.bottom_layout.addWidget(self.generate_button)
        self.bottom_layout.addWidget(self.copy_button)

        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_password)

    def generate_password(self):
        # Получаем значения настроек
        length = self.len_spin.value()
        use_letters = self.letters_checkbox.isChecked()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_digits = self.digits_checkbox.isChecked()
        use_special_chars = self.special_chars_checkbox.isChecked()

        # Генерируем пароль
        chars = ""
        if use_letters:
            chars += string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_special_chars:
            chars += string.punctuation

        password = "".join(random.choice(chars) for _ in range(length))
        self.result_label.setText(password)
        self.copy_button.setEnabled(True)


    def copy_password(self):
        password = self.result_label.text()
        QApplication.clipboard().setText(password)
        QMessageBox.information(self, "Копирование", "Пароль скопирован в буфер обмена.")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
