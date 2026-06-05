from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QDialog, QMessageBox, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from database import Database
from product_window import Ui_ProductWindow
from product_dialog import Ui_Dialog


class ProductCard(QFrame):
    # Карточка товара

    def __init__(self, product_data, db=None, is_admin=False, parent_form=None):
        super().__init__()
        self.product = product_data

        self.db = db
        self.is_admin = is_admin
        self.parent_form = parent_form

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

        if self.is_admin:
            buttons_layout = QVBoxLayout()

            update_button = QPushButton()
            update_button.setText('Обновить')
            buttons_layout.addWidget(update_button)

            delete_button = QPushButton()
            delete_button.setText('Удалить')
            buttons_layout.addWidget(delete_button)

            main_layout.addLayout(buttons_layout)

            update_button.clicked.connect(self.edit_product)
            delete_button.clicked.connect(self.delete_product)


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
    
    def edit_product(self):
        # Редактирование товара
        dialog = ProductDialog(product_data=self.product, parent=self.parent_form)

        if dialog.exec_() == QDialog.Accepted:
            new_data = dialog.get_product_data()

            if self.db.update_product(self.product['article'], new_data):
                QMessageBox.information(self, "Успех", "Товар обновлен")
                if self.parent_form:
                    self.parent_form.load_products()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось обновить товар")
    
    def delete_product(self):
        # Удаление товара
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Удалить товар \"{self.product['product_name']}\"",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            article = self.product['article']
            success, msg = self.db.delete_product(article)

            if success:
                QMessageBox.information(self, "Успех", msg)
                if self.parent_form:
                    self.parent_form.load_products()
            else:
                QMessageBox.warning(self, "Ошибка", msg)


