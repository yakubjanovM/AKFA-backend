-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июл 02 2023 г., 12:05
-- Версия сервера: 10.4.27-MariaDB
-- Версия PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `akfa`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('7df1e5c2a97a');

-- --------------------------------------------------------

--
-- Структура таблицы `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` varchar(999) DEFAULT NULL,
  `telefon_raqami` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `customers`
--

INSERT INTO `customers` (`id`, `name`, `telefon_raqami`, `user_id`) VALUES
(1, 'Mijoz 1', 906322007, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `kirim`
--

CREATE TABLE `kirim` (
  `id` int(11) NOT NULL,
  `money` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `source_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `maxsulot`
--

CREATE TABLE `maxsulot` (
  `id` int(11) NOT NULL,
  `name` varchar(999) DEFAULT NULL,
  `comment` varchar(999) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `maxsulot_tarkibi`
--

CREATE TABLE `maxsulot_tarkibi` (
  `id` int(11) NOT NULL,
  `name` varchar(999) DEFAULT NULL,
  `nechtaligi` int(11) DEFAULT NULL,
  `comment` varchar(999) DEFAULT NULL,
  `maxsulot_id` int(11) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `olchov_birligi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `nasiya`
--

CREATE TABLE `nasiya` (
  `id` int(11) NOT NULL,
  `money` int(11) DEFAULT NULL,
  `qoldiq` int(11) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `olchov`
--

CREATE TABLE `olchov` (
  `id` int(11) NOT NULL,
  `name` varchar(999) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `olchov`
--

INSERT INTO `olchov` (`id`, `name`) VALUES
(1, 'Olchov 1'),
(2, 'Olchov 2');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `status` varchar(999) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `prices`
--

CREATE TABLE `prices` (
  `id` int(11) NOT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `maxsulot_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `trades`
--

CREATE TABLE `trades` (
  `id` int(11) NOT NULL,
  `maxsulot_id` int(11) DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(999) DEFAULT NULL,
  `username` varchar(999) DEFAULT NULL,
  `password` varchar(999) DEFAULT NULL,
  `telefon_raqami` int(11) DEFAULT NULL,
  `role` varchar(999) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `password_hash` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `telefon_raqami`, `role`, `status`, `password_hash`) VALUES
(3, 'Nodirbek', 'Kanonir', 'Nodirbek444', 998959525, 'admin', 1, ''),
(4, NULL, 'admin', '$2b$12$mXxJzv/9n.WWRaK9MUlIze38virerBuak60QkHochhK2g038tlubW', NULL, NULL, NULL, '');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `kirim`
--
ALTER TABLE `kirim`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `maxsulot`
--
ALTER TABLE `maxsulot`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `maxsulot_tarkibi`
--
ALTER TABLE `maxsulot_tarkibi`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `nasiya`
--
ALTER TABLE `nasiya`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `olchov`
--
ALTER TABLE `olchov`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `prices`
--
ALTER TABLE `prices`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `trades`
--
ALTER TABLE `trades`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `kirim`
--
ALTER TABLE `kirim`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `maxsulot`
--
ALTER TABLE `maxsulot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `maxsulot_tarkibi`
--
ALTER TABLE `maxsulot_tarkibi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `nasiya`
--
ALTER TABLE `nasiya`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `olchov`
--
ALTER TABLE `olchov`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `prices`
--
ALTER TABLE `prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `trades`
--
ALTER TABLE `trades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
