# coding:utf-8
import codecs
"""
this is data preprocessing for open source code: d3.v4.js
by Jeffery Zhou
2016年11月11日
"""


class Preprocess(object):
    '''this is the data preprocessing class;

    '''



    def __init__(self):
        '''

        '''
        self.code_path = "/source_code/d3_test.js"
        self.keyword_path = 'reserved_keywords.txt'
        self.stopword_path = '/'

    def get_keyword(self):
        '''

        :return:
        '''
        keywords_lst = []
        word_file = codecs.open(self.keyword_path, 'r')
        words = word_file.read()
        word_file.close()
        keywords_lst = words.split('\n')
        return keywords_lst

p = Preprocess()
print p.get_keyword()









