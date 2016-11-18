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

p.word_tokenize()
p.printer("code after tokenizing", p.code)

p.remove_what2(p.code, p.keywords_js)
p.printer("code after removing keywords", p.code)

p.remove_what2(p.code, p.punctuation_lst)
p.printer("code after removing punctuation", p.code)

print type(p.code)

train_set = []
train_set.append(p.code)

dic = corpora.Dictionary(train_set)

corpus = [dic.doc2bow(text) for text in train_set]

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

lda = models.LdaModel(corpus_tfidf, id2word = dic, num_topics = 10)

hdp = models.HdpModel(corpus_tfidf, id2word= dic)

print hdp.print_topic(0)
# print hdp.print_topic(1)
# corpus_lda = lda[corpus_tfidf]

# lda = models.LdaModel(document, num_topics=10)
# print (lda[doc_bow])
for i in range(0, 10):
    print lda.show_topic(i, 10)
    print lda.get_topic_terms(i)


