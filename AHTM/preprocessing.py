# coding:utf-8
import os
import sys
import codecs
import nltk
from remove_word.punctuation import punc_lst
import logging
reload(sys)
sys.setdefaultencoding('utf-8')

"""
this is data preprocessing for open source code: d3_3.5.17.js
by Jeffery Zhou
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/preprocessing.log',
                    filemode='w')


class Preprocess(object):
    """
        this is the data preprocessing class;
    """
    code_path = "./source_code/d3_test.js"
    # code_path = "./source_code/d3_3.5.17.js"
    keyword_html_path = "./remove_word/keywords_html.txt"
    keyword_built_path = "./remove_word/built_in_object.txt"
    keyword_css_path = "./remove_word/keywords_css.txt"
    stop_word_path = "./remove_word/stop_words.txt"
    reserved_keyword_js_path = "./remove_word/reserved_keywords_js.txt"
    code_echarts_path = "./source_code/echarts"

    def multi_process(self):
        train_set = []
        walk = os.walk(Preprocess.code_echarts_path)
        name_no = 0
        for root, dirs, files in walk:
            for name in files:
                name_no += 1
                print name, name_no

                f = codecs.open(os.path.join(root, name), 'r', 'utf-8')
                raw = f.read()
                f.close()
                tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
                raw_ = tokenizer.tokenize(raw)
                raw__ = self.remove_what2(raw_, self.keywords_js)
                train_set.append(raw__)
        return train_set
        # raw = f.read()
        # word_list = list(jieba.cut(raw, cut_all=False))
        # train_set.append(word_list)





        pass


    def __init__(self):
        """

        """
        logging.info("object initializing...")
        self.punctuation_lst = punc_lst
        logging.info("punctuation archiving...")
        self.keywords_js = self.get_what_word(Preprocess.reserved_keyword_js_path)
        logging.info("got keyword for js!")
        # self.stopword = self.get_what_word(Preprocess.stop_word_path)
        # self.keyword_html = self.get_what_word(Preprocess.keyword_html_path)
        # self.keyword_css = self.get_what_word(Preprocess.keyword_css_path)
        self.code_path = Preprocess.code_path
        self.code = self.get_code()


    def get_code(self):
        """ return the code according the code file path. """
        code_file = codecs.open(self.code_path, 'r')
        code = code_file.read()  # 注释的操作
        code_file.close()
        logging.info("got code!")
        return code

    def get_code_multifile(self):
        """

        :return:
        """
        pass

    def get_what_word(self, path):
        word_file = codecs.open(path, 'r')
        words = word_file.read()
        word_file.close()
        words_lst = words.split('\n')
        return words_lst

    def word_tokenize(self):
        code = self.code
        # self.code = nltk.word_tokenize(code)

        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        self.code = tokenizer.tokenize(self.code)

    def keep_word_combination(self, code):
        pass

    def remove_what(self, code, remove_lst):
        """
        remove the word in remove_lst from code
        :param code:
        :param remove_lst:
        :return:
        """
        flag = True
        clean_code_lst = []
        for i in code:
            # if the word in the loop of remove_lst, change the flag
            for j in remove_lst:
                if i == j:
                    flag = False
            if flag:
                clean_code_lst.append(i)
            flag = True
        return clean_code_lst

    def remove_what2(self, code, remove_lst):
        """
        the same function of the remove_what
        :param code:
        :param remove_lst:
        :return:
        """
        # self.code = [i for i in code if i not in remove_lst]
        return [i for i in code if i not in remove_lst]

    def remove_operation_class(self, ):
        """
        处理类的运算符: .
        process the operation of class: .
        """
        pass

    def process_word_combination(self, ):
        pass

    def get_freq(self):
        fr_dct = nltk.FreqDist(self.code)
        # nltk.FreqDist.plot(fr_dct)
        return fr_dct

    # =========================================================
    def get_keyword(self):
        """
        get the keyword and reserved words in Javascript
        :return: keywords_lst
        """
        word_file = codecs.open(self.keyword_path, 'r')
        words = word_file.read()
        word_file.close()
        keywords_lst = words.split('\n')
        return keywords_lst

    def remove_punctuation(self, code):
        punc_lst = [
            '[', ']', '!', '(', ')', '=', '{', '}', ':', ';', ',',
            '&', '||', '--', '``', '+', '-', '*', '/', "''",
            '>', '<', '<=', '>=', '==', '?', '===', '!'
        ]

        clean_code_lst = []
        flag = True
        for i in code:
            for j in punc_lst:
                if i == j:
                    flag = False
            if flag:
                clean_code_lst.append(i)
            flag = True
        return clean_code_lst

    def remove_keywords(self, code):
        keywords = self.get_keyword()
        flag = True
        clean_code_lst = []
        for i in code:
            for j in keywords:
                if i == j:
                    flag = False
            if flag:
                clean_code_lst.append(i)
            flag = True
        return clean_code_lst

    def printer(self, info, content):
        for i in range(10):
            print '-',
        print ' ',
        print info,
        print ' ',
        for i in range(10):
            print '-',
        print '\n'
        print content, '\n'
        # print '\n'
        # for i in range(20+len(info)):
        #     print '-',
        # print '\n'

p = Preprocess()
# p.printer("code start", p.code)
p.word_tokenize()
p.printer("code after tokenizing", p.code)
p.printer("keyword in JS", p.keywords_js)
p.remove_what2(p.code, p.keywords_js)
p.printer("code after removing keywords", p.code)
p.remove_what2(p.code, p.punctuation_lst)
p.printer("code after removing punctuation", p.code)

freq_dct = p.get_freq()
p.printer("code freq ", freq_dct)

# for i in freq_dct.iteritems():
#     print i

# fd = freq_dct
fd = freq_dct
fd_keys_sorted = (key for key, value in sorted(fd.items(), key=lambda item: item[1], reverse=True))

count_dict = 0
for key in fd_keys_sorted:
    if count_dict < 100:
        print key, fd[key]
    count_dict += 1

# nltk.download()
# nltk.probability.gt_demo()
# print freq_dct[]
# print type(freq_dct[''])
# print type(freq_dct)
# freq_dct_sorted = sorted(freq_dct.iteritems(), key=lambda d: d[1], reverse=True)
#
# for i in freq_dct_sorted:
#     print i















