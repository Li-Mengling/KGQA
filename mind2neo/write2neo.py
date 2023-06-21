from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
import json
import os 
import ast
import collections

graph = Graph("http://localhost:7474/", auth=("neo4j", "lml2000326"),name = "neo4j")
graph.delete_all()
# a = Node("Person", name="Alice", sex="female", ID="222")
# b = Node("Person", name="Bob", sex="male", ID="123")
# ab = Relationship(a, "KNOWS", b)
# graph.create(ab)


def create_node(*args):
    node_type, name, enName, definition, features = args
    node = Node(node_type,name=name,enName = enName ,\
                     definition = definition, features = features)
    return node

def create_relation(node1,node2,relation = "belong_to"):
    rel = Relationship(node1, relation, node2)
    graph.create(rel)


def get_reply_imformation(now_data):
    #将title创建实体
    gpt_reply = ast.literal_eval(now_data["reply"].replace("},","}"))
    print(gpt_reply)
    node_type = gpt_reply['node_type']
    name = gpt_reply['name']
    enName = gpt_reply['enName']
    definition = gpt_reply['definition']
    features = gpt_reply['features']

    return node_type,name,enName,definition,features


#先拿出对应的reply，然后再遍历其value拿到list
def get_relation_list(data):
    if isinstance(data, dict):
        node_type,name,enName,definition,features = get_reply_imformation(data)
        node1 = create_node(node_type,name,enName, definition, features)
        graph.merge(node1,node_type,"name")
        #创建头实体
        for key, value in data.items():
            if isinstance(value,list):
            #拿到尾实体，并创建尾实体
                for item in value:
                    tNode_type,tName,tEnName,tDefinition,tFeatures = get_reply_imformation(item)
                    node2 = create_node(tNode_type,tName, tEnName , tDefinition, tFeatures)
                    graph.merge(node2,tNode_type,"name")
                    create_relation(node1,node2)
                #创建三元组
                get_relation_list(value)
    #如果是list列表则加载所有的name
    elif isinstance(data, list):

        for item in data:
            get_relation_list(item)



if __name__ == "__main__":
    file_dir = r"C:\Users\Leemonlin\Desktop\repository\QA1\mind2neo\data"
    files = os.listdir(file_dir)
    for file_name in files:
        path = file_dir + "/" + file_name
        with open(path, "r", encoding="utf-8") as f:
            raw_json = json.load(f)
            get_relation_list(raw_json)
            