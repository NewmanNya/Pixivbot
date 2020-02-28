import tweepy
import time
import os
import requests
import random

emoji_list = ['(・∀・)',
              '(≧▽≦)',
              '(•ө•)♡',
              '(*´∀｀)',
              '(ㆁωㆁ*)',
              '(*^^*)',
              '(≧∇≦)b',
              '(^_-)-☆',
              'ʕ•̀ω•́ʔ✧',
              '٩(♡ε♡ )۶',
              '٩(๑´3｀๑)۶',
              '(๑•̀ㅁ•́๑)✧',
              '•̀.̫•́✧',
              '(*˘︶˘*).｡.:*♡',
              '(•ө•)♡',
              '(>ω<)',
              '(´-﹏-`；)',
              '(¯―¯٥)',
              '(°ー°〃)',
              '(；´Д｀)',
              '(´-﹏-`；)',
              '(；一_一)',
              'm(_ _;)m',
              '(@_@)',
              '( ﾟдﾟ)',
              '(゜o゜)',
              '＼(◎o◎)／',
              '(✽ ﾟдﾟ ✽)',
              'ε≡≡ﾍ( ´Д`)ﾉ',
              '(｡ŏ﹏ŏ)',
              '( ･ั﹏･ั)',
              '(つд⊂)ｴｰﾝ',
              '(ﾉД`)ｼｸｼｸ',
              '٩(๑´0`๑)۶',
              '(ToT)/~~~',
              '｡･ﾟ･(ﾉД`)･ﾟ･｡',
              '｡･ﾟ･(ﾉ∀`)･ﾟ･｡',
              '(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)',
              '(︶^︶)',
              '(#･∀･)',
              '(－－〆)',
              '٩(๑`^´๑)۶',
              '٩(๑òωó๑)۶']

def ReadKey():
    key_list = []
    with open('password.txt', 'r') as f:
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
    print("Send " + PicPath)


def Rename():
    new_name = []
    i = 0
    for fpathe, dirs, fs in os.walk("./"):
        for f in fs:
            if f.endswith(".jpg"):
                i = i + 1
                raw_filename = fpathe + '/' + f
                new_filename = fpathe + '/' + str(i) + ".jpg"
                os.rename(raw_filename, new_filename)
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
            if flag_reboot:
                api = ApiInit()
                flag_reboot = 0
            if os.path.getsize(i) > 1000 * 3000:
                os.remove(i)
                continue
            else:
                TweetFunction(
                    api, i, emoji_list[random.randint(0, len(emoji_list)-1)])
            os.remove(i)
            print("remove " + i)
            time.sleep(30 * 2)

        except Exception as e:
            print(repr(e))
            print("ERROR")
            time.sleep(30 * 2)
            flag_reboot = 1
            print("reboot")
            api = ApiInit()
            api.update_status(
                status="@Neko__Nya__, HELP ME~, Error is " + repr(e))

    api.update_status(
        status="@Neko__Nya__, Pic list is empty.\nFill me up with more cute pictures please❤")
