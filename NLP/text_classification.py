from pyhanlp import *
import zipfile
import os
from pyhanlp.static import download, remove_file, HANLP_DATA_PATH


def test_data_path():
    """
    获取测试数据路径，位于$root/data/test，根目录由配置文件指定。
    :return:
    """
    data_path = os.path.join(HANLP_DATA_PATH, 'test')
    if not os.path.isdir(data_path):
        os.mkdir(data_path)
    return data_path


## 验证是否存在语料库，如果没有自动下载
def ensure_data(data_name, data_url):
    root_path = test_data_path()
    dest_path = os.path.join(root_path, data_name)
    if os.path.exists(dest_path):
        return dest_path

    if data_url.endswith('.zip'):
        dest_path += '.zip'
    download(data_url, dest_path)
    if data_url.endswith('.zip'):
        with zipfile.ZipFile(dest_path, "r") as archive:
            archive.extractall(root_path)
        remove_file(dest_path)
        dest_path = dest_path[:-len('.zip')]
    return dest_path


sogou_corpus_path = ensure_data('搜狗文本分类语料库迷你版',
                                'http://file.hankcs.com/corpus/sogou-text-classification-corpus-mini.zip')

## ===============================================
## 以下开始 标准化评测 朴素贝叶斯 和 SVM 分类器

#classifiers 分类器
IClassifier = JClass('com.hankcs.hanlp.classification.classifiers.IClassifier')
NaiveBayesClassifier = JClass('com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier')
LinearSVMClassifier = JClass('com.hankcs.hanlp.classification.classifiers.LinearSVMClassifier')

#corpus语料库
FileDataSet = JClass('com.hankcs.hanlp.classification.corpus.FileDataSet')
IDataSet = JClass('com.hankcs.hanlp.classification.corpus.IDataSet')
MemoryDataSet = JClass('com.hankcs.hanlp.classification.corpus.MemoryDataSet')

#statistics.evaluations统计评价
Evaluator = JClass('com.hankcs.hanlp.classification.statistics.evaluations.Evaluator')
FMeasure = JClass('com.hankcs.hanlp.classification.statistics.evaluations.FMeasure')

#tokenizers标记切词
BigramTokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.BigramTokenizer')
HanLPTokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.HanLPTokenizer')
ITokenizer = JClass('com.hankcs.hanlp.classification.tokenizers.ITokenizer')


def evaluate(classifier, tokenizer):
    training_corpus = FileDataSet().setTokenizer(tokenizer).load(sogou_corpus_path, "UTF-8", 0.9)
    classifier.train(training_corpus)
    testing_corpus = MemoryDataSet(classifier.getModel()).load(sogou_corpus_path, "UTF-8", -0.1)
    result = Evaluator.evaluate(classifier, testing_corpus)
    print(classifier.getClass().getSimpleName() + "+" + tokenizer.getClass().getSimpleName())
    print(result)


if __name__ == '__main__':


    #HanLPTokenizer：中文字典分词；BigramTokenizer：二元语法分词;BlankTokenizer英文分词
    #NaiveBayesClassifier：贝叶斯分类器；LinearSVMClassifier：线性支持向量机分类器
    evaluate(NaiveBayesClassifier(), HanLPTokenizer())

    evaluate(NaiveBayesClassifier(), BigramTokenizer())
    evaluate(LinearSVMClassifier(), HanLPTokenizer())

    #线性支持向量机的分类准确率更高，且分类速度更快，推进使用
    evaluate(LinearSVMClassifier(), BigramTokenizer())