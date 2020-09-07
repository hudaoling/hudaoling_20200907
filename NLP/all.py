#载入接下来分析用的库
# import pandas as pd
# import numpy as np
# import xgboost as xgb
# from tqdm import tqdm
# from sklearn.svm import SVC
# from keras.models import Sequential
# from keras.layers.recurrent import LSTM, GRU
# from keras.layers.core import Dense, Activation, Dropout
# from keras.layers.embeddings import Embedding
# from keras.layers.normalization import BatchNormalization
# from keras.utils import np_utils
# from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
# from sklearn.model_selection import GridSearchCV
# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn.decomposition import TruncatedSVD
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# from sklearn.naive_bayes import MultinomialNB
# from keras.layers import GlobalMaxPooling1D, Conv1D, MaxPooling1D, Flatten, Bidirectional, SpatialDropout1D
# from keras.preprocessing import sequence, text
# from keras.callbacks import EarlyStopping
# from nltk import word_tokenize

import  re

import os
path = "D:/PythonStudy/NLP/data/train_corpus" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
print(files)

news_dict={}
for i in [i.split('-') for i in files]:
    news_dict[i[0]]=i[1]
print(news_dict)

s=[]
for file in files: #遍历文件夹
    sub_path=path+'/'+file
    sub_files=os.listdir(sub_path)
    # print(sub_path,sub_files)
    # for f in sub_files:
        # print(f)
        # print(sub_path+"/"+f)
#         if not os.path.isdir(f):  # 判断是否是文件夹，不是文件夹才打开
#             f = open(sub_path+"/"+f,'rb')  #打开文件
#             articles=f.read().decode('utf-8','ignore')
#             print(articles)
#             iter_f = iter(f)  #创建迭代器
#             str = ""
#             for line in iter_f: #遍历文件，一行行遍历，读取文本
#                  str = str + line
#             s.append(str) #每个文件的文本存到list中
# #
# print(s)

f=open('D:/PythonStudy/NLP/data/train_corpus/C11-Space/C11-Space0001.txt','rb')
print(f.read().decode(encoding='utf-8'))
