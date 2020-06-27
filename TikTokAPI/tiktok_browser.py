import os
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from .utils import python_list2_web_list


class TikTokBrowser:

    def __init__(self, user_agent):
        self.userAgent = user_agent
        self.args = [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-infobars",
            "--window-position=0,0",
            "--ignore-certifcate-errors",
            "--ignore-certifcate-errors-spki-list",
            "--user-agent=" + self.userAgent,
        ]
        self.options = {
            'args': self.args,
            'headless': True,
            'ignoreHTTPSErrors': True,
            'userDataDir': "./tmp",
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False
        }

        self.api_list = [
            "/api/user/detail",
            "/api/user/list/",
            "/api/music/detail",
            "/api/item/detail",
            "/api/challenge/detail/",
            "/share/item/list",
            "/api/item_list/",
            "/api/comment/list/",
            "/api/comment/list/reply/",
            "/api/discover/*",
            "/api/commit/follow/user/",
            "/api/recommend/user/",
            "/api/impression/write/",
            "/share/item/explore/list",
            "/api/commit/item/digg/",
            "/node/share/*",
            "/discover/render/*"
        ]

        parent_folder = os.path.dirname(__file__)
        self.tiktok_dummy_page = "file://" + os.path.join(parent_folder, "website", "tiktok.html")

    def fetch_auth_params(self, url, language='en'):
        return asyncio.get_event_loop().run_until_complete(self.async_fetch_auth_params(url, language))

    async def async_fetch_auth_params(self, url, language):
        browser = await launch(self.options)
        page = await browser.newPage()

        await stealth(page)

        await page.setUserAgent(self.userAgent)
        await page.setExtraHTTPHeaders({
            'Accept-Language': language
        })

        await page.goto(self.tiktok_dummy_page, {'waitUntil': "load"})

        signature = await page.evaluate('''() => {
                var init_token = window.byted_acrawler.init({
                                    aid: 1988,
                                    dfp: !1,
                                    boe: !1,
                                    intercept: !0,
                                    enablePathList: ''' + python_list2_web_list(self.api_list) + '''
                                });
                var token = window.byted_acrawler.sign({url: "''' + url + '''"});
                return token;
            }''')

        await browser.close()
        return signature
