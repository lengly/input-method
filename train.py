#-*- coding: utf8 -*-
import jieba
import jieba.posseg
import nltk

words = []
fd = None

def load():
    global words, fd
    cnt = 0
    print '读入语料库'
    with open("prose.txt","r") as f:
        for line in f.read().split('\n'):
            words.extend(list(jieba.cut(line)))
    print '语料库分词完毕'
    fd = nltk.FreqDist(words)

def sort(lists):
    n = len(lists)
    for i in range(n):
        for j in range(i):
            if fd[lists[j].decode('utf8')] < fd[lists[i].decode('utf8')]:
                lists[i],lists[j] = lists[j],lists[i]

def train_with_freq(dictionary):
    for key,values in dictionary.items():
        sort(values)
    print '字典频率训练完毕'
