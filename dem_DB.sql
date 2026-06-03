-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Июн 03 2026 г., 13:30
-- Версия сервера: 8.0.46-0ubuntu0.24.04.2
-- Версия PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `dem_DB`
--

-- --------------------------------------------------------

--
-- Структура таблицы `order_items`
--

CREATE TABLE `order_items` (
  `id_items` int NOT NULL,
  `order_number` int NOT NULL,
  `article` varchar(20) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `quantity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Дамп данных таблицы `order_items`
--

INSERT INTO `order_items` (`id_items`, `order_number`, `article`, `quantity`) VALUES
(1, 1, 'А112Т4', 2),
(2, 1, 'F635R4', 2),
(3, 2, 'H782T5', 1),
(4, 2, 'G783F5', 1),
(5, 3, 'J384T6', 10),
(6, 3, 'D572U8', 10),
(7, 4, 'F572H7', 5),
(8, 4, 'D329H3', 4),
(9, 5, 'А112Т4', 2),
(10, 5, 'F635R4', 2),
(11, 6, 'H782T5', 1),
(12, 6, 'G783F5', 1),
(13, 7, 'J384T6', 10),
(14, 7, 'D572U8', 10),
(15, 8, 'F572H7', 5),
(16, 8, 'D329H3', 4),
(17, 9, 'B320R5', 5),
(18, 9, 'G432E4', 1),
(19, 10, 'S213E3', 5),
(20, 10, 'E482R4', 5);

-- --------------------------------------------------------

--
-- Структура таблицы `pickup_points`
--

CREATE TABLE `pickup_points` (
  `id_points` int NOT NULL,
  `adress` text CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Дамп данных таблицы `pickup_points`
--

INSERT INTO `pickup_points` (`id_points`, `adress`) VALUES
(1, '420151, г. Лесной, ул. Вишневая, 32'),
(2, '125061, г. Лесной, ул. Подгорная, 8'),
(3, '630370, г. Лесной, ул. Шоссейная, 24'),
(4, '400562, г. Лесной, ул. Зеленая, 32'),
(5, '614510, г. Лесной, ул. Маяковского, 47'),
(6, '410542, г. Лесной, ул. Светлая, 46'),
(7, '620839, г. Лесной, ул. Цветочная, 8'),
(8, '443890, г. Лесной, ул. Коммунистическая, 1'),
(9, '603379, г. Лесной, ул. Спортивная, 46'),
(10, '603721, г. Лесной, ул. Гоголя, 41'),
(11, '410172, г. Лесной, ул. Северная, 13'),
(12, '614611, г. Лесной, ул. Молодежная, 50'),
(13, '454311, г.Лесной, ул. Новая, 19'),
(14, '660007, г.Лесной, ул. Октябрьская, 19'),
(15, '603036, г. Лесной, ул. Садовая, 4'),
(16, '394060, г.Лесной, ул. Фрунзе, 43'),
(17, '410661, г. Лесной, ул. Школьная, 50'),
(18, '625590, г. Лесной, ул. Коммунистическая, 20'),
(19, '625683, г. Лесной, ул. 8 Марта'),
(20, '450983, г.Лесной, ул. Комсомольская, 26'),
(21, '394782, г. Лесной, ул. Чехова, 3'),
(22, '603002, г. Лесной, ул. Дзержинского, 28'),
(23, '450558, г. Лесной, ул. Набережная, 30'),
(24, '344288, г. Лесной, ул. Чехова, 1'),
(25, '614164, г.Лесной,  ул. Степная, 30'),
(26, '394242, г. Лесной, ул. Коммунистическая, 43'),
(27, '660540, г. Лесной, ул. Солнечная, 25'),
(28, '125837, г. Лесной, ул. Шоссейная, 40'),
(29, '125703, г. Лесной, ул. Партизанская, 49'),
(30, '625283, г. Лесной, ул. Победы, 46'),
(31, '614753, г. Лесной, ул. Полевая, 35'),
(32, '426030, г. Лесной, ул. Маяковского, 44'),
(33, '450375, г. Лесной ул. Клубная, 44'),
(34, '625560, г. Лесной, ул. Некрасова, 12'),
(35, '630201, г. Лесной, ул. Комсомольская, 17'),
(36, '190949, г. Лесной, ул. Мичурина, 26');

-- --------------------------------------------------------

--
-- Структура таблицы `tovar`
--

CREATE TABLE `tovar` (
  `article` varchar(20) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `unit` varchar(20) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `supplier` varchar(255) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `manufacturer` varchar(255) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `category` varchar(100) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `current_discount` decimal(5,2) NOT NULL,
  `stock_quantity` int NOT NULL,
  `description` text CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `image` text CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Дамп данных таблицы `tovar`
--

INSERT INTO `tovar` (`article`, `product_name`, `unit`, `price`, `supplier`, `manufacturer`, `category`, `current_discount`, `stock_quantity`, `description`, `image`) VALUES
('B320R5', 'Туфли', 'шт.', 4300.00, '2', '4', '0', 2.00, 6, 'Туфли Rieker женские демисезонные, размер 41, цвет коричневый', '9.jpg'),
('B431R5', 'Ботинки', 'шт.', 2700.00, '3', '4', '1', 2.00, 5, 'Мужские кожаные ботинки/мужские ботинки', ''),
('C436G5', 'Ботинки', 'шт.', 10200.00, '2', '5', '0', 15.00, 9, 'Ботинки женские, ARGO, размер 40', ''),
('D268G5', 'Туфли', 'шт.', 4399.00, '3', '4', '0', 3.00, 12, 'Туфли Rieker женские демисезонные, размер 36, цвет коричневый', ''),
('D329H3', 'Полуботинки', 'шт.', 1890.00, '3', '5', '0', 4.00, 4, 'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый', '8.jpg'),
('D364R4', 'Туфли', 'шт.', 12400.00, '2', '1', '0', 16.00, 5, 'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши', ''),
('D572U8', 'Кроссовки', 'шт.', 4100.00, '3', '3', '1', 3.00, 6, '129615-4 Кроссовки мужские', '6.jpg'),
('E482R4', 'Полуботинки', 'шт.', 1800.00, '2', '1', '0', 2.00, 14, 'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный', ''),
('F427R5', 'Ботинки', 'шт.', 11800.00, '3', '4', '0', 15.00, 11, 'Ботинки на молнии с декоративной пряжкой FRAU', ''),
('F572H7', 'Туфли', 'шт.', 2700.00, '2', '2', '0', 2.00, 14, 'Туфли Marco Tozzi женские летние, размер 39, цвет черный', '7.jpg'),
('F635R4', 'Ботинки', 'шт.', 3244.00, '3', '2', '0', 2.00, 13, 'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый', '2.jpg'),
('G432E4', 'Туфли', 'шт.', 2800.00, '2', '1', '0', 3.00, 15, 'Туфли kari женские TR-YR-413017, размер 37, цвет: черный', '10.jpg'),
('G531F4', 'Ботинки', 'шт.', 6600.00, '2', '1', '0', 12.00, 9, 'Ботинки женские зимние ROMER арт. 893167-01 Черный', ''),
('G783F5', 'Ботинки', 'шт.', 5900.00, '2', '3', '1', 2.00, 8, 'Мужские ботинки Рос-Обувь кожаные с натуральным мехом', '4.jpg'),
('H535R5', 'Ботинки', 'шт.', 2300.00, '3', '4', '0', 2.00, 7, 'Женские Ботинки демисезонные', ''),
('H782T5', 'Туфли', 'шт.', 4499.00, '2', '1', '1', 4.00, 5, 'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный', '3.jpg'),
('J384T6', 'Ботинки', 'шт.', 3800.00, '3', '4', '1', 2.00, 16, 'B3430/14 Полуботинки мужские Rieker', '5.jpg'),
('J542F5', 'Тапочки', 'шт.', 500.00, '2', '1', '1', 13.00, 0, 'Тапочки мужские Арт.70701-55-67син р.41', ''),
('K345R4', 'Полуботинки', 'шт.', 2100.00, '3', '6', '1', 2.00, 3, '407700/01-02 Полуботинки мужские CROSBY', ''),
('K358H6', 'Тапочки', 'шт.', 599.00, '2', '4', '1', 20.00, 2, 'Тапочки мужские син р.41', ''),
('L754R4', 'Полуботинки', 'шт.', 1700.00, '2', '1', '0', 2.00, 7, 'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный', ''),
('M542T5', 'Кроссовки', 'шт.', 2800.00, '3', '4', '1', 18.00, 3, 'Кроссовки мужские TOFA', ''),
('N457T5', 'Полуботинки', 'шт.', 4600.00, '2', '6', '0', 3.00, 13, 'Полуботинки Ботинки черные зимние, мех', ''),
('O754F4', 'Туфли', 'шт.', 5400.00, '3', '4', '0', 4.00, 18, 'Туфли женские демисезонные Rieker артикул 55073-68/37', ''),
('P764G4', 'Туфли', 'шт.', 6800.00, '2', '6', '0', 15.00, 15, 'Туфли женские, ARGO, размер 38', ''),
('S213E3', 'Полуботинки', 'шт.', 2156.00, '3', '6', '1', 3.00, 6, '407700/01-01 Полуботинки мужские CROSBY', ''),
('S326R5', 'Тапочки', 'шт.', 9900.00, '3', '6', '1', 17.00, 15, 'Мужские кожаные тапочки \"Профиль С.Дали\" ', ''),
('S634B5', 'Кеды', 'шт.', 5500.00, '3', '6', '1', 3.00, 0, 'Кеды Caprice мужские демисезонные, размер 42, цвет черный', ''),
('T324F5', 'Сапоги', 'шт.', 4699.00, '2', '6', '0', 2.00, 5, 'Сапоги замша Цвет: синий', ''),
('А112Т4', 'Ботинки', 'шт.', 4990.00, '2', '1', '0', 3.00, 6, 'Женские Ботинки демисезонные kari', '1.jpg');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id_user` int NOT NULL,
  `role` varchar(50) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `full_name` varchar(100) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `login` varchar(50) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Дамп данных таблицы `user`
--

INSERT INTO `user` (`id_user`, `role`, `full_name`, `login`, `password`) VALUES
(1, 'Администратор', 'Никифорова Весения Николаевна', '94d5ous@gmail.com', 'uzWC67'),
(2, 'Администратор', 'Сазонов Руслан Германович', 'uth4iz@mail.com', '2L6KZG'),
(3, 'Администратор', 'Одинцов Серафим Артёмович', 'yzls62@outlook.com', 'JlFRCZ'),
(4, 'Менеджер', 'Степанов Михаил Артёмович', '1diph5e@tutanota.com', '8ntwUp'),
(5, 'Менеджер', 'Ворсин Петр Евгеньевич', 'tjde7c@yahoo.com', 'YOyhfR'),
(6, 'Менеджер', 'Старикова Елена Павловна', 'wpmrc3do@tutanota.com', 'RSbvHv'),
(7, 'Авторизированный клиент', 'Михайлюк Анна Вячеславовна', '5d4zbu@tutanota.com', 'rwVDh9'),
(8, 'Авторизированный клиент', 'Ситдикова Елена Анатольевна', 'ptec8ym@yahoo.com', 'LdNyos'),
(9, 'Авторизированный клиент', 'Ворсин Петр Евгеньевич', '1qz4kw@mail.com', 'gynQMT'),
(10, 'Авторизированный клиент', 'Старикова Елена Павловна', '4np6se@mail.com', 'AtnDjr');

-- --------------------------------------------------------

--
-- Структура таблицы `zakaz`
--

CREATE TABLE `zakaz` (
  `order_number` int NOT NULL,
  `order_date` date NOT NULL,
  `delivery_date` date NOT NULL,
  `pickup_code` varchar(50) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `order_status` varchar(50) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `id_points` int NOT NULL,
  `id_user` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Дамп данных таблицы `zakaz`
--

INSERT INTO `zakaz` (`order_number`, `order_date`, `delivery_date`, `pickup_code`, `order_status`, `id_points`, `id_user`) VALUES
(1, '2025-02-27', '2025-04-20', '901', 'Завершен', 1, 4),
(2, '2022-09-28', '2025-04-21', '902', 'Завершен', 11, 1),
(3, '2025-03-21', '2025-04-22', '903', 'Завершен', 2, 2),
(4, '2025-02-20', '2025-04-23', '904', 'Завершен', 11, 3),
(5, '2025-03-17', '2025-04-24', '905', 'Завершен', 2, 4),
(6, '2025-03-01', '2025-04-25', '906', 'Завершен', 15, 1),
(7, '2026-02-27', '2025-04-26', '907', 'Завершен', 3, 2),
(8, '2025-03-31', '2025-04-27', '908', 'Новый ', 19, 3),
(9, '2025-04-02', '2025-04-28', '909', 'Новый ', 5, 4),
(10, '2025-04-03', '2025-04-29', '910', 'Новый ', 19, 4);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`id_items`),
  ADD KEY `article` (`article`) USING BTREE,
  ADD KEY `order_number` (`order_number`) USING BTREE;

--
-- Индексы таблицы `pickup_points`
--
ALTER TABLE `pickup_points`
  ADD PRIMARY KEY (`id_points`);

--
-- Индексы таблицы `tovar`
--
ALTER TABLE `tovar`
  ADD PRIMARY KEY (`article`);

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- Индексы таблицы `zakaz`
--
ALTER TABLE `zakaz`
  ADD PRIMARY KEY (`order_number`),
  ADD KEY `id_points` (`id_points`),
  ADD KEY `id_user` (`id_user`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `order_items`
--
ALTER TABLE `order_items`
  MODIFY `id_items` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `pickup_points`
--
ALTER TABLE `pickup_points`
  MODIFY `id_points` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT для таблицы `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `zakaz`
--
ALTER TABLE `zakaz`
  MODIFY `order_number` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `article` FOREIGN KEY (`article`) REFERENCES `tovar` (`article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_number` FOREIGN KEY (`order_number`) REFERENCES `zakaz` (`order_number`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `zakaz`
--
ALTER TABLE `zakaz`
  ADD CONSTRAINT `id_points` FOREIGN KEY (`id_points`) REFERENCES `pickup_points` (`id_points`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
