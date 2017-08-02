/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-08-02 14:03:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `chemi_interface_case`
-- ----------------------------
DROP TABLE IF EXISTS `chemi_interface_case`;
CREATE TABLE `chemi_interface_case` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `API_Purpose` char(30) DEFAULT NULL COMMENT '接口描述',
  `Requst_URL` varchar(200) DEFAULT NULL COMMENT '接口请求地址',
  `Request_Method` char(10) DEFAULT NULL COMMENT '请求方法',
  `Request_Data_Type` char(10) DEFAULT NULL COMMENT '请求数据类型',
  `Request_Data` text COMMENT '请求body',
  `Encryption` tinyint(1) DEFAULT NULL COMMENT '是否加密,0加密,1不加密',
  `Check_Point` char(50) DEFAULT NULL COMMENT '检查点',
  `Correlation` char(50) DEFAULT NULL COMMENT '关联',
  `Active` tinyint(1) DEFAULT NULL COMMENT '是否有效,0有效,1无效',
  `Response` text COMMENT '响应回写',
  `Result` char(10) DEFAULT NULL COMMENT '测试结果',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of chemi_interface_case
-- ----------------------------
INSERT INTO `chemi_interface_case` VALUES ('1', '获取720设备最新版本', 'http://host地址/rest/device/getlatestversion.do', 'POST', 'Data', '{\"prodtype\":\"720\"}', '1', 'msg:\"执行成功\"', null, '1', '', null);
INSERT INTO `chemi_interface_case` VALUES ('2', '检测新版本', 'http://host地址/rest/device/setversion.do', 'POST', 'Data', '{\"prodtype\":\"1005\",\"version\":\"31\"}', '1', '{\"code\":200,\"msg\":\"执行成功\",\"isupdate\":1}', null, '0', null, null);
INSERT INTO `chemi_interface_case` VALUES ('3', '获取720_53设备最新版本', 'http://host地址/rest/device/getlatestversion.do', 'POST', 'Data', '{\"prodtype\":\"720_53\"}', '1', 'msg:\"执行成功\"', '', '0', null, null);
INSERT INTO `chemi_interface_case` VALUES ('4', '获取720can设备最新版本', 'http://host地址/rest/device/getlatestversion.do', 'POST', 'Data', '{\"prodtype\":\"720can\"}', '1', '\"code\":200', null, '0', null, null);
INSERT INTO `chemi_interface_case` VALUES ('5', '图片上传', 'http://host地址/weedfs-fileupload/rest/file/fileupload.do', 'POST', 'Data', 'C:/Users/Public/Pictures/Sample Pictures/1447007795_9803.jpg', '1', '\"code\":\"200\",\"msg\":\"执行成功！\"', null, '0', '{\"code\":\"200\",\"cmd\":\"\",\"result\":{\"fid\":\"15,2b1613ebd6bdc6\",\"real_url\":\"http://newfile.che-mi.net/15,2b1613ebd6bdc6\",\"url\":\"http://newfile.che-mi.net/\",\"size\":59109},\"msg\":\"执行成功！\"}', 'pass');

-- ----------------------------
-- Table structure for `fangche_interface_case`
-- ----------------------------
DROP TABLE IF EXISTS `fangche_interface_case`;
CREATE TABLE `fangche_interface_case` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `API_Purpose` char(30) DEFAULT NULL COMMENT '接口描述',
  `Requst_URL` varchar(200) DEFAULT NULL COMMENT '接口请求地址',
  `Request_Method` char(10) DEFAULT NULL COMMENT '请求方法',
  `Request_Data_Type` char(10) DEFAULT NULL COMMENT '请求数据类型',
  `Request_Data` text COMMENT '请求body',
  `Encryption` tinyint(1) DEFAULT NULL COMMENT '是否加密,0加密,1不加密',
  `Check_Point` char(50) DEFAULT NULL COMMENT '检查点',
  `Correlation` char(50) DEFAULT NULL COMMENT '关联',
  `Active` tinyint(1) DEFAULT NULL COMMENT '是否有效,0有效,1无效',
  `Response` text COMMENT '响应回写',
  `Result` char(10) DEFAULT NULL COMMENT '测试结果',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fangche_interface_case
