青柠疫服‘半自动’打卡  beta1.3
---
基于 Python + selenium。解决青柠疫情每天的繁琐登录打卡，是需要弹出一个窗口（已经在想办法解决了），所以叫做半自动打卡。
暂时凑合用用吧。会想办法进行简化，让其真正成为自动打卡。



---
使用教程：
 - 1.安装 Python 3.6 及以上版本。（怎么安装自行百度）

    

 - 2.requirements.txt 是所需第三方模块，执行 

  ```
  pip install -r requirements.txt
  ```

   安装模块。
  需要安装的 Python 库有：selenium 、 request 库。

  

 - 3.需要下载对应系统的 webdriver 。webdriver 下载地址：http://chromedriver.storage.googleapis.com/index.html
 并存放到本文件夹下。并修改代码中 webdriver 的绝对路径。推荐下载 80 以后的版本

 - 4.修改名字、学号、密码等变量。

 - 5.运行 daka.py 

---

增加页面的验证，跳转更加准确。任然有偶发性跳转失败。
增加验证码识别及填充，准确性有待提高。使用的是百度的文字识别接口。


---
TODO：
打算封装为 EXE 应用。
提升稳定度和验证码识别的准确性


