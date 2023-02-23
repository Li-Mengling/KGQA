import pdfplumber
from collections import defaultdict
import json
class pdf2text:
    def __init__(self):
        ###手动建立一个字典key->章节名，value->重置章节页数
        self.main_chapter = {"Information Technology, the Internet, and You":"2",
                    "The Internet, the Web, and Electronic Commerce":"24",
                    "Application Software":"56",
                    "System Software":"84",
                    "The System Unit":"108",
                    "Input and Output":"134",
                    "Secondary Storage":"164",
                    "Communications and Networks":"186",
                    "Privacy, Security, and Ethics":"214",
                    "Information Systems":"246",
                    "Databases":"268",
                    "Systems Analysis and Design":"292",
                    "Programming and Languages":"316",
                    "The Evolution of the Computer Age":"347",
                    "The Computer Buyer’s Guide":"358",
                    "Glossary":"362",
                    "Index":"383"
                    }
        self.ret = None


    def by_chapter(self,source_path):
        for item,value in self.main_chapter.items():
            new_value = int(value) + 52
            self.main_chapter[item] = str(new_value)
        #重置章节的必要性：之前并不是每一页都有页码
        with pdfplumber.open(source_path) as pdf:
            reset_page = 1
            for page in pdf.pages:
                page_text = page.extract_text() +"\nreset page " + str(reset_page)+'\n'+'-------------------------------------------- 分页分隔 --------------------------------------------\n'
                reset_page += 1
                f = open(r'text.txt','a',encoding='UTF-8')
                f.write(page_text)
                # 每页打印一分页分隔

    #判别函数，用于判断字符串是否含有字母单词
    def check_string(self,s):
        has_digit = False
        has_letter = False
        for c in s:
            if c.isdigit():
                has_digit = True
            elif c.isalpha():
                has_letter = True
            if has_digit and has_letter:
                return 1
        if has_digit:
            return 0
        elif has_letter:
            return -1
        else:
            return None

    #获取图书目录json字典
    def get_dict(self,edit_path,write_json_path):
        list_chapter = list(self.main_chapter)
        i_chapter = []
        ii_chapter = []

        with open(edit_path,'r',encoding='utf-8') as f :
            lines = f.readlines()
        sub_list = []
        sub_dict = {}
        for i in range(len(lines)-1):
            if self.check_string(lines[i]) == -1:
                ii_chapter.append(lines[i].replace(' \n',''))
                sub_list = []
            elif self.check_string(lines[i]) == 1:
                sub_list.append(lines[i].replace('\n',''))
                if self.check_string(lines[i+1]) == -1:
                    sub_dict[ii_chapter[-1]] = sub_list
            elif self.check_string(lines[i]) == 0:
                pass
        ii_chapter = ii_chapter[2:]

        
        for ii in ii_chapter:
            if ii.find('\xa0') != -1:
                ii_chapter.remove(ii)

        find_index1  = 0 #用于定位list_chapter 
        default_dict = defaultdict(list)
        for chapter in ii_chapter:
            if chapter.find(list_chapter[find_index1].upper()) != -1 :
                default_dict[list_chapter[find_index1]] = []
                i_chapter.append(list_chapter[find_index1])
                if self.main_chapter[list_chapter[find_index1]] == '383':
                    break
                find_index1 += 1
            elif find_index1 != 0:
                default_dict[list_chapter[find_index1 -1]].append(chapter)


        i_chapter = [i.upper() for i in i_chapter]
        ii_chapter = [i for i in ii_chapter if i not in i_chapter]
        for key,value in default_dict.items():
            for sub_key,sub_value in sub_dict.items():
                add_dict = {}
                if sub_key in value:
                    add_dict[sub_key] = sub_value
                    value[value.index(sub_key)] = add_dict
                    default_dict[key] = value
        json_dict = json.dumps(default_dict,indent = 4)
        with open(write_json_path,'w',encoding='UTF-8') as f:
                    f.write(json_dict)




if __name__ == "__main__":
    source_path = r"leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/ISE EBook for Computing Essenti - O'Leary, Timothy;O'Leary, Linda.pdf"
    edit_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/edit.txt'
    write_json_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/json_dict.json'
    pdf2text =pdf2text()
    # pdf2text.by_chapter(source_path)
    pdf2text.get_dict(edit_path,write_json_path)