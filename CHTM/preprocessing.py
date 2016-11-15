# coding:utf-8
import codecs
import nltk
import gensim

"""
this is data preprocessing for open source code: d3_3.5.17.js
by Jeffery Zhou
"""


class Preprocess(object):
    """
        this is the data preprocessing class;
    """

    def __init__(self):
        """

        """
        self.code_path = "source_code/d3_test.js"
        self.keyword_path = 'reserved_keywords.txt'
        # self.code = self.get_code()
        self.stopword_path = '/'

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

    def get_code(self):
        """ return the code according the code file path. """
        code_file = codecs.open(self.code_path, 'r')
        code = code_file.read()  # 注释的操作
        code_file.close()
        return code

    def word_tokenize(self, code):
        return nltk.word_tokenize(code)

    def keep_word_combination(self, code):
        pass

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
        clean_code_lst = []
        for i in code:
            for j in keywords:
                if i == j:
                    code.remove(i)
        return code



p = Preprocess()
code1 = p.word_tokenize(p.get_code())
print code1
code2 = p.remove_punctuation(code1)
print code2
code3 = p.remove_keywords(code2)
print code3









