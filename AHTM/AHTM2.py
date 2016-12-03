# coding:utf-8
"""
building the AHTM models.
"""
import nltk
import codecs
import sys
import pandas
import numpy
from preprocessing import Preprocess
from gensim import corpora, models, similarities
import pyLDAvis
import pyLDAvis.gensim as pg
from pprint import pprint
p = Preprocess()
print "\n"

train_set = p.multi_process()

dic = corpora.Dictionary(train_set)
dic.save_as_text('dic1_AHTM', False)
# 提取出文档集的词和词频
print dic.id2token
print dic.token2id
print dic.dfs
print dic.num_docs
print dic.num_nnz
print dic.num_pos


print dic[0]

corpus = [dic.doc2bow(text) for text in train_set]
# dicno:[(id, freqnum), ....]

print corpus[0]

# print corpus
# 每个文档转成词袋模型

tfidf = models.TfidfModel(corpus)
# tfidf.save("tfidf_AHTM")

corpus_tfidf = tfidf[corpus]
print "corpus_tfidf: \n"
print corpus_tfidf

lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=31)
print "lda: documents -> topics"
d_t_lst = [i for i in lda.get_document_topics(corpus)]

for i in d_t_lst:
    p_dt_sum = 0
    print i
    print len(i)
    print ''
    for j in i:
        p_dt_sum += j[1]
    print p_dt_sum

#
lsa = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=31)
#
corpus_lda = lda[corpus_tfidf]

# print "LDA results:"
# for i in range(0, 31):
#     print lda.print_topic(i, 30)
#
print "LSA results:"
for i in range(0, 31):
    print lsa.print_topic(i, 30)

for doc in lsa:
    print doc

# pyLDAvis.gensim.prepare(lda, corpus, dic)




