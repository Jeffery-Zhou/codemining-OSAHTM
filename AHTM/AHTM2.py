# coding:utf-8
"""
building the AHTM models.
"""
import nltk
import codecs
import sys
from preprocessing import Preprocess
from gensim import corpora, models, similarities

p = Preprocess()
print "\n"

train_set = p.multi_process()

dic = corpora.Dictionary(train_set)

corpus = [dic.doc2bow(text) for text in train_set]

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=31)

lsa = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=31)

corpus_lda = lda[corpus_tfidf]

print "LDA results:"
for i in range(0, 31):
    print lda.print_topic(i, 30)

print "LSA results:"
for i in range(0, 31):
    print lsa.print_topic(i, 30)




