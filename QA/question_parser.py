
class QuestionPaser:
    #涉及实体链接部分
    def entity_link(entity):
        pass


    def paser(self,res_classify):
        entities = res_classify["entities"]
        query_type = res_classify["query_type"]
        sql_ = {}
        sql_['query_type'] = query_type

        
        
        if(query_type == "是什么"):
            sql = ["MATCH (m:Concept) where m.name = '{0}' return m.name, m.definition".format(entity.strip()) for entity in entities ]        
        sql_["sql"] = sql   

        return sql_

