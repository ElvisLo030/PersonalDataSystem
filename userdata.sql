-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-04-23 03:53:23
-- 伺服器版本： 10.4.27-MariaDB
-- PHP 版本： 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `middb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `user_data`
--
-- 建立時間： 2024-04-23 01:26:59
-- 最後更新： 2024-04-23 01:52:56
--

CREATE TABLE `user_data` (
  `name` varchar(50) NOT NULL,
  `student_id` char(8) NOT NULL,
  `birthdate` date NOT NULL,
  `birth_time` time NOT NULL,
  `city` varchar(50) NOT NULL,
  `town` varchar(50) NOT NULL,
  `goal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `user_data`
--

INSERT INTO `user_data` (`name`, `student_id`, `birthdate`, `birth_time`, `city`, `town`, `goal`) VALUES
('SimbaWu', '41111197', '1999-10-31', '06:20:00', '15', '鳳山區', 'Greate life too!'),
('jeanWu', '41111198', '1963-05-25', '06:20:00', '15', '鳳山區', 'Greate life!');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `user_data`
--
ALTER TABLE `user_data`
  ADD PRIMARY KEY (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
