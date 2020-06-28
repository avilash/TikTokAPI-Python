from TikTokAPI import TikTokAPI


video_id = "6843481669886954757"
api = TikTokAPI()
video_obj = api.getVideoById(video_id)
print(video_obj)
