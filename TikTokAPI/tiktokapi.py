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

    def send_get_request(self, url, params):
        url = build_get_url(url, params)
        signature = self.tiktok_browser.fetch_auth_params(url, language=self.language)
        url = build_get_url(url, {self.signature_key: signature}, append=True)
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

    def getUserVideos(self, user_id, secUid, count=30):
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
