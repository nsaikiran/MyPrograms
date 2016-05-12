-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: MovieTicket
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `firstshow`
--

DROP TABLE IF EXISTS `firstshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `firstshow` (
  `theatre` varchar(20) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `firstshow`
--

LOCK TABLES `firstshow` WRITE;
/*!40000 ALTER TABLE `firstshow` DISABLE KEYS */;
INSERT INTO `firstshow` VALUES ('apsara',15),('apsara',14),('apsara',20),('apsara',21),('satya',5),('satya',11),('satya',15),('satya',2),('tirumala',7),('tirumala',14),('tirumala',16),('tirumala',11),('tirumala',24),('dwaraka',5),('dwaraka',6),('dwaraka',17),('dwaraka',18),('Santhosh',1),('Santhosh',2),('CHARAN',1),('CHARAN',15),('Santhosh',16),('Santhosh',15),('Santhosh',14),('Shakuntala',32),('Shakuntala',33),('Shakuntala',34),('dwaraka',9),('dwaraka',10),('dwaraka',13),('dwaraka',14),('dwaraka',1),('dwaraka',19),('satya',20),('satya',22),('satya',21);
/*!40000 ALTER TABLE `firstshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matineeshow`
--

DROP TABLE IF EXISTS `matineeshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matineeshow` (
  `theatre` varchar(20) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matineeshow`
--

