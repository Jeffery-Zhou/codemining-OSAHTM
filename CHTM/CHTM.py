# coding:utf-8
"""

"""
import nltk
import gensim
import codecs
import sys

# nltk.download()
file_test = codecs.open("source_code/d3_test.js", 'r')
code1 = file_test.read()
file_test.close()
print code1

code_tokenize = nltk.word_tokenize(code1)

print "\n"
print "==========================code after tokenizing===================="
print code_tokenize
print type(code_tokenize)
print code_tokenize[-110:]


