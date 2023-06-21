# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
import os 
import requests
import random
import json
from hashlib import md5
import re

'''
    翻译类：提供api接口的访问，以及翻译结果的返回。
'''
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
        try:
            r = requests.post(self.url, params=payload, headers=headers)
            result = r.json()['trans_result'][0]['dst']
            # Show response
            return result
        except Exception as e:
            print(e)
        
            


def trasns_process(trans,path):
    basename = os.path.basename(path)
    print("processing chapter: {}".format(os.path.basename))
    with open(path,'r',encoding='utf-8') as f:
        chapter = f.readlines()
    for line in chapter:
        line = line.replace("-------------------------------------------- 分页分隔 --------------------------------------------\n",'')
        if line == ' ' or line =='\n'or line.find("reset page") != -1:
            continue
        result_line = trans.translate(line)
        write_path = os.path.join(r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/translate',basename)
        if not os.path.exists(write_path):
            os.mknod(write_path)
        else:
            with open(write_path,'a',encoding='utf-8') as af:
                        if result_line != None:
                            print(result_line)
                            af.write(result_line)
    split(write_path)


def split(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    pattern = r'([。？！])'
    result = re.split(pattern, text)
    text_list =  ["".join(result[i:i+2]) for i in range(0, len(result), 2)]
    with open(path, "w", encoding="utf-8") as f:
        for sentence in text_list:
            f.write(sentence.strip() + "\n")




if __name__ == "__main__":
    # query = "this is a test" #这是我们需要放入章节
    trans = Translate()
    chapter_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/chapter'
    files = os.listdir(chapter_path)
    for file in files:
        trasns_process(trans,os.path.join(chapter_path,file))
   
