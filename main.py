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

def Rename():
    new_name = []
    i  = 0
    for fpathe, dirs, fs in os.walk("./"):
        for f in fs:
            if f.endswith(".jpg"):
                i = i + 1
                raw_filename = fpathe + '/' + f
                new_filename = fpathe + '/' + str(i) +".jpg"
                os.rename(raw_filename,new_filename)
                new_name.append(new_filename)

            if f.endswith(".png"):
                i = i + 1
                raw_filename = fpathe + '/' + f
                new_filename = fpathe + '/' + str(i) + ".png"
                os.rename(raw_filename, new_filename)
                new_name.append(new_filename)
    return new_name

def get_pic_list():
    all = []
    for fpathe, dirs, fs in os.walk("./"):
        for f in fs:
            filename = fpathe + '/' + f
            if filename.endswith(".jpg"):
                all.append(filename)
            if filename.endswith(".png"):
                all.append(filename)
    print(all)
    return all

if __name__ == '__main__':
    try:
        print(Rename())
    except Exception as e:
        repr(e)

    pic_list = get_pic_list()

    flag_reboot = 0
    api = ApiInit()
    for i in pic_list:
        try:
            if flag_reboot :
                api = ApiInit()
                flag_reboot = 0
            TweetFunction(api,i,"See more cute pics @BotTamako\nBot collects pics from Pixiv daily")
            os.remove(i)
            print("remove "+ i)
            time.sleep(30 * 2)

        except Exception as e:
            repr(e)
            print("ERROR")
            time.sleep(30 * 2)
            flag_reboot = 1
            print("reboot")
            api = ApiInit()
            api.update_status(status="@Neko__Nya__, HELP ME~")
