import argparse
from TikTokAPI import TikTokAPI


def getUser(user_name):
    api = TikTokAPI()
    return api.getUserByName(user_name)


def getVideosByUserName(user_name):
    api = TikTokAPI()
    return api.getVideosByUserName(user_name, count=1)


def getLikesByUserName(user_name):
    api = TikTokAPI()
    return api.getLikesByUserName(user_name, count=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data', dest='data', type=str, help='user/videos/likes')
    args = parser.parse_args()

    var = "fcbarcelona"
    if args.data == 'user':
        retval = getUser(var)
        print(retval)
    elif args.data == 'videos':
        retval = getVideosByUserName(var)
        print(retval)
    elif args.data == 'likes':
        retval = getLikesByUserName(var)
        print(retval)
    else:
        print("Invalid Argument")
