# -*- coding: utf-8 -*-
# import modules & set up logging
import gensim, logging
import os
from gensim.models.word2vec import LineSentence
from gensim.models import word2vec
from gensim import utils
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

number_iter = 1
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

jsonPath = '/home/ksoo/Downloads/scrapy_sample/scrapy_sample/corpus/'
saveModelName = 'gensimdata'
sentences = LineSentence(jsonPath + 'cp_copy.json')
try:
        model = word2vec.Word2Vec.load(saveModelName + '.model')
except:
        print "새로 학습"
        
        model = word2vec.Word2Vec(size=30, window = 8, workers=8)
        model.build_vocab(sentences)

ss = utils.RepeatCorpusNTimes(sentences, number_iter)
model.train(ss)

model.save(saveModelName + '.model')
model.save_word2vec_format(saveModelName + '.bin', binary=True)



