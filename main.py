import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from database import Database
from login_form import Ui_MainWindow
from product_form import ProductForm

class LoginForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.loginButton.clicked.connect(self.on_login)
        self.guestButton.clicked.connect(self.on_guest)
        self.exitButton.clicked.connect(self.close)

    def on_login(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()

        if not login or not password:
            QMessageBox.warning(self, "Предупреждение", "Ввидите логин и пароль")
            return
        
        print(f'Попытка входа: {login} / {password}')

        user = self.db.get_user(login, password)
        if user:
            print(f"Успешный вход: {user['full_name']} ({user['role']})")
            self.open_product_form(user)
        else:
            print(f'Неверный логин или пароль')

    def on_guest(self):
        print('Вход как гость')
        
        guest_user = {
            'id_user': 0,
            'role': "Гость",
            'full_name': 'Гость',
            'login': '',
            'password': ''
        }
        self.open_product_form(guest_user)

    def open_product_form(self, user):
        # Здесь будет открытие универсальной формы для авторизованного пользователя
        self.hide()
        self.product_form = ProductForm(user, login_window=self)
        self.product_form.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())