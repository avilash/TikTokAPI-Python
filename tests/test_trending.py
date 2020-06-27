from TikTokAPI import TikTokAPI

api = TikTokAPI()
retval = api.getTrending(count=5)
print("Trending Videos")
print(retval)
