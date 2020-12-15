-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: wavehoteldb
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `categoryguests`
--

LOCK TABLES `categoryguests` WRITE;
/*!40000 ALTER TABLE `categoryguests` DISABLE KEYS */;
INSERT INTO `categoryguests` VALUES ('KND','NOIDIA',1,'Khách Nội Địa Không Phụ Thu'),('KNN','NUOCNGOAI',1.5,'Khách Nước Ngoài Nhân Hệ Số 1.5');
/*!40000 ALTER TABLE `categoryguests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `categoryrooms`
--

LOCK TABLES `categoryrooms` WRITE;
/*!40000 ALTER TABLE `categoryrooms` DISABLE KEYS */;
INSERT INTO `categoryrooms` VALUES ('CC','Phòng Cao Cấp',170000,3,'Phòng Cao Cấp có diện tích từ 37 m² tới 43 m² được thiết kế với hướng nhìn ra vườn Thượng Uyển hoặc cận cảnh hồ bơi. Phòng có 1 giường đôi hoặc 2 giường đơn, được trang trí bởi nội thất cổ điển sang trọng và nghệ thuật trang trí vô cùng tinh tế đến từng chi tiết.'),('TC','Phòng Tiêu Chuẩn',150000,3,'Phòng Tiêu Chuẩn có diện tích 40 m² tới 47 m², được thiết kế với hướng nhìn ra biển. Phòng có 1 giường đôi được trang trí với những đồ nội thất cổ điển sang trọng với nghệ thuật trang trí vô cùng tinh tế đến từng chi tiết.'),('VIP','Phòng VIP',200000,3,'Phòng VIP là loại phòng đặc biệt của khách sạn WAVEL với diện tích từ 105 m² phù hợp cho khách gia đình. Một phòng được trang bị 1 giường ngủ King size và 2 giường ngủ đơn. Đây là loại phòng được thiết kế với hướng nhìn ra biển xanh rộng lớn ngay trong tầm mắt của du khách. Phòng có không gian bếp thoáng đãng, tủ lạnh, bàn khách và sofa.Ngoài ra có đầy đủ TV LCD 32 in, Wifi...Phòng được trang trí với nội thất cổ điển sang trọng và nghệ thuật trang trí vô cùng tinh tế đến từng chi tiết.');
/*!40000 ALTER TABLE `categoryrooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `change_the_rules`
--

LOCK TABLES `change_the_rules` WRITE;
/*!40000 ALTER TABLE `change_the_rules` DISABLE KEYS */;
INSERT INTO `change_the_rules` VALUES (1,'Số khách tối đa/ phòng','3',1),(2,'Phụ thu khách thứ 3','25%',1),(3,'Hệ số khách nước ngoài','1.5',1),(4,'Hệ số khách nội địa','1.0',1),(5,'Giá phòng VIP/ đêm','200000',1),(6,'Giá phòng CC/ đêm','170000',1),(7,'Giá phòng TC / đêm','150000',1);
/*!40000 ALTER TABLE `change_the_rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `roomdetails`
--

LOCK TABLES `roomdetails` WRITE;
/*!40000 ALTER TABLE `roomdetails` DISABLE KEYS */;
INSERT INTO `roomdetails` VALUES ('1','Nguyen Van A','243546457','3246345','2020-12-01','2020-12-08',3,0,'P11',1,'KND');
/*!40000 ALTER TABLE `roomdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES ('P11','Deluxe King','PHONGCOKHACH','images/room_1.jpg','CC'),('P12','Deluxe Triple','PHONGTRONG','images/room_2.jpg','CC'),('P13','Grand Deluxe Family','PHONGTRONG','images/room_3.jpg','CC'),('P14','Deluxe Twin','PHONGTRONG','images/room_4.jpg','CC'),('P21','Deluxe Twin Sea View','PHONGTRONG','images/room_5.jpg','CC'),('P22','Grand Deluxe King Sea View','PHONGTRONG','images/room_6.jpg','CC'),('P23','Luxury King','PHONGTRONG','images/room_8.jpg','CC'),('P24','Luxury Triple','PHONGTRONG','images/room_9.jpg','CC'),('P31','Luxury Twin','PHONGTRONG','images/room_10.jpg','CC'),('P32','Luxury Deluxe ','PHONGTRONG','images/tc1.jpg','TC'),('P33','Luxury Family','PHONGTRONG','images/tc4.jpg','TC'),('P34','Two Bedrooms Suite Sea View','PHONGTRONG','images/tc3.jpg','TC'),('P41','Deluxe King Sea View Room','PHONGTRONG','images/vip1.jpg','VIP'),('P42','VIP King Sew View ','PHONGTRONG','images/vip2.jpg','VIP'),('P43','VIP King Of Queen','PHONGTRONG','images/vip3.jpg','VIP'),('P44','VIP Luxury ','PHONGTRONG','images/tc3.jpg','VIP');
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `surcharge`
--

LOCK TABLES `surcharge` WRITE;
/*!40000 ALTER TABLE `surcharge` DISABLE KEYS */;
INSERT INTO `surcharge` VALUES (1,0,1);
/*!40000 ALTER TABLE `surcharge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `usernhanvien`
--

LOCK TABLES `usernhanvien` WRITE;
/*!40000 ALTER TABLE `usernhanvien` DISABLE KEYS */;
INSERT INTO `usernhanvien` VALUES (1,'admin','e10adc3949ba59abbe56e057f20f883e','ADMIN','Pham Thi Hong An','Quan Ly','0345605625','2015-12-12','Nu'),(3,'Nam','81dc9bdb52d04dc20036dbd8313ed055','USER','Nguyen Van Nam','Le Tan','034568678','2020-12-08','Nam');
/*!40000 ALTER TABLE `usernhanvien` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-15 23:49:43
