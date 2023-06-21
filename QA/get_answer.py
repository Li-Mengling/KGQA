from py2neo import Graph

class AnswerSearcher:
    def __init__(self): 
        self.g = Graph("http://localhost:7474/", auth=("neo4j", "lml2000326"),name = "neo4j")
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''
    def search_main(self, sql_):
        question_type = sql_['query_type']
        queries = sql_['sql']
        answers = []
       
        for query in queries:
            ress = self.g.run(query).data()
            print(ress)
            answers += ress
           
        
        return answers

