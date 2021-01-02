from TikTokAPI import TikTokAPI
from utils import read_json_from_file

api = TikTokAPI(read_json_from_file("cookie.json"))
retval = api.getTrending(count=5)
print("Trending Videos")
print(retval)
