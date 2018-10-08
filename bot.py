# coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import requests
import json
import os

global auto_reply, rebort_apply, apikey

# When recieve the following msg types, trigger the auto replying.


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isMpChat=True)
def text_reply(msg):
    global auto_reply, rebort_apply, apikey

    # The command signal of "[自动回复]"
    if msg['FromUserName'] == myUserName and msg['Content'] == u"开启自动回复":
        auto_reply = True
        itchat.send_msg(u"[自动回复]已经打开。\n", msg['FromUserName'])
    elif msg['FromUserName'] == myUserName and msg['Content'] == u"关闭自动回复":
        auto_reply = False
        itchat.send_msg(u"[自动回复]已经关闭。\n", msg['FromUserName'])
    elif msg['FromUserName'] == myUserName and msg['Content'] == u"开启图灵机器人":
        rebort_apply = True
        itchat.send_msg(u"[图灵机器人]已经打开。\n", msg['FromUserName'])
        print('[图灵机器人]已经打开。')
    elif msg['FromUserName'] == myUserName and msg['Content'] == u"关闭图灵机器人":
        rebort_apply = False
        itchat.send_msg(u"[图灵机器人]已经关闭。\n", msg['FromUserName'])
    else:
        if auto_reply == True:
            itchat.send_msg(u"[自动回复]您好，我现在有事不在，一会再和您联系。\n",
                            msg['FromUserName'])
        else:
            # Sleep 1 second is not necessary. Just cheat human.
            time.sleep(1)
            if rebort_apply == True:
                cont = requests.get(
                    'http://www.tuling123.com/openapi/api?key=%s&info=%s' % (apikey, msg['Content'])).content
                m = json.loads(cont)
                itchat.send(m['text'], msg['FromUserName'])
                if m['code'] == 200000:
                    itchat.send(m['url'], msg['FromUserName'])
                if m['code'] == 302000:
                    itchat.send(m['list'], msg['FromUserName'])
                if m['code'] == 308000:
                    itchat.send(m['list'], msg['FromUserName'])
    return


# Main
if __name__ == '__main__':
    global auto_reply, rebort_apply, apikey

    # get your apikey from http://www.tuling123.com and set to the enviroment variable TULING_API_KEY
    apikey = os.environ['TULING_API_KEY']

    if apikey == "":
        print("please provide TULING_API_KEY enviroment variable")
        os._exit(1)

    # Set the hot login
    itchat.auto_login(hotReload=True)

    # Get your own UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print(myUserName)
    auto_reply = False
    rebort_apply = True

    itchat.run()
