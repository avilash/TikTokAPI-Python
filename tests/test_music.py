import argparse
from TikTokAPI import TikTokAPI


def getMusic(music_id):
    api = TikTokAPI()
    return api.getMusic(music_id)


def getVideosByMusic(music_id):
    api = TikTokAPI()
    return api.getVideosByMusic(music_id, count=10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--data', dest='data', type=str, help='music/videos')
    args = parser.parse_args()

    var = "6704854531001289474"
    if args.data == 'music':
        retval = getMusic(var)
        print(retval)
    elif args.data == 'videos':
        retval = getVideosByMusic(var)
        print(retval)
    else:
        print("Invalid Argument")

