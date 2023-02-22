-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2023 at 04:54 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hr`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `employee_name` varchar(50) NOT NULL,
  `employee_surname` varchar(255) NOT NULL,
  `employee_mail` varchar(255) NOT NULL,
  `employee_phone` bigint(20) NOT NULL,
  `employee_address` varchar(255) NOT NULL,
  `employee_salary` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`employee_id`, `employee_name`, `employee_surname`, `employee_mail`, `employee_phone`, `employee_address`, `employee_salary`) VALUES
(124, 'Ελπινίκη', 'Κρούνη', '-', 6944556632, 'Κόδρου 20, Αγία Βαρβάρα', 900.43),
(789, 'Αντώνης', 'Λάκος', '-', 6900043221, 'Αγίου Δημητρίου 9, Άγιος Δημήτριος', 750.59),
(1032, 'Αλέξανδρος', 'Παπαδόπουλος', 'alex.pap@yahoo.gr', 6910322233, 'Αγίου Δημητρίου 9, Κολωνός', 750.59),
(2100, 'Αντώνης', 'Παπαδόπουλος', '-', 6943032121, 'Οσίου Ανδρέα 5, Νέα Ιωνία', 750.59),
(2441, 'Παναγιώτα', 'Παπαδοπούλου', '-', 6938432022, 'Ούλωφ Πάλμε 40, Ζωγράφου', 750.59),
(2933, 'Κώστας', 'Ορνιεράκης', '-', 6980432420, 'Γεωργίου Γεννηματά 96-98, Αγία Βαρβάρα', 750.59),
(3214, 'Αντώνης', 'Γεωργίου', 'tony.g@gmail.com', 6934355532, 'Ποταμού 30, Κορυδαλλός', 900.43),
(3422, 'Κυριακή', 'Τσανάι', '-', 6903215652, 'Γεωργίου Γεννηματά 50, Αγία Βαρβάρα', 750.59),
(4321, 'Κώστας', 'Κούνης', '-', 2103432944, 'Ναυκρατούσας 2, Αθήνα', 750.59),
(4332, 'Αρετή', 'Παπαδοπούλου', 'areti@gmail.com', 6959430221, 'Λεωφ. Αθηνών 150, Χαϊδάρι', 750.59),
(5601, 'Αντώνης', 'Γεωργίου', 'a.tony@yahoo.gr', 6993302221, 'Πλατεία Δημαρχείου 33, Μεταμόρφωση', 1200.65),
(5633, 'Αρετή', 'Κούνη', '-', 2104532821, 'Αγίας Ελεούσης 33, Αγία Βαρβάρα', 900.43),
(7332, 'Κυριακή', 'Παπαδοπούλου', '-', 6922001133, 'Λεωφ. Αθηνών 150, Χαϊδάρι', 750.59),
(7422, 'Αρετή', 'Μανωλίδου', '-', 6902301222, 'Φιλίππου 10, Χαλάνδρι', 750.59),
(7754, 'Αλέξανδρος', 'Κούνης', '-', 2103383322, 'Ούλωφ Πάλμε 10, Ζωγράφου', 750.59),
(8000, 'Κώστας', 'Βασιλειάδης', '-', 2109090221, 'Δαιδάλου 20, Γέρακας', 900.43),
(9534, 'Παναγιώτα', 'Πλεκτή', '', 6932234171, 'Πραξιτέλους 4, Αθήνα', 750.59),
(9876, 'Αντώνης', 'Γεωργίου', 'g.tony@mail.co.uk', 6925069493, 'Δυρραχίου 2, Αθήνα', 1232.56);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD UNIQUE KEY `employee_id` (`employee_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9880;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