class ProductDialog(QDialog):
    # Диалог для добавления/редактирования товара

    def __init__(self, product_data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.product_data = product_data
        self.setWindowTitle("Добавление товара" if product_data is None else "Редактирование товара")

        self.ui.button_box.accepted.connect(self.accept)
        self.ui.button_box.rejected.connect(self.reject)

        if product_data:
            self.load_product_data()
            self.ui.edit_article.setReadOnly(True)
    
    def load_product_data(self):
        # Заполнение полей при редактировании
        self.ui.edit_article.setText(str(self.product_data.get('article', '')))
        self.ui.edit_name.setText(str(self.product_data.get('product_name', '')))
        self.ui.edit_category.setText(str(self.product_data.get('category', '')))
        self.ui.edit_manufacturer.setText(str(self.product_data.get('manufacturer', '')))
        self.ui.edit_supplier.setText(str(self.product_data.get('supplier', '')))
        self.ui.spin_price.setValue(int(self.product_data.get('price', 0)))
        self.ui.spin_discount.setValue(int(self.product_data.get('current_discount', 0)))
        self.ui.spin_quantity.setValue(int(self.product_data.get('stock_quantity', 0)))
        self.ui.edit_unit.setText(str(self.product_data.get('unit', '')))
        self.ui.edit_description.setText(str(self.product_data.get('description', '')))
        self.ui.edit_image.setText(str(self.product_data.get('image', '')))
    
    def get_product_data(self):
        # Возвращает словарь с данными товара
        return {
            'article': self.ui.edit_article.text().strip(),
            'product_name': self.ui.edit_name.text().strip(),
            'category': self.ui.edit_category.text().strip(),
            'manufacturer': self.ui.edit_manufacturer.text().strip(),
            'supplier': self.ui.edit_supplier.text().strip(),
            'price': self.ui.spin_price.text().strip(),
            'current_discount': self.ui.spin_discount.text().strip(),
            'stock_quantity': self.ui.spin_quantity.text().strip(),
            'unit': self.ui.edit_unit.text().strip(),
            'description': self.ui.edit_description.text().strip(),
            'image': self.ui.edit_image.text().strip(),
    }

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
        self.filter_label.setVisible(self.role in ['Менеджер', 'Администратор'])
        self.supplier_combo.setVisible(self.role in ['Менеджер', 'Администратор'])

        self.logout_button.clicked.connect(self.on_logout)
        self.orders_button.clicked.connect(self.on_orders)
        self.add_button.clicked.connect(self.on_add)

        if self.role in ['Менеджер', 'Администратор']:
            self.sort_combo.clear()
            self.sort_combo.addItem("Без сортировки", None)
            self.sort_combo.addItem("Цена (возрастание)", 'price_asc')
            self.sort_combo.addItem("Цена (убывание)", 'price_desc')
            self.sort_combo.addItem("Количество (возрастание)", 'quantity_asc')
            self.sort_combo.addItem("Количество (убывание)", 'quantity_desc')
            self.sort_combo.currentIndexChanged.connect(self.on_sort_changed)
            self.search_edit.textChanged.connect(self.on_search_changed)

            # Загружаем список поставщиков
            suppliers = self.database.get_suppliers_list()
            self.supplier_combo.clear()
            self.supplier_combo.addItem("Все поставщики", None)
            for supplier in suppliers:
                self.supplier_combo.addItem(supplier, supplier)
            self.supplier_combo.currentIndexChanged.connect(self.on_filter_changed)



        self.load_products()

    def load_products(self):
        # Загрузка товаров из базы данных
        # try:
        products = self.database.get_products()

        # Очищаем контейнер
        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Добавляем карточки товаров
        # for product in products:
        #     card = ProductCard(product)
        #     self.products_layout.addWidget(card)
        is_admin = (self.role == 'Администратор')
        for product in products:
            card = ProductCard(
                product,
                is_admin=is_admin,
                db=self.database if is_admin else None,
                parent_form=self
            )
            self.products_layout.addWidget(card)
        
        # except Exception as e:
        #     print(e)

    def on_sort_changed(self, index):
        sort_type = self.sort_combo.currentData()

        products = self.database.get_products(sort_type)

        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        is_admin = (self.role == 'Администратор')
        for product in products:
            card = ProductCard(
                product,
                is_admin=is_admin,
                db=self.database if is_admin else None,
                parent_form=self
            )
            self.products_layout.addWidget(card)
    
    def on_search_changed(self, text):
        # Поиск при изменении текста с учетом фильтра
        supplier_name = self.supplier_combo.currentData() if hasattr(self, 'supplier_combo') else None

        if supplier_name:
            products = self.database.get_products_by_supplier(supplier_name)
            if text and text.strip():
                filtered = []
                for product in products:
                    if text.strip().lower() in product['product_name'].lower():
                        filtered.append(product)
                products = filtered
        else:
            if not text or text.strip() == "":
                products = self.database.get_products()
            else: 
                products = self.database.get_products_search(text.strip())
        
        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        is_admin = (self.role == 'Администратор')
        for product in products:
            card = ProductCard(
                product,
                is_admin=is_admin,
                db=self.database if is_admin else None,
                parent_form=self
            )
            self.products_layout.addWidget(card)

    def on_filter_changed(self):
        # Фильтрация при изменении поставщика
        supplier_name = self.supplier_combo.currentData()
        # search_text = self.search_edit.text().strip() if self.search_edit.text() else None

        if supplier_name:
            products = self.database.get_products_by_supplier(supplier_name)
        else:
            products = self.database.get_products()

        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater

        # for product in products:
        #     card = ProductCard(product)
        #     self.products_layout.addWidget(card)
        is_admin = (self.role == 'Администратор')
        for product in products:
            card = ProductCard(
                product,
                is_admin=is_admin,
                db=self.database if is_admin else None,
                parent_form=self
            )
            self.products_layout.addWidget(card)
    
    def on_logout(self):
        # Выход из аккаунта
        self.close()
        if self.login_window:
            self.login_window.show()
        
    def on_orders(self):
        pass

    def on_add(self):
        # Добавление нового товара
        dialog = ProductDialog(parent=self)

        if dialog.exec_() == QDialog.Accepted:
            product_data = dialog.get_product_data()

            if not product_data['article']:
                QMessageBox.warning(self, "Ошибка", "Артикул обязателен!")
                return

            if not product_data['product_name']:
                QMessageBox.warning(self, "Ошибка", "Название товара обязательно!")
                return

            existing = self.database.get_products()
            for p in existing:
                if p['article'] == product_data['article']:
                    QMessageBox.warning(self, "Ошибка", "Товар с таким артикулом уже существует!")
                    return

            if self.database.add_product(product_data):
                QMessageBox.information(self, "Успех", f"Товар '{product_data['product_name']}' добавлен!")
                self.load_products()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось добавить товар")
    
    


