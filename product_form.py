from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from database import Database
from product_window import Ui_ProductWindow


class ProductCard(QFrame):
    # Карточка товара

    def __init__(self, product_data):
        super().__init__()
        self.product = product_data
        self.setup_ui()

    def setup_ui(self):
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(1)
        self.setMinimumHeight(200)

        main_layout = QHBoxLayout(self)

        # Фото товара
        self.photo_label = QLabel()
        self.photo_label.setFixedSize(100, 100)
        photo_path = f'images/{self.product['image']}' if self.product['image'] else "images/picture.png"
        pixmap = QPixmap(photo_path)
        self.photo_label.setPixmap(pixmap.scaled(90, 90, Qt.KeepAspectRatio))

        main_layout.addWidget(self.photo_label)

        # Информация о товаре
        info_layout = QVBoxLayout()

        price = float(self.product['price'])
        discount = float(self.product['current_discount'])

        # Категория и название
        title_label = QLabel(f"{self.product['category']} | {self.product['product_name']}")
        # title_label.setFont(QFont(pointSize=12, weight=QFont.Bold))
        info_layout.addWidget(title_label)

        # Описание
        description = self.product['description']
        if len(description) > 50:
            description = description[:50] + '...'
        info_layout.addWidget(QLabel(f"Производитель: {self.product['manufacturer']}"))
        info_layout.addWidget(QLabel(f"Поставщик: {self.product['supplier']}"))

        # Цена со скидкой или без
        if discount > 0:
            old_price_label = QLabel(f'{price:.2f} Р.')
            old_price_label.setStyleSheet('text-decoration: line-through; color: red;')
            info_layout.addWidget(old_price_label)

            new_price = price * (1 - discount / 100)
            new_price_label = QLabel(f"{new_price:.2f} Р.")
            # new_price_label.setFont(QFont(pointSize=11, weight=QFont.Bold))
            info_layout.addWidget(new_price_label)
        else:
            price_label = QLabel(f'{price:.2f} Р.')
            # price_label.setFont(QFont(pointSize=11))
            info_layout.addWidget(price_label)

        # Единица измерения и количество
        info_layout.addWidget(
            QLabel(f'Единица измерения: {self.product['unit']} В наличии: {self.product['stock_quantity']} шт.')
        )

        info_layout.addStretch()
        main_layout.addLayout(info_layout)

        # Блок скидки справа
        discount_frame = QFrame()
        discount_frame.setFixedSize(120, 100)
        discount_frame.setFrameShape(QFrame.Box)
        discount_frame.setLineWidth(1)

        discount_layout = QVBoxLayout(discount_frame)
        discount_layout.setAlignment(Qt.AlignCenter)
        
        discount_title = QLabel("Действующая\nскидка")
        # discount_title.setFont(QFont(pointSize=9, weight=QFont.Bold))
        discount_title.setAlignment(Qt.AlignCenter)
        discount_layout.addWidget(discount_title)

        discount_value = QLabel(f'{discount}%')
        # discount_value.setFont(QFont(pointSize=14, weight=QFont.Bold))
        discount_value.setAlignment(Qt.AlignCenter)
        discount_layout.addWidget(discount_value)

        main_layout.addWidget(discount_frame)

        if discount > 15:
            self.setStyleSheet('background-color: #2E8B57;')
        elif int(self.product['stock_quantity']) <= 0:
            self.setStyleSheet("background-color: #ADD8E6")


class ProductForm(QMainWindow, Ui_ProductWindow):
    # Универсальная форма для всех ролей

    def __init__(self, user, login_window=None):
        super().__init__()
        self.setupUi(self)

        # Создаем контейнер товаров
        self.products_layout = QVBoxLayout(self.products_container)
        self.products_container.setLayout(self.products_layout)

        self.user = user
        self.role = user['role']
        self.user_name = user['full_name']
        self.login_window = login_window
        self.database = Database()

        # Настройка заголовка
        titles = {
            'Гость': "Просмотр товаров (Гость)",
            "Авторизированный клиент": "Просмотр товаров (Клиент)",
            "Менеджер": "Управление товарами (Менеджер)",
            "Администратор": "Администрирование (Администратор)"
        }
        self.setWindowTitle(f'{titles.get(self.role)} - ООО Обувь')

        self.user_label.setText(self.user_name)

        self.orders_button.setVisible(self.role in ['Менеджер', 'Администратор'])
        self.add_button.setVisible(self.role == 'Администратор')

        self.search_label.setVisible(self.role in ['Менеджер', 'Администратор'])
        self.search_edit.setVisible(self.role in ['Менеджер', 'Администратор'])
        self.sort_label.setVisible(self.role in ['Менеджер', 'Администратор'])
        self.sort_combo.setVisible(self.role in ['Менеджер', 'Администратор'])

        self.logout_button.clicked.connect(self.on_logout)
        self.orders_button.clicked.connect(self.on_orders)
        self.add_button.clicked.connect(self.on_add)

        self.load_products()

    def load_products(self):
        # Загрузка товаров из базы данных
        # try:
        with self.database.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tovar ORDER BY product_name") 
            products = cursor.fetchall()

        # Очищаем контейнер
        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Добавляем карточки товаров
        for product in products:
            print(product)
            card = ProductCard(product)
            self.products_layout.addWidget(card)
        
        # except Exception as e:
        #     print(e)
    
    def on_logout(self):
        # Выход из аккаунта
        self.close()
        if self.login_window:
            self.login_window.show()
        
    def on_orders(self):
        pass

    def on_add(self):
        pass

