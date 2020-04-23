# -*- coding: utf-8 -*-
import pandas as pd
import jieba
from collections import Counter
from jpype import *
import pymysql
import re
import traceback
import  pyhanlp

#  加载自然语言处理模块
startJVM(getDefaultJVMPath(), "-Djava.class.path=C:\\Program Files\\hanlp\\hanlp-1.7.0.jar;C:\\Program Files\\hanlp", "-Xms1g", "-Xmx1g")
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')