-- ----------------------------
INSERT INTO `fangche_interface_case` VALUES ('1', '房车登录', 'http://host地址/rvcamp/m/user/login/general', 'POST', 'Data', '{\"username\":\"13538152630\",\"password\":\"1234567\"}', '1', '\"success\": true', null, '0', '{\"success\":true,\"data\":{\"id\":\"62b16918a0f24a048dd68b869feded9a\",\"username\":\"13538152630\",\"password\":null,\"nickname\":\"微波快来\",\"avatarUrl\":\"http://newfile.che-mi.net/31,28850465b283d4\",\"verifyCode\":null,\"uuid\":\"91beb6e388754bf9bf876782ba7ac3c2\",\"secret\":\"62fc63a5608a492aa8126141ec911753\"},\"errorCode\":null,\"msg\":null}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('2', '获取直播评论列表', 'http://host地址/panorama-cm720/rest/app/GetLiveComment.do', 'POST', 'Data', '{\"video_id\":1,\"start\":0,\"count\":1}', '1', '\"code\":200', null, '0', '{\"code\":200,\"msg\":\"执行成功\",\"result\":[{\"com_id\":6,\"is_del\":0,\"memo\":\"评论内容\",\"memo_time\":1501492093000,\"user_id\":16,\"video_id\":1}],\"total\":2}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('3', '点赞与打赏', 'http://host地址/panorama-cm720/rest/live/SetVpLike.do', 'POST', 'Data', '{\"uuid\":\"${id}\",\"live_id\":1,\"live_type\":1,}', '1', '\"code\":200', 'id', '0', '{\"code\":200,\"data\":{\"a_count\":10,\"b_count\":10,\"c_count\":10,\"create_time\":1495728000000,\"diamonds_count\":10,\"flower_count\":10,\"gold_count\":10,\"update_time\":1500825600000,\"user_id\":16},\"isLike\":1,\"msg\":\"执行成功\",\"result\":1,\"total\":35}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('4', '获取直播列表__房车直播', 'http://host地址/panorama-cm720/rest/app/GetLiveList.do', 'POST', 'Data', '{\"type\":1,\"content\":\"\",\"start\":0,\"count\":10}\r', '1', '\"msg\":\"执行成功\"', null, '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('5', '直播评论', 'http://host地址/panorama-cm720/rest/app/SetLiveComment.do', 'POST', 'Data', '{\"video_id\":1,\"uuid\":\"${id}\",\"comment\":\"评论内容\"}', '1', '\"msg\":\"执行成功\"', 'id', '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('6', '获取打赏道具数量', 'http://host地址/panorama-cm720/rest/live/GetRewardCount.do', 'POST', 'Data', '{\"uuid\":\"${id}\"}', '1', '\"msg\":\"执行成功\",\"code\":200', 'id', '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('7', '房车登录失败,密码错误', 'http://host地址/rvcamp/m/user/login/general', 'POST', 'Data', '{\"username\":\"13538152630\",\"password\":\"123456\"}', '1', '\"msg\":\"用户名/密码错误\"', null, '0', '{\"success\":false,\"data\":null,\"errorCode\":\"username/password error\",\"msg\":\"用户名/密码错误\"}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('8', '房车登录失败,用户名不存在', 'http://host地址/rvcamp/m/user/login/general', 'POST', 'Data', '{\"username\":\"13538152633\",\"password\":\"123456\"}', '1', '\"msg\":\"用户名/密码错误\"', null, '0', '{\"success\":false,\"data\":null,\"errorCode\":\"username/password error\",\"msg\":\"用户名/密码错误\"}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('9', '获取直播评论列表失败', 'http://host地址/panorama-cm720/rest/app/GetLiveComment.do', 'POST', 'Data', '{\"video_id\":100,\"start\":0,\"count\":1}', '1', '\"code\":302,\"msg\":\"操作失败\"', null, '0', '{\"code\":302,\"msg\":\"操作失败\",\"total\":0}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('10', '获取直播评论列表失败', 'http://host地址/panorama-cm720/rest/app/GetLiveComment.do', 'POST', 'Data', '{\"video_id\":100,\"start\":10,\"count\":1}', '1', '\"code\":302,\"msg\":\"操作失败\"', null, '0', '{\"code\":302,\"msg\":\"操作失败\",\"total\":0}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('11', '点赞与打赏,用户不存在/未登陆', 'http://host地址/panorama-cm720/rest/live/SetVpLike.do', 'POST', 'Data', '{\n\"uuid\":\"62b16918a0f24a048dd68b869feded9c\",\n\"live_id\":1,\n\"live_type\":1,\n}', '1', '\"code\":301,\"msg\":\"用户未登录\"', null, '0', '{\"code\":301,\"data\":[],\"isLike\":1,\"msg\":\"参数不正确\",\"result\":0}', 'pass');
INSERT INTO `fangche_interface_case` VALUES ('12', '点赞与打赏,live_type不正确', 'http://host地址/panorama-cm720/rest/live/SetVpLike.do', 'POST', 'Data', '{\"uuid\":\"${id}\",\"live_id\":1,\"live_type\":12,}', '1', '\"code\":301,\"msg\":\"参数不正确\"', null, '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('13', '获取直播列表__车米直播', 'http://host地址/panorama-cm720/rest/app/GetLiveList.do', 'POST', 'Data', '{\"type\":0,\"content\":\"\",\"start\":0,\"count\":10}\r', '1', '\"code\":200,\"msg\":\"执行成功\"', null, '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('14', '获取直播列表__直播类型错误', 'http://host地址/panorama-cm720/rest/app/GetLiveList.do', 'POST', 'Data', '{\"type\":2,\"content\":\"\",\"start\":0,\"count\":10}\r', '1', '\"code\":200,\"msg\":\"暂无数据\"', null, '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('15', '直播评论_用户不存在', 'http://host地址/panorama-cm720/rest/app/SetLiveComment.do', 'POST', 'Data', '{\"video_id\":1,\"uuid\":\"62b16918a0f24a048dd68b869feded9\",\"comment\":\"评论内容\"}', '1', '\"code\":302,\"msg\":\"请重新登录\"', null, '0', null, null);
INSERT INTO `fangche_interface_case` VALUES ('16', '获取打赏道具数量', 'http://host地址/panorama-cm720/rest/live/GetRewardCount.do', 'POST', 'Data', '{\"uuid\":\"0\"}', '1', '\"msg\":\"用户未登录\"', null, '0', null, null);
