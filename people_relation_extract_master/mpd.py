import os, json
import numpy as np
from bert.extract_feature import BertVector
from keras.models import load_model
from att import Attention

# 加载训练效果最好的模型
model_dir = './models'
files = os.listdir(model_dir)
models_path = [os.path.join(model_dir, _) for _ in files]
best_model_path = sorted(models_path, key=lambda x: float(x.split('-')[-1].replace('.h5', '')), reverse=True)[0]
print(best_model_path)
model = load_model(best_model_path, custom_objects={"Attention": Attention})

# 利用BERT提取句子特征
bert_model = BertVector(pooling_strategy="NONE", max_seq_len=80)

with open('./word/text1.txt', 'w', encoding='utf-8') as f1:
    with open('./word/sentence6.txt', 'r', encoding='utf-8') as f2:
        for line in f2.readlines():
            if len(line) == 1:
                continue
            per1, per2, doc = line.split('#')
            text = '$'.join([per1, per2, doc.replace(per1, len(per1) * '#').replace(per2, len(per2) * '#')])
            print(text)

            # 利用BERT提取句子特征
            # bert_model = BertVector(pooling_strategy="NONE", max_seq_len=80)
            vec = bert_model.encode([text])["encodes"][0]
            x_train = np.array([vec])

            # 模型预测并输出预测结果
            predicted = model.predict(x_train)
            y = np.argmax(predicted[0])

            with open('data/rel_dict.json', 'r', encoding='utf-8') as f:
                rel_dict = json.load(f)

            id_rel_dict = {v: k for k, v in rel_dict.items()}
            print('原文: %s' % line)
            print('预测人物关系: %s' % id_rel_dict[y])
            if id_rel_dict[y] == 'unknown':
                continue
            f1.write(per1 + ',' + per2 + ',' + id_rel_dict[y] + '\n')
            # f1.write(line+id_rel_dict[y]+'\r\n')
