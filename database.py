import pymysql

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        # Подключение к БД
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='demoDB',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            self.connect = None

    # 
    # Users methods
    # 
    def get_user(self, login, password):
        # Проверка пользователя при входе
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT id_user, role, full_name FROM user WHERE login=%s AND password=%s"
                cursor.execute(sql, (login, password))
                result = cursor.fetchone()

                return result
        except Exception as e:
            return None
    
    # 
    # Products methods
    # 
    def get_products(self, sort_type=''):
        # Получение всех товаров
        if not self.is_connected():
            return []
        
        order_by = 'product_name ASC'

        if sort_type == 'price_asc':
            order_by = "price ASC"
        elif sort_type == 'price_desc':
            order_by = "price DESC"
        elif sort_type == 'quantity_asc':
            order_by = "stock_quantity ASC"
        elif sort_type == 'quantity_desc':
            order_by = 'stock_quantity DESC'

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""
                    SELECT 
                        article, product_name, unit, price, supplier,
                        manufacturer, category, current_discount,
                        stock_quantity, description, image
                    FROM tovar
                    ORDER BY {order_by}       
                """)
                return cursor.fetchall()
        except Exception as e:
            print(e)
            return []
    
    def get_products_search(self, search_text):
        # Поиск товаров по названию
        if not self.is_connected():
            return []
        
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT
                        article, product_name, unit, price, supplier,
                        manufacturer, category, current_discount,
                        stock_quantity, description, image
                    FROM tovar
                    WHERE product_name LIKE %s
                    ORDER BY product_name
                """
                cursor.execute(sql, (f'%{search_text}%'))
                return cursor.fetchall()
        except Exception as e:
            print(f'Ошибка get_products_search: {e}')
            return []
        
    def get_products_by_supplier(self, supplier_name):
        # Получение товаров по поставщику
        if not self.is_connected():
            return []

        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT 
                        article, product_name, unit, price, supplier,
                        manufacturer, category, current_discount,
                        stock_quantity, description, image
                    FROM tovar
                    WHERE supplier = %s
                    ORDER BY product_name
                """

                cursor.execute(sql, (supplier_name,))
                return cursor.fetchall()
        except Exception as e:
            print(f'Ошибка get_products_by_supplier {e}')
            return []
    
    # 
    # Добавление/Редактирование/Удаление продутоа
    # 
    def add_product(self, product_data):
        # Добавление товара
        if not self.is_connected():
            return False
        
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    INSERT INTO tovar
                    (article, product_name, category, manufacturer, supplier, price, current_discount, stock_quantity, unit, description, image)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                cursor.execute(sql, (
                    product_data.get('article'),
                    product_data.get('product_name'),
                    product_data.get('category'),
                    product_data.get('manufacturer'),
                    product_data.get('supplier'),
                    product_data.get('price'),
                    product_data.get('current_discount'),
                    product_data.get('stock_quantity'),
                    product_data.get('unit'),
                    product_data.get('description'),
                    product_data.get('image'),
                ))
                self.connection.commit()
                return True
        except Exception as e:
            print(f'Ошибка add_product: {e}')
            return False
    
    def update_product(self, article, product_data):
        # Обновление товара
        if not self.is_connected():
            return False

        try:
            with self.connection.cursor() as cursor:
                sql = """
                    UPDATE tovar
                    SET product_name=%s, category=%s, manufacturer=%s, supplier=%s, price=%s, current_discount=%s, stock_quantity=%s, unit=%s, description=%s, image=%s
                    WHERE article=%s
                """
                cursor.execute(sql, (
                    product_data.get('product_name'),
                    product_data.get('category'),
                    product_data.get('manufacturer'),
                    product_data.get('supplier'),
                    product_data.get('price'),
                    product_data.get('current_discount'),
                    product_data.get('stock_quantity'),
                    product_data.get('unit'),
                    product_data.get('description'),
                    product_data.get('image'),
                    article
                ))
                self.connection.commit()
                return True
        except Exception as e:
            print(f'Ошибка update_product: {e}')
            return False
    
    def delete_product(self, article):
        # Удаление товара с проверкой наличия в заказах
        if not self.is_connected():
            return False, "Нет подключения к БД"
        
        try:
            with self.connection.cursor() as cursor:
                # Проверка наличия в заказах
                cursor.execute(
                    "SELECT * FROM order_items WHERE article=%s",
                    (article,)
                )
                result = cursor.fetchall()
                if result:
                    return False, f'Товар "{article}" присутствует в заказах! Удаление невозможно'
                
                cursor.execute('DELETE FROM tovar WHERE article = %s', (article,))
                self.connection.commit()
                return True, f'Товар "{article}" удален'
        except Exception as e:
            print(f'Ошибка в delete_product {e}')
        
    # 
    # Supplier methods
    # 
    def get_suppliers_list(self):
        # Получение списка всех поставщиков
        if not self.is_connected():
            return []

        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT DISTINCT supplier
                    FROM tovar
                    WHERE supplier IS NOT NULL AND supplier != ''
                    ORDER BY supplier
                """
                cursor.execute(sql)
                results = cursor.fetchall()
                return [row['supplier'] for row in results]
        except Exception as e:
            print(f'Ошибка get_suppliers_list: {e}')
            return []

    
    def is_connected(self):
        # Проверка подключения
        return self.connection is not None
    
    def close(self):
        # Закрытие соединения
        if self.connection:
            self.connection.close()
            self.connection = None