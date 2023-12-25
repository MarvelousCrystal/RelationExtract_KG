# -*- coding: utf-8 -*-
import pyltp
import os
import jieba
import jieba.posseg as pseg

# LTP_DATA_DIR = 'D:\\SoftInstall\\ltp_data_v3.4.0'  # ltp模型目录的路径


with open('C:\\Users\\lx\\Desktop\\Work\科研\\HLM\\people_relation_extract_master\\word\\name.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        l = line.replace('\n', '').split('，')
        jieba.add_word(l[0], 999, 'nr')


def cut_words(words):

    array=[]
    array1=[] #分词
    array2=[] #词性jieba
    line=pseg.cut(words)
    for l in line:
        array1.append(l.word)
        array2.append(l.flag)
    array.append(array1)
    array.append(array2)
    print(array[0])
    print(array[1])

    # 分词
    # segmentor = pyltp.Segmentor()
    # seg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
    # segmentor.load(seg_model_path)
    # words = segmentor.segment(words)
    # array_str="|".join(words)
    # array=array_str.split("|")
    # segmentor.release()
    return array


# def words_mark(array):
#
#     # 词性标注模型路径，模型名称为`pos.model`
#     pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
#     postagger = pyltp.Postagger()  # 初始化实例
#     postagger.load(pos_model_path)  # 加载模型
#     postags = postagger.postag(array)  # 词性标注
#     pos_str=' '.join(postags)
#     pos_array=pos_str.split(" ")
#     postagger.release()  # 释放模型
#     return pos_array

def get_target_array(words):

    # 获取目标词性单词
    # target_pos = ['nh', 'n']
    # target_array = []
    # seg_array = cut_words(words)
    # print(seg_array)
    # pos_array = words_mark(seg_array)
    # for i in range(len(pos_array)):
    #     if pos_array[i] in target_pos:
    #         target_array.append(seg_array[i])
    # target_array.append(seg_array[1])

    target_pos = ['nr', 'n']
    target_array = []
    array = cut_words(words)
    seg_array = array[0]
    pos_array = array[1]
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])
    target_array.append(seg_array[1])
    print(target_array)

    return target_array


def get_target_array2(words):

    # 获取目标词性单词
    # target_pos = 'nh'
    # target_array = []
    # seg_array = cut_words(words)
    # seg_array = jieba.lcut(words)
    # print(seg_array)
    # pos_array = words_mark(seg_array)
    # for i in range(len(pos_array)):
    #     if pos_array[i] == target_pos:
    #         target_array.append(seg_array[i])
    # # target_array.append(seg_array[1])
    # print(target_array)

    # print(array[0])
    target_pos = 'nr'
    target_array = []
    array = cut_words(words)
    seg_array = array[0]
    pos_array = array[1]
    for i in range(len(pos_array)):
        if pos_array[i] == target_pos:
            target_array.append(seg_array[i])
    print(target_array)

    return target_array






