# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5
class Translate():
    def __init__(self):
        
        # Set your own appid/appkey.
        self.appid = '20230223001572757'
        self.appkey = '8RFjakpwSTpICGVMqLoO'
        # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
        self.from_lang = 'en'
        self.to_lang =  'zh'
        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        self.url = endpoint + path


# Generate salt and sign
    def make_md5(self,s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self,query="please set the query"):
        salt = random.randint(32768, 65536)
        sign = self.make_md5(self.appid + query + str(salt) + self.appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': self.appid, 'q': query, 'from': self.from_lang, 'to': self.to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(self.url, params=payload, headers=headers)
        result = r.json()

        # Show response
        print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    # query = "this is a test" #这是我们需要放入章节
    trans = Translate()
    trans.translate()