# register_login
用户登录和注册并且与mysql数据库进行交互的小程序
1 mysqlhelper模块用来简化数据库和python交互的代码
2 需要在mysql中创建db5数据库
以及如下的表格
create table user(
	username varchar(20),
	passwd char(40)
	)charset=utf8;
3 使用到了hashlib中的sha1加密方式

