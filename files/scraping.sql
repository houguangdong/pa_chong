# Host: 10.117.171.135  (Version 5.7.16)
# Date: 2016-12-19 10:51:23
# Generator: MySQL-Front 5.4  (Build 4.53) - http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "pages"
#

DROP TABLE IF EXISTS `pages`;
CREATE TABLE `pages` (
  `id` bigint(7) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `content` varchar(10000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
