# 打开文件并读取内容
path = r'leemonlin/python/programs/KG-based-Auto_QA-System/ComputingEssential/book_text/text.txt'
with open(path, "r",encoding='utf-8') as f:
    content = f.read()

# 用正则表达式替换字符串
import re
content = re.sub(r"page \d+", "", content)

# 将修改后的内容写回文件
with open(path, "w",encoding='utf-8') as f:
    f.write(content)

print("替换完成！")