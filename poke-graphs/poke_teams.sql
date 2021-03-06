-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: pokemon_teams
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dancers`
--

DROP TABLE IF EXISTS `dancers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dancers` (
  `id` bigint(20) DEFAULT NULL,
  `pokemon` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dancers`
--

LOCK TABLES `dancers` WRITE;
/*!40000 ALTER TABLE `dancers` DISABLE KEYS */;
INSERT INTO `dancers` VALUES (1,'talonflame'),(2,'aurorus'),(3,'reshiram'),(4,'arctozolt'),(5,'palkia'),(6,'guzzlord');
/*!40000 ALTER TABLE `dancers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team1`
--

DROP TABLE IF EXISTS `team1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team1` (
  `id` bigint(20) DEFAULT NULL,
  `pokemon` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team1`
--

LOCK TABLES `team1` WRITE;
/*!40000 ALTER TABLE `team1` DISABLE KEYS */;
INSERT INTO `team1` VALUES (1,'charizard'),(2,'aurorus'),(3,'amaura'),(4,'carkol'),(5,'rotom-heat'),(6,'walrein');
/*!40000 ALTER TABLE `team1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-08 21:05:51
