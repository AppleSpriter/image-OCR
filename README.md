# image-OCR

今天在下载表情包的时候，因为是以数字按顺序命名的，突然奇想用表情包里面的文字命名，所以利用百度云、腾讯云的文字识别api开发了这两个小应用

## 使用方法

imageOCR 是用的[百度云](https://cloud.baidu.com/)里面的OCR功能，注册申请一个账号，每日有50000张免费标准/500张免费高精度可用
imageOCR_tencent 是用的[腾讯云](https://cloud.tencent.com/)，同上

使用时通过申请下来的用，将百度里面修改为自己的

```
APP_ID = '11111111'
API_KEY = 'xxxxxx'
SECRET_KEY = 'xxxxxx'
```

腾讯云同理，修改以下部分为自己的id, key

```
cred = credential.Credential("xxxxx", "xxxxx") 
```

## 图片添加

图片放到同文件夹下的image文件夹中即可

## 注意事项

- 第一次使用时没经验，百度的文档也没有写每秒并发，没有加上sleep延时机制，导致识别到100多张图片的时候被服务器认为是DDOS攻击，封了两个小时左右才好。

- 加入了文件名正则化机制，只保留汉字数字英文字符（否则会有无法保存的情况
- 同文件名会根据原始文件名称加入成为后缀，防止重名

## 测试情况

测试了500张表情包，识别准确率还挺高的，由于是动漫人物有时候会多出来一些字符（比如嘴识别成O、V），一些很小的字符也可以识别出来，小修了一下就没什么了
