# 面向选课新生的课程问答：知识图谱+问答系统

### 1. 问题

​	\*数据：结构化数据+非结构化数据+半结构化数据

​	\*如何定义以及构建知识图谱

​	\*问答系统的搭建

​	\*页面功能设计：点赞功能

​	\*页面UI设计：类知乎问答记录生成

​	\*数据库的搭建

****



### 2. 任务细分

####  2.1 数据

​	重点需要讨论：如何规范数据的格式以便下游操作（将数据抽取成实体-关系-实体和实体-属性-属性值的形式存放(json文件)）

​	1.数据源：百度问答 链接: https://pan.baidu.com/s/1pLXEYtd 密码: 6fbf

```
2. 文件列表：
WebQA.v1.0/readme.txt
WebQA.v1.0/me_test.ann.json （一个问题只配一段材料，材料中有答案）
WebQA.v1.0/me_test.ir.json （一个问题配多段材料，材料可能有也可能没有答案）
WebQA.v1.0/me_train.json （混合的训练语料）
WebQA.v1.0/me_validation.ann.json （一个问题只配一段材料，材料中有答案）
WebQA.v1.0/me_validation.ir.json （一个问题配多段材料，材料可能有也可能没有答案）
```

1. 数据示例：

   'Q_ANN_VAL_000689':

    {'question': '李有才板话中深受封建等级思想毒害的是谁?', 

   'evidences': 

   ​       {'Q_ANN_VAL_000689#00':

   ​                            {

   ​								'answer': ['老秦'],

   ​							    'evidence': '小芹的恋爱受到二诸葛和三仙姑的阻碍,主要是因为这些封建家长们落后的封建  	思想...《李有才板话》中的老秦,是受封建等级官念毒害极深的人,当他认为从县里来的...'

   ​                            }

   ​     }

   }

​	4.数据处理

​	 将对应文件整理为question : {} answer : {} evidence : {}的形式分别存放在文件中。

####  2.2 知识图谱

##### 2.2.1.已有学科知识图谱：

1.数据

​	（1） 清华大学教育kg 链接：https://github.com/THU-KEG/EDUKG	![知识图谱](C:\Users\Leemonlin\AppData\Roaming\Typora\typora-user-images\image-20230208192423372.png)

​	（2）CN-DBpedia三元组数据 链接：http://kw.fudan.edu.cn/cndbpedia/download/

​			  具体内容查看：http://www.openkg.cn/dataset/cndbpedia

​	（3）ownthink中文知识图谱：https://github.com/ownthink/KnowledgeGraphData

​			  数据下载链接：https://pan.baidu.com/s/1LZjs9Dsta0yD9NH-1y0sAw 提取码: 3hpp ）注：解压密码是：https://www.ownthink.com/

2.安装并配置neo4j：

​	ps：3.x版本需要jdk版本11以上，5.x版本需jdk版本17以上，现已部署至服务器，浏览器访问：http://192.168.0.112:7474/browser，账号：neo4j,密码: (密码为空格)

3.导入ttl文件至neo4j:

​	需下载插件：https://github.com/neo4j-labs/neosemantics，并将其放入%NEO4J_HOME%/plugins目录下，同时插件版本必须和neo4j版本对应。该插件[官方文档](https://neo4j.com/labs/neosemantics/4.0/import/)。

4.导入Cql:

``` CQL
CALL n10s.rdf.import.fetch("file:///C:\\Users\\Leemonlin\\Desktop\\清华大学edukg\\main.ttl", "Turtle");
```

**2.2.1.自建学科知识图谱：**

#### 2.3 问答系统

| 1.方法一 ：通过match语句对用户问题进行查找匹配并返回合适结果。 |
| ------------------------------------------------------------ |
| 问题（文本）--> CQL --> 数据库 -->结果 -->返回答案（自然语言生成文本) |
| 模板+文本匹配:模板的设计                                     |
| <img src="C:\Users\Leemonlin\AppData\Roaming\Typora\typora-user-images\image-20230208203123365.png" alt="模板示例" style="zoom:150%;" /> |

![image-20230208205812309](C:\Users\Leemonlin\AppData\Roaming\Typora\typora-user-images\image-20230208205812309.png)



**************************

### 3.资源共享

​		目前检索到的关于KGQA和智能问答的博客汇总如下：

​		\*[面向职场的KGQA](https://blog.csdn.net/weixin_46571822/article/details/125555649)

​		\*[百度飞浆关于KGQA的项目](https://blog.csdn.net/m0_63642362/article/details/122158783)，另附有关键算法代码

​		\*[针对复杂问题的知识图谱问答最新进展](https://zhuanlan.zhihu.com/p/134090164)

​		\*[北京邮电大学硕士论文-基于知识图谱与深度学习的问答系统算法研究与实现](https://kns.cnki.net/KCMS/detail/detail.aspx?filename=1021130320.nh&dbname=CMFD202201&dbcode=cdmd&uid=&v=MDA2MjVSWWFtejExUEhia3FXQTBGckNVUjdtZlplZHJGeXJoVjcvTFZGMjVIN0s3SHRMT3I1RWJQSVIrZm5zNHk=)

****

### 4. 反馈栏

​	大家有什么问题，可以汇总在这里。

​	\-   2023/2/9 李孟灵 上传更新：更新了百度问答数据集以及对其整理的代码

​	-  2023/2/14 李孟灵 更新了README文档





​	
