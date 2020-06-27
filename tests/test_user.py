from TikTokAPI import TikTokAPI

user = "fcbarcelona"
print("Testing For User - {}".format(user))
api = TikTokAPI()
retval = api.getUserByName(user)
print("User Details")
print(retval)
user_obj = retval["userInfo"]["user"]
retval = api.getUserVideos(user_obj["id"], user_obj["secUid"], count=1)
print("User Videos")
print(retval)
