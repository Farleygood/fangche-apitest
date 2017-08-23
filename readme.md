
### 说明文档
* 测试用例使用mysql管理,本来是打算使用excel的,公司excel只要修改了就加密了
  加密后读excel就报错,极不方便
* sql语句可以直接导入,里面有个字段Active字段在需要跳过某条用例是使用
![alt text](https://github.com/Farleygood/fangche-apitest/raw/master/img/1.png)

* 目前是两个项目,一个是chemi的,一个是fangche的,每个项目下面有多个.py文件,每个.py文件
  都是一个接口,里面每条case都是一条测试用例,测试用例从数据库里读
 > testcase
 >> 项目一
 >>> 接口1  
 >>> 接口2  
 
 >> 项目二
 >>> 接口1  
 >>> 接口2  
* 测试用例跑完后就发送邮件给对应的人,当然也可以集成到jenkins里,构建失败后发送邮件

  
#### 遗留问题
* 1.发布动态的接口(test_uploadfile.py)需要上传文件,从数据库里面读出来用例怎么都不成功,现在还是使用
  原始的方法直接把参数写到脚本里面,后面在想其他的办法
  
