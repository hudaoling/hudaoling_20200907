import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":
    corpus = ["我 来到 北京 清华大学",  # 第一类文本切词后的结果，词之间以空格隔开
              "他 来到 了 网易 杭研 大厦",  # 第二类文本的切词结果
              "小明 硕士 毕业 与 中国 科学院",  # 第三类文本的切词结果
              "我 爱 北京 天安门"]  # 第四类文本的切词结果


    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值

    tf_metrix=vectorizer.fit_transform(corpus)#fit_transform是将文本转为词频矩阵
    print('tf_metrix:',tf_metrix)

    tfidf = transformer.fit_transform(tf_metrix)  # fit_transform是计算tf-idf
    print('tfidf:',tfidf)

    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语,列表list格式
    print('word:',word)

    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    print('weight:',weight)

    for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for遍历某一类文本下的词语权重
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])





# 建议使用TfidfVectorizer，它相当于TfidfTransformer+CountVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer


document = ["我 来到 北京 清华大学",  # 第一类文本切词后的结果，词之间以空格隔开
          "他 来到 了 网易 杭研 大厦",  # 第二类文本的切词结果
          "小明 硕士 毕业 与 中国 科学院",  # 第三类文本的切词结果
          "我 爱 北京 天安门"]  # 第四类文本的切词结果

tfidf_model = TfidfVectorizer().fit(document)#建模

word_2= tfidf_model.vocabulary_   # 词袋，词语与列的对应关系,字典dict格式
print('word_2:',word_2)
print(list(word_2.keys()))


tfidf_2 = tfidf_model.transform(document)  # 得到tf-idf矩阵，稀疏矩阵表示法
print('tfidf:',tfidf_2)#


weight_2 = tfidf_2.toarray()
print('toarray:',weight_2)
print('todense:',tfidf_2.todense())   # toarray和todense输出一致,但是toarray可以通过i，j取值


for i in range(len(weight_2)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for遍历某一类文本下的词语权重
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word_2)):
        print(i,j)
        print(list(word_2.keys())[j], weight_2[i][j])

