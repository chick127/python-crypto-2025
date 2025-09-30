import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('간단한 계산기')

        main_layout = QVBoxLayout()

        equation_layout = QHBoxLayout()
        self.equation_label = QLabel('수식 입력:')
        self.equation_input = QLineEdit()
        self.equation_input.setPlaceholderText('예: 10 + 5')

        equation_layout.addWidget(self.equation_label)
        equation_layout.addWidget(self.equation_input)

        result_layout = QHBoxLayout()
        self.result_label_title = QLabel('계산 결과:')
        self.result_label = QLabel('')
        self.result_label.setStyleSheet("font-size: 16px; font-weight: bold; color: blue;")
        self.result_label.setAlignment(Qt.AlignLeft)

        result_layout.addWidget(self.result_label_title)
        result_layout.addWidget(self.result_label)
        result_layout.addStretch()

        main_layout.addLayout(equation_layout)
        main_layout.addLayout(result_layout)

        self.setLayout(main_layout)

        self.equation_input.returnPressed.connect(self.calculate)

    def calculate(self):
        try:
            equation = self.equation_input.text()
            if not equation.strip():
                self.result_label.setText('오류: 수식을 입력하세요.')
                return

            result = eval(equation) 
            self.result_label.setText(f'{equation} = {result}')

        except (SyntaxError, NameError, ZeroDivisionError) as e:
            self.result_label.setText(f'오류: {e}')
        except Exception as e:
            self.result_label.setText(f'알 수 없는 오류: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
