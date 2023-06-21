import Chat
import ast




class Classifier():
    def __init__(self) -> None:
        print("开始分类")

    def classify(self,question):
        chat = Chat.Chat()
        res_msg = chat.chat_function(question)
        function_args = ast.literal_eval(res_msg['function_call']['arguments'])
        entities = function_args['entities'].split(",")
        query_type = function_args['query_type']


        print(entities, query_type)

        
        return {"entities":entities, "query_type":query_type}
        

