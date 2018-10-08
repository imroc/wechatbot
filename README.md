## 微信自动回复(图灵机器人)

#### 用法
1. 在 http://www.tuling123.com 注册创建公众号机器人并获取 apikey
2. 导出 apikey 到环境变量
``` bash
export TULING_API_KEY=xxx
```
3. 如果没有安装依赖先安装依赖
``` bash
pip3 install itchat
pip3 install requests
```
4. 运行机器人
``` bash
python3 bot.py
```
然后会弹出二维码，微信扫一扫登录就启动了。可以用自己的微信给自己发控制命令，支持的命令有：
- 开启图灵机器人(默认开启，用 tuling123.com 的机器人接口回复)
- 关闭图灵机器人
- 开启自动回复(每次都只回复 "[自动回复]您好，我现在有事不在，一会再和您联系。")
- 关闭自动回复
