import json 
from collections import defaultdict


def processing_data(json_text,name):
    pair_dict  = defaultdict(dict)
    
    for key1 in json_text:
        json_dict = defaultdict(list)
        question  = json_text[key1]['question']
        json_dict['question'].append(question)
        for key2 in json_text[key1]['evidences']:
            answer = json_text[key1]['evidences'][key2]['answer']
            evidence1  = json_text[key1]['evidences'][key2]['evidence']
            json_dict['answer'] = answer
            json_dict['evidence'].append(evidence1)
        pair_dict[key1] = json_dict

    save_path = "leemonlin/python/programs/KG-based-Auto_QA-System/data/processing_data/processing" + name 
    with open(save_path,'w',encoding='UTF-8') as f:
                f.write(json.dumps(pair_dict,indent = 4))


def processing_fix(json_text,name):
    pass 



def load_json(url):
    type_json = open(url, "r",encoding='UTF-8')
    json_text = json.load(type_json)
    return json_text


if __name__ == "__main__":
    dir_path = '/mnt/data/data/home/limengling/leemonlin/python/programs/KG-based-Auto_QA-System/data/WebQA.v1.0/'
    file_list =  ['me_test.ann.json','me_test.ir.json','me_train.json','me_validation.ann.json','me_validation.ir.json']
    for file_suffix  in file_list:
        json_text = load_json(dir_path+file_suffix)
        processing_data(json_text,file_suffix)
    
   
