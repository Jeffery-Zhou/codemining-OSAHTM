# coding:utf-8
import


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

