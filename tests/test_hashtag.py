import argparse
from TikTokAPI import TikTokAPI
from utils import read_json_from_file


def getHashTag(hashTag):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    return api.getHashTag(hashTag)


def getVideosByHashTag(hashTag):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    return api.getVideosByHashTag(hashTag, count=10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data', dest='data', type=str, help='hashtag/videos')
    args = parser.parse_args()

    var = "#fcbarcelona"
    if args.data == 'hashtag':
        retval = getHashTag(var)
        print(retval)
    elif args.data == 'videos':
        retval = getVideosByHashTag(var)
        print(retval)
    else:
        print("Invalid Argument")

