import os
import random
import urllib.parse
from .utils import random_key, build_get_url, get_req_json, get_req_content, get_req_text
from .tiktok_browser import TikTokBrowser


class TikTokAPI(object):

    def __init__(self, language='en', browser_lang="en-US", timezone="Asia/Kolkata", region='IN', cookie=None):
        self.base_url = "https://t.tiktok.com/api"
        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"

        self.headers = {
            "User-Agent": self.user_agent,
        }
        self.language = language
        self.browser_lang = browser_lang
        self.timezone = timezone
        self.region = region

        if cookie is None:
            self.verifyFp = random_key(16)
        else:
            self.verifyFp = cookie
        self.default_params = {
            "aid": "1988",
            "app_name": "tiktok_web",
            "device_platform": "web",
            "referer": "",
            "user_agent": urllib.parse.quote_plus(self.user_agent),
            "cookie_enabled": "true",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": self.browser_lang,
            "browser_platform": "Linux+x86_64",
            "browser_name": "Mozilla",
            "browser_version": "5.0+(X11)",
            "browser_online": "true",
            "timezone_name": self.timezone,
            # "page_referer": "https://www.tiktok.com/foryou?lang=en",
            "priority_region": self.region,

            "appId": "1180",
            "region": self.region,
            "appType": "t",

            "isAndroid": "false",
            "isMobile": "false",
            "isIOS": "false",
            "OS": "linux",
            "tt-web-region": self.region,

            "language": self.language,
            "verifyFp": self.verifyFp
        }
        self.signature_key = "_signature"
        self.did_key = "did"
        self.tiktok_browser = TikTokBrowser(self.user_agent)

    def send_get_request(self, url, params, extra_headers=None):
        url = build_get_url(url, params)
        did = str(random.randint(10000, 999999999))
        url = build_get_url(url, {self.did_key: did}, append=True)
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
            "type": "5",
            "secUid": "",
            "maxCursor": "0",
            "minCursor": "0",
            "sourceType": "12",
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

    def downloadVideoById(self, video_id, save_path):
        video_info = self.getVideoById(video_id)
        video_url = video_info["itemInfo"]["itemStruct"]["video"]["downloadAddr"]
        headers = {"User-Agent": "okhttp"}
        video_data = get_req_content(video_url, params=None, headers=headers)
        with open(save_path, 'wb') as f:
            f.write(video_data)

    def downloadVideoByIdNoWatermark(self, video_id, save_path):
        video_info = self.getVideoById(video_id)
        video_url = video_info["itemInfo"]["itemStruct"]["video"]["downloadAddr"]
        headers = {"User-Agent": "okhttp"}
        video_data = get_req_text(video_url, params=None, headers=headers)
        pos = video_data.find("vid:")
        video_url_no_wm = "https://api2-16-h2.musical.ly/aweme/v1/play/?video_id={" \
                          "}&vr_type=0&is_play_url=1&source=PackSourceEnum_PUBLISH&media_type=4" \
            .format(video_data[pos+4:pos+36])
        headers = {"User-Agent": "okhttp"}
        video_data_no_wm = get_req_content(video_url_no_wm, params=None, headers=headers)
        with open(save_path, 'wb') as f:
            f.write(video_data_no_wm)
