-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2023 at 09:10 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `b_id` int(255) NOT NULL,
  `bname` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `quantity` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`b_id`, `bname`, `author`, `quantity`) VALUES
(1, 'Encyclopedia', 'William', 2),
(2, 'Hamlet', 'William Shakespeare', 3),
(3, 'Juliusceaser', 'William shakespeare', 3),
(4, 'Brothers', 'Alex', 0);

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `is_id` int(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `bname` varchar(255) NOT NULL,
  `is_date` date NOT NULL,
  `ex_date` date NOT NULL,
  `re_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`is_id`, `uname`, `bname`, `is_date`, `ex_date`, `re_date`) VALUES
(1, 'prem', 'Hamlet', '2023-07-15', '2023-07-24', '0000-00-00'),
(2, 'praveen', 'Encyclopedia', '2023-07-04', '2023-07-16', '2023-07-14'),
(3, 'praveen', 'Hamlet', '2023-06-08', '2023-06-20', '2023-06-20'),
(4, 'hari', 'Brothers', '2023-07-15', '2023-07-20', '2023-07-17');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `t_id` int(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `bname` varchar(255) NOT NULL,
  `due` int(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`t_id`, `uname`, `bname`, `due`, `status`) VALUES
(1, 'praveen', 'Hamlet', 200, 'paid'),
(2, 'prem', 'Hamlet', 200, 'not paid'),
(3, 'praveen', 'Encyclopedia', 100, 'not paid'),
(4, 'hari', 'Brothers', 100, 'paid'),
(5, 'ragul', 'Brothers', 200, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `u_id` int(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `email` varchar(252) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `uname`, `email`, `password`) VALUES
(1, 'prem', 'premnath123@gmail.com', 'priya'),
(2, 'praveen', 'praveenpopz@gmail.com', '2028'),
(3, 'hari', 'krishnan@gmail.com', 'hari13'),
(6, 'ragul', 'raguls123@gmail.com', 'ragul9764'),
(7, 'naveen', 'naveen@gamil.com', '2721'),
(8, 'gowsik', 'gowsik12@gmail.com', 'gowsik00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`b_id`,`bname`);

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`is_id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`t_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`u_id`,`uname`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `b_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `is_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `t_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `u_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
