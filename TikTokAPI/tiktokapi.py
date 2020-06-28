import os
from .utils import random_key, build_get_url, get_req_json
from .tiktok_browser import TikTokBrowser


class TikTokAPI(object):

    def __init__(self, language='en', region='IN', cookie=None):
        self.base_url = "https://t.tiktok.com/api"
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/83.0.4103.106 Safari/537.36"

        self.headers = {
            "User-Agent": self.user_agent
        }
        self.language = language
        self.region = region
        if cookie is None:
            self.verifyFp = random_key(16)
        else:
            self.verifyFp = cookie
        self.default_params = {
            "language": self.language,
            "verifyFp": self.verifyFp
        }
        self.signature_key = "_signature"
        self.tiktok_browser = TikTokBrowser(self.user_agent)

    def send_get_request(self, url, params, extra_headers=None):
        url = build_get_url(url, params)
        signature = self.tiktok_browser.fetch_auth_params(url, language=self.language)
        url = build_get_url(url, {self.signature_key: signature}, append=True)
        if extra_headers is None:
            headers = self.headers
        else:
            headers = {}
            for key, val in extra_headers.items():
                headers[key] = val
            for key, val in self.headers.items():
                headers[key] = val
        data = get_req_json(url, params=None, headers=self.headers)
        return data

    def getTrending(self, count=30):
        url = self.base_url + "/item_list/"
        req_default_params = {
            "id": "1",
            "type": "1",
            "secUid": "",
            "maxCursor": "0",
            "minCursor": "0",
            "sourceType": "12",
            "appId": "1180",
            "region": self.region
        }
        params = {
            "count": str(count)
        }
        for key, val in req_default_params.items():
            params[key] = val
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)

    def getUserByName(self, user_name):
        url = self.base_url + "/user/detail/"
        params = {
            "uniqueId": user_name
        }
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)

    def getVideosByUserName(self, user_name, count=30):
        user_data = self.getUserByName(user_name)
        user_obj = user_data["userInfo"]["user"]
        user_id = user_obj["id"]
        secUid = user_obj["secUid"]

        url = self.base_url + "/item_list/"
        req_default_params = {
            "type": "1",
            "maxCursor": "0",
            "minCursor": "0",
            "sourceType": "8",
            "appId": "1180",
            "region": self.region
        }
        params = {
            "id": user_id,
            "secUid": secUid,
            "count": str(count)
        }
        for key, val in req_default_params.items():
            params[key] = val
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)
    
    def getLikesByUserName(self, user_name, count=30):
        user_data = self.getUserByName(user_name)
        user_obj = user_data["userInfo"]["user"]
        user_id = user_obj["id"]
        secUid = user_obj["secUid"]

        url = self.base_url + "/item_list/"
        req_default_params = {
            "type": "2",
            "maxCursor": "0",
            "minCursor": "0",
            "sourceType": "9",
            "appId": "1180",
            "region": self.region
        }
        params = {
            "id": user_id,
            "secUid": secUid,
            "count": str(count)
        }
        for key, val in req_default_params.items():
            params[key] = val
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)

    def getHashTag(self, hashTag):
        url = self.base_url + "/challenge/detail/"
        params = {
            "challengeName": hashTag.replace("#", "")
        }
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)

    def getVideosByHashTag(self, hashTag, count=30):
        hashTag = hashTag.replace("#", "")
        hashTag_obj = self.getHashTag(hashTag)
        hashTag_id = hashTag_obj["challengeInfo"]["challenge"]["id"]
        url = "https://m.tiktok.com/share/item/list"
        req_default_params = {
            "secUid": "",
            "type": "3",
            "minCursor": "0",
            "maxCursor": "0",
            "shareUid": "",
            "recType": ""
        }
        params = {
            "id": str(hashTag_id),
            "count": str(count),
        }
        for key, val in req_default_params.items():
            params[key] = val
        for key, val in self.default_params.items():
            params[key] = val
        extra_headers = {"Referer": "https://www.tiktok.com/tag/" + str(hashTag)}
        return self.send_get_request(url, params, extra_headers=extra_headers)

    def getMusic(self, music_id):
        url = self.base_url + "/music/detail/"
        params = {
            "musicId": music_id
        }
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)

    def getVideosByMusic(self, music_id, count=30):
        url = "https://m.tiktok.com/share/item/list"
        req_default_params = {
            "secUid": "",
            "type": "4",
            "minCursor": "0",
            "maxCursor": "0",
            "shareUid": "",
            "recType": ""
        }
        params = {
            "id": str(music_id),
            "count": str(count),
        }
        for key, val in req_default_params.items():
            params[key] = val
        for key, val in self.default_params.items():
            params[key] = val
        extra_headers = {"Referer": "https://www.tiktok.com/music/original-sound-" + str(music_id)}
        return self.send_get_request(url, params, extra_headers=extra_headers)

    def getVideoById(self, video_id):
        url = self.base_url + "/item/detail/"
        params = {
            "itemId": str(video_id)
        }
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)
