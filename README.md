# database-class-design
1.	登陆及注册
1.1	注册
-	密保问题*3
-	密码采取双重MD5+SALT加密(伪）
1.2	登陆
1.3	忘记密码
- 通过注册时填写的三个密保问题完成找回
1.4	验证码
- 基于Django-simple-captcha实现验证码的动态生成、替换

2.	信息分权限展示
2.1	增加(管理员vip用户)
- 通过url字符串拼接的方式实现
2.2	删除
-	允许管理员vip用户进行信息的删除
-	允许使用复选框进行多个同时删除
2.3	查看
- 基于Bootstrap表盘(panel)实现
2.4	修改(管理员vip用户)
- 采用Bootstrap3+jquery+x-editable实现页面内点击修改，并自动更新对应该分数段的绩点成绩。

3.	管理
3.1	信息管理
- 能够修改用户信息
3.2	权限管理
- 修改用户权限，完成普通用户及管理员vip用户的切换
