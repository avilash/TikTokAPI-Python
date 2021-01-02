import argparse
from TikTokAPI import TikTokAPI
from utils import read_json_from_file


def getVideoById(video_id):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    return api.getVideoById(video_id)


def downloadVideoById(video_id):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    api.downloadVideoById(video_id, video_id+".mp4")


def downloadVideoByIdNoWatermark(video_id):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    api.downloadVideoByIdNoWatermark(video_id, video_id+"_no_wm.mp4")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data', dest='data', type=str, help='data/video/video_no_wm')
    args = parser.parse_args()

    var = "6843481669886954757"
    if args.data == 'data':
        retval = getVideoById(var)
        print(retval)
    elif args.data == 'video':
        downloadVideoById(var)
    elif args.data == 'video_no_wm':
        downloadVideoByIdNoWatermark(var)
    else:
        print("Invalid Argument")
