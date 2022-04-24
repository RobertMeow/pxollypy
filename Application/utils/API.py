import requests
import time


class ErrorVK(Exception):
    def __init__(self, code, error):
        self.code = code
        self.error = error


class Captcha(Exception):
    def __init__(self, img):
        self.img = img


class API:
    __slots__ = ['session', 'v', 'token', 'data', 'owner_id', 'kwargs', 'url_api']

    def __init__(self, token, v="5.161", proxies=None):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'API'})
        if proxies is not None:
            self.session.proxies.update(proxies)
        self.v = v
        self.token = token
        self.data = {'access_token': self.token, "v": self.v, }

        self.kwargs = ()
        self.url_api = "https://api.vk.com/method/{}"

        self.owner_id = self.method('users.get')[0]['id']

    def method(self, name, p=None):
        result = self.http(method=False, url=self.url_api.format(name), data=(self.data if p is None else {**self.data, **p})).json()
        if 'error' in result:
            if result['error']['error_code'] == 14:
                raise Captcha(result['error']['captcha_img'])
            else:
                if result['error']['error_code'] == 6:
                    time.sleep(0.4)
                raise ErrorVK(result['error']['error_code'], result['error']['error_msg'])
        else:
            return result['response']

    def http(self, method=True, **kwargs):
        self.kwargs = kwargs
        try:
            if method:
                return self.session.get(**kwargs)
            return self.session.post(**kwargs)
        except requests.exceptions.RequestException as ex:
            print('Error request:', ex)

    def get_peer_id(self, text, cmi, date, from_id):
        response = self.method("messages.search", {"q": text, "count": 5})
        for t in response['items']:
            if t['from_id'] == from_id and t['conversation_message_id'] == cmi and t['date'] == date and t['text'] == text:
                return t['peer_id']