LOCK TABLES `matineeshow` WRITE;
/*!40000 ALTER TABLE `matineeshow` DISABLE KEYS */;
INSERT INTO `matineeshow` VALUES ('tirumala',17),('tirumala',16),('tirumala',21),('tirumala',22),('tirumala',2),('tirumala',8),('tirumala',24),('tirumala',30),('satya',5),('satya',10),('satya',12),('satya',19),('satya',20),('Santhosh',6),('Santhosh',7),('Santhosh',15),('Santhosh',14),('CHARAN',15),('CHARAN',16),('CHARAN',19),('CHARAN',26),('Santhosh',1),('Santhosh',2),('Santhosh',3),('Shakuntala',32),('Shakuntala',33),('Shakuntala',34),('Shakuntala',35),('minisatya',3),('minisatya',4),('minisatya',20),('minisatya',21),('minisatya',22),('tirumala',25),('tirumala',26),('tirumala',27),('tirumala',28);
/*!40000 ALTER TABLE `matineeshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `morningshow`
--

DROP TABLE IF EXISTS `morningshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `morningshow` (
  `theatre` varchar(20) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `morningshow`
--

LOCK TABLES `morningshow` WRITE;
/*!40000 ALTER TABLE `morningshow` DISABLE KEYS */;
INSERT INTO `morningshow` VALUES ('satya',9),('satya',8),('satya',14),('satya',21),('minisatya',4),('minisatya',10),('minisatya',16),('minisatya',15),('CHARAN',4),('CHARAN',10),('CHARAN',10),('CHARAN',11),('CHARAN',12),('CHARAN',23),('CHARAN',18),('CHARAN',25),('CHARAN',31),('Santhosh',15),('Santhosh',14),('dwaraka',10),('dwaraka',5),('dwaraka',2),('dwaraka',3),('dwaraka',12),('dwaraka',18),('dwaraka',17),('dwaraka',13),('dwaraka',20),('tirumala',26),('tirumala',13),('tirumala',15),('Shakuntala',26),('Shakuntala',27),('Shakuntala',28),('Shakuntala',29);
/*!40000 ALTER TABLE `morningshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `theatre` varchar(20) DEFAULT NULL,
  `movie` varchar(20) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('dwaraka','Kumari 21F',75),('tirumala','Kumari 21F',75),('satya','Kanche',50),('apsara','Akhil',150),('minisatya','ChiikatiRajyam',150),('Santhosh','SizeZero',75),('CHARAN','BAHUBALI',150),('Shakuntala','Vikramasimha',75),('Vinayaka','bahubali 3',75),('Annapurna','Naannaku Premato',150);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `secondshow`
--

DROP TABLE IF EXISTS `secondshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `secondshow` (
  `theatre` varchar(20) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `secondshow`
--

LOCK TABLES `secondshow` WRITE;
/*!40000 ALTER TABLE `secondshow` DISABLE KEYS */;
INSERT INTO `secondshow` VALUES ('dwaraka',7),('dwaraka',10),('dwaraka',14),('tirumala',15),('tirumala',14),('tirumala',20),('tirumala',29),('tirumala',24),('tirumala',4),('tirumala',7),('minisatya',2),('minisatya',7),('minisatya',15),('minisatya',15),('minisatya',13),('minisatya',14),('minisatya',8),('minisatya',1),('CHARAN',28),('CHARAN',14),('CHARAN',6),('CHARAN',31),('CHARAN',36),('CHARAN',1),('CHARAN',10),('CHARAN',13),('CHARAN',19),('Shakuntala',14),('Shakuntala',15),('Shakuntala',16),('Shakuntala',17),('Santhosh',10),('Santhosh',11),('Shakuntala',33),('Shakuntala',34),('satya',14),('satya',15),('satya',16),('satya',18),('satya',17);
/*!40000 ALTER TABLE `secondshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theatre`
--

DROP TABLE IF EXISTS `theatre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `theatre` (
  `name` varchar(20) DEFAULT NULL,
  `phno` varchar(10) NOT NULL DEFAULT '',
  `passwd` varchar(10) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `rows` int(11) DEFAULT NULL,
  `cols` int(11) DEFAULT NULL,
  PRIMARY KEY (`phno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theatre`
--

LOCK TABLES `theatre` WRITE;
/*!40000 ALTER TABLE `theatre` DISABLE KEYS */;
INSERT INTO `theatre` VALUES ('dwaraka','1234567890','dwaraka','Nuzvid',5,4),('tirumala','1847385904','tirumala','Nuzvid',5,6),('minisatya','2738948609','minisatya','Vijayawada',4,6),('CHARAN','6666669999','NAME','Nuzvid',6,6),('apsara','8690382648','apsara','Vijayawada',4,6),('Santhosh','8985619211','dnjpm','Vijayawada',4,4),('satya','9583086916','satya','Nuzvid',4,6),('Vinayaka','9652077939','1234','Vijayawada',4,4),('Shakuntala','9874563210','123456789','Vijayawada',6,6),('Annapurna','9876545123','annapurna','Vijayawada',5,6);
/*!40000 ALTER TABLE `theatre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `user` char(20) DEFAULT NULL,
  `id` char(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES ('saikiran','TueNov2419:49:50IST2015'),('NEELIMA','TueNov2420:05:37IST2015'),('NEELIMA','TueNov2421:16:11IST2015'),('NEELIMA','TueNov2421:23:46IST2015'),('saikiran','TueNov2421:27:44IST2015'),('saikiran','WedNov2502:18:05IST2015'),('NARESH','ThuNov2603:46:32IST2015'),('saikiran','ThuNov2603:48:47IST2015');
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `phno` varchar(10) NOT NULL DEFAULT '',
  `name` varchar(20) DEFAULT NULL,
  `passwd` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`phno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1234567890','tester','tester'),('1334567890','tester2','tester'),('3245798025','shankar','shankar'),('8763128909','NARESH','naresh'),('8985259795','Prasanth','prasanthv'),('8985610211','tester3','dnjpm'),('9000160177','Abhinav','123456789'),('9491165338','saikiran','sai'),('9494174396','sai','sai'),('9505841421','abhi','abhi'),('9515162567','Abhinav','iiluvbooks'),('9603232094','iiit','6hw3m'),('9652077939','NEELIMA','1234'),('9842762183','raj','raj'),('9966199017','ram','ram'),('9999996666','VARUN','SAME'),('9999999999','hello','hello');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-27 17:26:32
