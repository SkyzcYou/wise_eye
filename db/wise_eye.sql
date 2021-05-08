/*
 Navicat Premium Data Transfer

 Source Server         : LocalMySQL
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : wise_eye

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 08/05/2021 22:26:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for all_info
-- ----------------------------
DROP TABLE IF EXISTS `all_info`;
CREATE TABLE `all_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `indate` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of all_info
-- ----------------------------
INSERT INTO `all_info` VALUES (15, '<img onclick=\"clike_img()\" class=\"table_in_image\" src=\"../static/uploads/1620479517001-tmp7fwnlx06.jpg.jpg\"alt=\"\">', '411381199812167133', '2021-05-08 21:11:57');

SET FOREIGN_KEY_CHECKS = 1;
