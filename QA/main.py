import question_classifier
import question_parser
import get_answer

query = "请解释一下操作系统的作用是什么？有哪些类型"


classifier = question_classifier.Classifier()
res_classify = classifier.classify(query)
print("你提出的问题是" + "\n" + query)
paser = question_parser.QuestionPaser()
sql_ = paser.paser(res_classify)
print(sql_)
get_answer1 = get_answer.AnswerSearcher()
get_answer1.search_main(sql_)