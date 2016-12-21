# coding:utf-8
"""
building the AHTM models.
"""
import nltk
import codecs
import sys
import pandas
import numpy
import gensim
from preprocessing import Preprocess
from gensim import corpora, models, similarities
import pyLDAvis
p = Preprocess()
print "\n"
pm = p.multi_process()
train_set = pm[0]
# [ [],
#   [],...
#     ]
before_word_num = pm[1]
after_word_num = pm[2]
# print before_word_num
# print after_word_num



for i in train_set:
    for j in i:
        if len(j) <= 1:
            print "有长度为1的存在哦。"

dic = corpora.Dictionary(train_set)
dic2 = corpora.Dictionary(train_set)

# dic.save_as_text('dic1_AHTM', False)
# 提取出文档集的词和词频
# print dic.id2token
# print dic.token2id
# print dic.dfs
# print dic.num_docs
# print dic.num_nnz
# print dic.num_pos


# print dic[0]

corpus = [dic.doc2bow(text) for text in train_set]

# print "dic-------------------"
# for i in dic:
#     print dic(i),
    # print i, dic.id2token, dic.dfs, dic.num_docs, dic.num_pos
corpus2 = [[dic2.doc2bow(text, allow_update=True) for text in train_set]]
# print dic2.num_pos
print "dct2 ===================="
print dic2.num_docs


# dicno:[(id, freqnum), ....]

# bow_len = []
# for doc in corpus:
#     bow_len.append(len(doc))
#
# print "before length"
# for i in before_word_num:
#     print i
# print ""
#
# print "after length"
# for i in after_word_num:
#     print i
# print ""
#
# print "bow length"
# for i in bow_len:
#     print i
# print ""


# print corpus
# 每个文档转成词袋模型

tfidf = models.TfidfModel(corpus)
# tfidf.save("tfidf_AHTM")

corpus_tfidf = tfidf[corpus]
print "corpus_tfidf: \n"
print corpus_tfidf

lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=39)
# lda2 = models.LdaSeqModelModel(corpus_tfidf, id2word=dic, num_topics=70)

lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=70)
# lda.save('')

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

#
# corpus_lda = lda[corpus_tfidf]

print "LDA results:"
for i in range(0, 39):
    print lda.print_topic(i, 10)

# lsi_topic
print "LSA results:"
for i in range(0, 32):
    # print lsi.print_topic(i, 10)
    print i
    for j in lsi.show_topic(i, 10):
        print j[0],



# for doc in lsa:
#     print doc


# data1 = pyLDAvis.prepare(lda, corpus_tfidf, dic)
# pyLDAvis.save_html(data1, '.ldavis.html')
# pyLDAvis.prepared_data_to_html(data1)



"""
app.title = '笛卡尔坐标系上的热力图';

var hours = ['1', '2', '3', '4', '5', '6', '7',
        '8', '8a', '9a','10a','11a',
        '12p', '1p', '2p', '3p', '4p', '5p',
        '6p', '7p', '8p', '9p', '10p', '11p'];
var days = ['1', '2', '3',
        'Wednesday', 'Tuesday', 'Monday', 'Sunday'];

var data = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1],[4,0,1],[4,1,3],[4,2,0],[4,3,0],[4,4,0],[4,5,1],[4,6,0],[4,7,0],[4,8,0],[4,9,2],[4,10,4],[4,11,4],[4,12,2],[4,13,4],[4,14,4],[4,15,14],[4,16,12],[4,17,1],[4,18,8],[4,19,5],[4,20,3],[4,21,7],[4,22,3],[4,23,0],[5,0,2],[5,1,1],[5,2,0],[5,3,3],[5,4,0],[5,5,0],[5,6,0],[5,7,0],[5,8,2],[5,9,0],[5,10,4],[5,11,1],[5,12,5],[5,13,10],[5,14,5],[5,15,7],[5,16,11],[5,17,6],[5,18,0],[5,19,5],[5,20,3],[5,21,4],[5,22,2],[5,23,0],[6,0,1],[6,1,0],[6,2,0],[6,3,0],[6,4,0],[6,5,0],[6,6,0],[6,7,0],[6,8,0],[6,9,0],[6,10,1],[6,11,0],[6,12,2],[6,13,1],[6,14,3],[6,15,4],[6,16,0],[6,17,0],[6,18,0],[6,19,0],[6,20,1],[6,21,2],[6,22,2],[6,23,6]];

data = data.map(function (item) {
    return [item[1], item[0], item[2] || '-'];
});

option = {
    tooltip: {
        position: 'top'
    },
    animation: false,
    grid: {
        height: '50%',
        y: '10%'
    },
    xAxis: {
        type: 'category',
        data: hours,
        splitArea: {
            show: true
        }
    },
    yAxis: {
        type: 'category',
        data: days,
        splitArea: {
            show: true
        }
    },
    visualMap: {
        min: 0,
        max: 10,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: '15%'
    },
    series: [{
        name: 'Punch Card',
        type: 'heatmap',
        data: data,
        label: {
            normal: {
                show: true
            }
        },
        itemStyle: {
            emphasis: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }]
};
"""




