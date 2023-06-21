import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  

openai.api_key = "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"
messages = [{"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"}]


ORDER = "你是程序，你只需要返回问句中函数的json格式即可，下面是问句："


class Chat():
    def __init__(self) -> None:
        pass
      
    
    # @retry(wait=wait_random_exponential(min=10, max=60), stop=stop_after_attempt(10))
    def chat_davinc(self,messages):
        response = openai.Completion.create(\
            engine='text-davinci-003',
            prompt=messages,
            temperature=0.2,
            max_tokens=2000,
            top_p=1
        )
        res_msg = response['choices'][0]['text'].strip()
        print(res_msg)
        return res_msg
    
    @retry(wait=wait_random_exponential(min=10, max=60), stop=stop_after_attempt(10))
    def chat_gpt3(self,args):
        messages.append({"role": "user", "content": args}) 
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature=0.7
        )
        res_msg = completion.choices[0].message
        return res_msg
    
    def chat_function(self,query): 
        messages.append({"role": "user", "content": ORDER}) 
        messages.append({"role": "user", "content": query}) 
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo-0613",
            messages = messages,
            temperature=0.1,
            functions = [
                        {
                            "name": "get_entity",
                            "description": "返回该问句中的计算机科学实体",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "entities": {
                                        "type": "string",
                                        "description": "计算机学科知识图谱中的实体. For example, 操作系统,\
                                            The query should be returned in plain text, not in JSON",
                                    },
                                    "query_type":{
                                        "type":"string",
                                        "description":"返回该问句的类型。For example, 是什么 ，怎么 ，什么时候"
                                    }
                                },
                                "required": ["entities","query_type"],
                            },
                        }
                    ],
            function_call="auto",
            )
        res_msg = completion.choices[0].message
        print(res_msg)
        return res_msg


    @classmethod
    def desk(self,args):
        messages.append({"role": "user", "content": args}) 
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature=0.7
        )
        res_msg = completion.choices[0].message
        print(res_msg["content"].strip())