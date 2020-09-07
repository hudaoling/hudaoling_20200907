# 首先，文本数据属于非结构化数据，一般要转换成结构化的数据，一般是将文本转换成“文档 - 词频矩阵”，矩阵中的元素使用词频或者TF - IDF。
# TF - IDF的主要思想是：如果某一个词或短语在一篇文章中出现的频率高，并且在其他文章中很少出现，则认为此词或短语具有很好的类别区分能力，适合用于分类。TF - IDF = TF * IDF
# IDF主要思想：如果包含词条t的文档越少，也就是n越小，IDF越到，则说明词条t具有很好的区分能力。
# TF指的是某一个给定的词语在该文件中出现的频率，这是对词数的归一化，IDF是一个词语重要性的度量，IDF = log（D / Dn），其中对数以2为底，D为文本总数，Dn为该词在n个网页中出现过。具体证明推导可以参考《数学之美》中对于TF - IDF的介绍，其实IDF是一个特定条件下关键词的概率分布的交叉熵，是信息论中的内容。

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

# 1) 导入数据
categories = ['alt.atheism',
              'rec.sport.hockey',
              'comp.graphics',
              'sci.crypt',
              'comp.os.ms-windows.misc',
              'sci.electronics',
              'comp.sys.ibm.pc.hardware',
              'sci.med',
              'comp.sys.mac.hardware',
              'sci.space',
              'comp.windows.x',
              'soc.religion.christian',
              'misc.forsale',
              'talk.politics.guns',
              'rec.autos'
              'talk.politics.mideast',
              'rec.motorcycles',
              'talk.politics.misc',
              'rec.sport.baseball',
              'talk.religion.misc']
# 导入训练数据
train_path = '20news-bydate-train'
dataset_train = load_files(container_path=train_path, categories=categories)
# 导入评估数据
test_path = '20news-bydate-test'
dataset_test = load_files(container_path=test_path, categories=categories)
# 计算词频
count_vect = CountVectorizer(stop_words='english', decode_error='ignore')
X_train_counts = count_vect.fit_transform(dataset_train.data)
# 计算TF-IDF
tf_transfomer = TfidfVectorizer(stop_words='english', decode_error='ignore')
X_train_counts_tf = tf_transfomer.fit_transform(dataset_train.data)

# 算法评估基准
'''采用10折交叉验证的方式来比较算法的准确度'''
num_folds = 10
seed = 7
scoring = 'accuracy'
# 评估算法
models = {}
models['LR'] = LogisticRegression()  # 逻辑回归
models['SVM'] = SVC()  # 支持向量机
models['CART'] = DecisionTreeClassifier()  # 分类与回归树
models['MNB'] = MultinomialNB()  # 朴素贝叶斯分类器
models['KNN'] = KNeighborsClassifier()  # K近邻算法
results = []
for key in models:
    kfold = KFold(n_splits=num_folds, random_state=seed)
    cv_results = cross_val_score(models[key], X_train_counts_tf, dataset_train.target, cv=kfold, scoring=scoring)
    results.append(cv_results)
    print('%s:%f(%f)' % (key, cv_results.mean(), cv_results.std()))

# 逻辑回归调参
'''逻辑回归中的超参数是C，C值越小正则化强度越大'''
param_grid = {}
param_grid['C'] = [0.1, 5, 13, 15]
model = LogisticRegression()
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(X=X_train_counts_tf, y=dataset_train.target)
print('最优 : %s 使用 %s' % (grid_result.best_score_, grid_result.best_params_))
# 朴素贝叶斯分类器调参
param_grid = {}
param_grid['alpha'] = [0.001, 0.01, 0.1, 1.5]
model = MultinomialNB()
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(X=X_train_counts_tf, y=dataset_train.target)
print('最优 : %s 使用 %s' % (grid_result.best_score_, grid_result.best_params_))

# 集成算法
ensembles = {}
ensembles['RF'] = RandomForestClassifier()  # 随机森林
ensembles['AB'] = AdaBoostClassifier()  # Adaboost
results = []
for key in ensembles:
    kfold = KFold(n_splits=num_folds, random_state=seed)
    cv_results = cross_val_score(ensembles[key], X_train_counts_tf, dataset_train.target, cv=kfold, scoring=scoring)
    results.append(cv_results)
    print('%s : %f (%f)' % (key, cv_results.mean(), cv_results.std()))
# 集成算法调参
param_grid = {}
param_grid['n_estimators'] = [10, 100, 150, 200]
model = RandomForestClassifier()
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(X=X_train_counts_tf, y=dataset_train.target)
print('最优 : %s 使用 %s' % (grid_result.best_score_, grid_result.best_params_))

# 生成模型
model = LogisticRegression(C=13)
model.fit(X_train_counts_tf, dataset_train.target)
X_test_counts = tf_transformer.transform(dataset_test.data)
predictions = model.predict(X_test_counts)
print(accuracy_score(dataset_test.target, predictions))
print(classification_report(dataset_test.target, predictions))
