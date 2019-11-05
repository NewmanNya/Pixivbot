import tweepy
import time
import os
import requests

def ReadKey():
    key_list = []
    with open('password.txt','r') as f:
        for line in f:
            # Copy from internet [works]
            key_list.append(line.strip('\n').split(',')[0])

    return key_list

# Init API
def ApiInit():
    key_list = ReadKey()
    auth = tweepy.OAuthHandler(key_list[0], key_list[1])
    auth.set_access_token(key_list[2], key_list[3])
    return tweepy.API(auth)

# Tweet function
def TweetFunction(api, PicPath, Content):
    api.update_with_media(PicPath, Content)
    print("Send "+PicPath)

# Set Mode
def TweetCmd(api,gap):
    for i in range(StartNum,EndNum):

        PicName = str(i)
        Content = "See more cute pics @BotTamako\n Bot collects pics from Pixiv daily"
        TweetFunction(api, PicAddress="./MARKDONE",PicName= PicName, Content=Content)
        time.sleep(gap)

if __name__ == '__main__':
    all = []
    for fpathe, dirs, fs in os.walk("./"):
        for f in fs:
            filename = fpathe+'/'+f
            if filename.endswith(".jpg"):
                all.append(filename)
            if filename.endswith(".png"):
                all.append(filename)
    print (all)

    flag_rebot = 0
    api = ApiInit()
    for i in all:
        try:
            if flag_rebot :
                api = ApiInit()
                flag_rebot = 0
            TweetFunction(api,i,"See more cute pics @BotTamako\nBot collects pics from Pixiv daily")
            os.remove(i)
            print("remove "+ i)
            time.sleep(30 * 2)
        except:
            print(Exception)
            time.sleep(3600 * 2)
            flag_rebot = 1
            print("rebot")
            api = ApiInit()
            api.update_status(status="@Neko__Nya__, HELP ME~")
