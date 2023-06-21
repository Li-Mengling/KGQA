import pdfplumber
from collections import defaultdict
import json
import os

class Pdf2text:
    def __init__(self):
        ###手动建立一个字典:{key->章节名，value->重置章节页数}
        self.main_chapter = {"0 prologue":"1",
                    "1 Information Technology, the Internet, and You":"53",
                    "2 The Internet, the Web, and Electronic Commerce":"102",
                    "3 Application Software":"176",
                    "4 System Software":"233",
                    "5 The System Unit":"283",
                    "6 Input and Output":"344",
                    "7 Secondary Storage":"419",
                    "8 Communications and Networks":"469",
                    "9 Privacy, Security, and Ethics":"536",
                    "10 Information Systems":"604",
                    "11 Databases":"649",
                    "12 Systems Analysis and Design":"697",
                    "13 Programming and Languages":"747",
                    "14 The Evolution of the Computer Age":"808",
                    "15 The Computer Buyer’s Guide":"825",
                    "16 Glossary":"836",
                    "17 Index":"891",
                    "End":"957"
                    }
        self.ret = None

    '''
        将pdf文件转换成txt文件存放，只运行一次
    '''
    def reset_txt(self,source_path,write_path):
        #reset page重置章节的必要性：之前并不是每一页都有页码
        with pdfplumber.open(source_path) as pdf:
            reset_page = 0
            for page in pdf.pages:
                page_text = page.extract_text() +"\nreset page " + str(reset_page)+'\n'+'-------------------------------------------- 分页分隔 --------------------------------------------\n'
                reset_page += 1
                f = open(write_path,'a',encoding='UTF-8')
                f.write(page_text)
                # 每页打印一分页分隔

    '''
        判别函数，用于判断字符串是否含有字母单词
    '''
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

    '''
        获取图书目录json字典
    '''
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

    '''
        按章节存放txt
    '''
    def get_by_chapter(self,write_path):
        with open(write_path, 'r',encoding = 'utf-8') as f:
            content = f.read()

        # 以分页符进行分割
        pages = content.split('-------------------------------------------- 分页分隔 --------------------------------------------')
        pages = pages[:958]
        
        for item,value in self.main_chapter.items():
            new_value = int(value) 
            self.main_chapter[item] =  new_value
        prefix = r"leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/chapter"
        now_page = 0
        now_key = ''
        suffix = ".txt"
        for key,value in self.main_chapter.items():
            if value == 1:
                now_key = key
                continue
            chapter_path  = os.path.join(prefix,now_key+suffix)
            str_list = pages[now_page:value-1]
            now_page = value
            now_key = key
            chapter_str = self.list2str(str_list)
            with open(chapter_path,'w',encoding='utf-8') as f:
                f.write(chapter_str)

    def list2str(self,str_list):
        prologue = ''
        for i in str_list:
            prologue = prologue+ str(i)+'-------------------------------------------- 分页分隔 --------------------------------------------'
        return prologue

if __name__ == "__main__":
    source_path = r"leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/ISE EBook for Computing Essenti - O'Leary, Timothy;O'Leary, Linda.pdf"
    edit_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/edit.txt'
    write_json_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/json_dict.json'
    write_path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/text.txt'
    pdf2text = Pdf2text()
    # pdf2text.reset_txt(source_path,write_path)
    # pdf2text.get_dict(edit_path,write_json_path)
    pdf2text.get_by_chapter(write_path)