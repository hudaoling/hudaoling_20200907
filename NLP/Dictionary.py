

#字典切词
def load_dictionary():
    '''加载字典，返回dict'''
    dic = set()

    # 按行读取字典文件，每行第一个空格之前的字符串提取出来。
    for line in open("CoreNatureDictionary.mini.txt", "r",encoding=' utf-8 '):
        dic.add(line[0:line.find('	')])

    return dic


def fully_segment(text, dic):
    '''切词：找出一段文本中的所有单词'''
    word_list = []
    for i in range(len(text)):  # i 从 0 到text的最后一个字的下标遍历
        for j in range(i + 1, len(text) + 1):  # j 遍历[i + 1, len(text)]区间
            word = text[i:j]  # 取出连续区间[i, j]对应的字符串
            if word in dic:  # 如果在词典中，则认为是一个词
                word_list.append(word)
    return word_list


# dic = load_dictionary()
# print(fully_segment('我们就读北京大学', dic))


def forward_segment(text, dic):
    '''正向最长匹配'''

    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]                      # 当前扫描位置的单字
        for j in range(i + 1, len(text) + 1):       # 所有可能的结尾
            word = text[i:j]                        # 从当前位置到结尾的连续字符串
            if word in dic:                         # 在词典中
                if len(word) > len(longest_word):   # 并且更长
                    longest_word = word             # 则更优先输出
        word_list.append(longest_word)              # 输出最长词
        i += len(longest_word)                      # 正向扫描
    return word_list

# dic = load_dictionary()
# print(forward_segment('就读北京大学', dic))
# print(forward_segment('研究生命起源', dic))


def backward_segment(text, dic):
    '''逆向最长匹配'''

    word_list = []
    i = len(text) - 1
    while i >= 0:                                   # 扫描位置作为终点
        longest_word = text[i]                      # 扫描位置的单字
        for j in range(0, i):                       # 遍历[0, i]区间作为待查询词语的起点
            word = text[j: i + 1]                   # 取出[j, i]区间作为待查询单词
            if word in dic:
                if len(word) > len(longest_word):   # 越长优先级越高
                    longest_word = word
                    break
        word_list.insert(0, longest_word)           # 逆向扫描，所以越先查出的单词在位置上越靠后
        i -= len(longest_word)
    return word_list

# dic = load_dictionary()
# print(backward_segment('研究生命起源', dic))
# print(backward_segment('项目的研究', dic))




def count_single_char(word_list: list):  # 统计单字成词的个数
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dic):
    '''双向最长匹配'''

    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):  # 词数更少优先级更高
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):  # 单字更少优先级更高
            return f
        else:
            return b  # 都相等时逆向匹配优先级更高


# print(bidirectional_segment('研究生命起源', dic))
# print(bidirectional_segment('项目的研究', dic))




## 节点类
class Node():
    def __init__(self) -> None:
        self.children = {}
        self.value = None

    # 增加节点
    def add_child(self, char, value, overwrite=False):
        child = self.children.get(char)
        if child is None:
            child = Node()  # 创建子节点
            self.children[char] = child  # 子节点赋值，字 -> 节点的映射

        if value is not None or overwrite:
            child.value = value  # 节点上对应的词

        return child


## 字典树  继承节点类
class Trie(Node):

    def __contains__(self, key):
        return self[key] is not None

    # 查询方法
    def __getitem__(self, key): #key=用户输入的‘词语’
        # print(key)
        state = self
        for char in key: #key的单字循环：自  然 人
            state = state.children.get(char)
            # print(state.value)
            if state is None:
                return None

        return state.value

    # 重载方法，使得类可以像对待dict那样操作字典树
    # 构建一个词的字典树
    def __setitem__(self, key, value):
        state = self
        print(value)
        for i, char in enumerate(key):
            print(i,char)
            if i < len(key) - 1:
                state = state.add_child(char, None)
                print(state.value)
            else:
                state = state.add_child(char, value, True)
                print(state.value)



if __name__ == '__main__':

    trie = Trie() #实例化
    # 增
    trie['自然'] = 'nature'
    trie['自然人'] = 'human'
    trie['自然语言'] = 'language'
    trie['自语'] = 'talk	to oneself'
    trie['入门'] = 'introduction'

    assert '自然' in trie
    assert '自然人' in trie
    assert '自然语言' in trie


    # # 删
    # trie['自然'] = None
    #
    # assert '自然' not in trie
    # # 改
    # trie['自然语言'] = 'human language'
    #
    # assert trie['自然语言'] == 'human language'
    # # 查
    # assert trie['入门'] == 'introduction'
    # print()