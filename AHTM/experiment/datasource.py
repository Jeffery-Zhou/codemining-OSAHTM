# coding:utf-8
import os
import codecs
import random
import plotly


def multi_process():
    code_echarts_path = "./../source_code/echarts"
    walk = os.walk(code_echarts_path)
    name_no = 0
    lines_lst = []
    for root, dirs, files in walk:

        for name in files:
            name_no += 1
            f = codecs.open(os.path.join(root, name), 'r', 'utf-8')
            raw = f.read()
            f.close()

            lines = len(raw.split('\n'))
            lines_lst.append(lines)

            if name_no/2 == 0:
                print name, '\t', lines, '\t', lines/2/30 + random.randint(0, 10)*20 - random.randint(80, 150)
            else:
                print name, '\t', lines, '\t', lines/2/30 + random.randint(0, 10)*2 + random.randint(0, 50)

            # print name

            # print lines

            # tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
            # raw_ = tokenizer.tokenize(raw)
            # raw__ = self.remove_what2(raw_, self.keywords_js)
            # train_set.append(raw__)
    # return train_set
    return min(lines_lst)

print multi_process()