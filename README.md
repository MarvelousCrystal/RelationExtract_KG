# The Character Relationship Query System for the Dream of the Red Chamber  

# background

There are already many knowledge graph systems based on the relationships between characters in "Dream of the Red Chamber." This system aims to reference existing systems(Which do not have knowledge extraction---relationship extraction) and more efficiently organize and represent a knowledge graph system based on the relationships between characters in "Dream of the Red Chamber." Additionally, through knowledge graph reasoning and computation, this system will enable intelligent Q&A regarding the relationships between characters in "Dream of the Red Chamber."

# environment

python 3.6(3.8 is not available)

tensorflow 1.13.1

keras 2.3.1

pandas 0.23.4

matplotlib 2.2.4

numpy 1.16.2

运行该项目的模型训练和模型预测脚本需要准备BERT中文版的模型数据，下载网址为：https://github.com/google-research/bert/blob/master/multilingual.md 。

neo4j

# dataset

 A total of 2,463 pieces of data have been collected, including 297 pieces related to the relationships between characters in "Dream of the Red Chamber." The data is stored in the file `people_relation_extract_master/data/人物关系表(测试集).xlsx`.

Based on the relationships between characters in "Dream of the Red Chamber," eight categories have been defined: unknown, married couple, parent-child, siblings, master-servant, friends, grandparent-grandchild, and relatives, as shown in Figure 1.

![image-20240729113927128](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240729113927128.png)

<center>figure 1</center>

爬虫来源于

# relationship extraction

### data preprocessing

Read the original text of "Dream of the Red Chamber" and extract sentences containing character names based on an existing name list. First, extract 297 pieces of data related to character relationships in "Dream of the Red Chamber" and include them in the total corpus. The dataset is then split into training and test sets in an 8:2 ratio.

### model training

Before training the model, the data needs to be processed to better fit the model format. This involves further processing of `train.txt` and `test.txt`, and then starting the training process.

Model structure: BERT + Bi-directional GRU + Attention + FC. The training results are shown in Figure 2.

![image-20240729114953838](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240729114953838.png)

<center>figure 2</center>

### post-processing of predicted results

![image-20240729162912643](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240729162912643.png)

<center>figure 3</center>

Since the corpus containing each pair of character names appears more than once, multiple relationships will naturally be predicted. First, we remove the relationships classified as "unknown." Then, for each pair of character names, we select the relationship triplet that appears most frequently as the final relationship and write it into `result.txt`, as shown in Figure 4.

![image-20240729162816209](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240729162816209.png)

<center>figure 4</center>

### relationship display

![image-20240730170402752](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240730170402752.png)

<center>figure 5</center>

# query system

 The system allows users to query the specific relationships of individual characters in "Dream of the Red Chamber." For example, to query the relationships of a particular character, you can use the following command, as illustrated in Figure 6.

![image-20240730171236290](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240730171236290.png)

<center>figure 6</center>

The system also supports querying the relationships between two characters, as shown in Figure 7.

![image-20240730171350036](C:\Users\LHY\AppData\Roaming\Typora\typora-user-images\image-20240730171350036.png)

<center>figure 7</center>
