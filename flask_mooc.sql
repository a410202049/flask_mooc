/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50636
Source Host           : localhost:3306
Source Database       : flask_mooc

Target Server Type    : MYSQL
Target Server Version : 50636
File Encoding         : 65001

Date: 2017-08-03 16:05:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('5679c0124020');

-- ----------------------------
-- Table structure for `menu_auth`
-- ----------------------------
DROP TABLE IF EXISTS `menu_auth`;
CREATE TABLE `menu_auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `method` varchar(100) DEFAULT NULL,
  `sort` int(11) DEFAULT NULL,
  `icon` varchar(30) DEFAULT NULL,
  `grant` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of menu_auth
-- ----------------------------
INSERT INTO `menu_auth` VALUES ('1', '0', '系统管理', null, '1', 'ti-home', null, null, null);
INSERT INTO `menu_auth` VALUES ('2', '1', '站点设置', 'site-seting', '2', null, 'edit', null, null);
INSERT INTO `menu_auth` VALUES ('3', '1', '权限菜单', 'auth-menu', '3', null, 'add,edit,del', null, null);
INSERT INTO `menu_auth` VALUES ('4', '0', '文章管理', 'article-manage', '4', 'ti-pencil-alt', null, null, null);

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `last_time` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `is_manage` enum('1','0') DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`),
  KEY `group_id` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('2', 'admin', 'admin@qq.com', 'pbkdf2:sha256:50000$PMfRhLAt$4a2ef1c519aa46693ae267d3261b6ea63f244608855baa7b90ab2e663e810f01', '2017-05-18 09:37:44', '2017-05-18 09:37:44', '1', '0', 'kerry', '1', '1', '2017-05-22 13:58:13', '2017-05-22 13:58:15');
INSERT INTO `users` VALUES ('3', 'kerry', '1509699669@qq.com', 'pbkdf2:sha256:50000$PMfRhLAt$4a2ef1c519aa46693ae267d3261b6ea63f244608855baa7b90ab2e663e810f01', '2017-05-18 09:37:44', '2017-05-18 09:37:44', '1', '0', 'Jane Carter', '1', '1', null, null);
INSERT INTO `users` VALUES ('11', 'annie67', 'louise@tekfly.mil', 'pbkdf2:sha256:50000$2PykiSVR$ca8f790ab467abe2d52cb227c0c2da7af0fd4798ef7c7d028b09f7b0cfc9d3a4', '2017-05-18 09:37:45', '2017-05-18 09:37:45', '1', '0', 'Judy Ford', '2', '1', null, null);

-- ----------------------------
-- Table structure for `users_group`
-- ----------------------------
DROP TABLE IF EXISTS `users_group`;
CREATE TABLE `users_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `rules` text,
  `description` text,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_group
-- ----------------------------
INSERT INTO `users_group` VALUES ('1', 'administrator', '1', '', 'administration', '2017-05-19 15:23:56', '2017-05-19 15:25:55');
INSERT INTO `users_group` VALUES ('2', 'manage', '1', '[ { \"id\": \"1\", \"methods\": [ \"add\", \"edit\", \"del\" ] } ]', 'manage', '2017-05-22 13:57:27', '2017-05-22 13:57:29');
