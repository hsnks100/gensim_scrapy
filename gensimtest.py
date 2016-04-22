# -*- coding: utf-8 -*-

import gensim, logging
import os
import time
# def MySentences(fname):
    # for line in open(fname):
        # yield line.split()

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

model = gensim.models.Word2Vec.load_word2vec_format('gensimdata.bin', binary=True, encoding='utf-8')  # C binary format
print "============== " + str(time.asctime()) + "============="
# print "-----------------------------------------------------------------------------------------------"
print "print model.similarity(u'나라/Noun', u'이탈리아/Noun')"
print "\t", model.similarity(u'나라/Noun', u'이탈리아/Noun')
print "print model.similarity(u'나라/Noun', u'프로그램/Noun')"
print "\t", model.similarity(u'나라/Noun', u'프로그램/Noun')
print "print model.doesnt_match(u'프로그래밍/Noun 언어/Noun 아이스크림/Noun 컴파일러/Noun 모니터/Noun'.split())"
print "\t", model.doesnt_match(u'프로그래밍/Noun 언어/Noun 아이스크림/Noun 컴파일러/Noun 모니터/Noun'.split()).encode('utf-8')

# # print model.similarity('girl', 'woman')
# print "부산대에 관한 유사도"
# for  i in model.most_similar(u'부산대'):
	# print "\t", i[0], i[1]
keyword = u'컴파일러/Noun'
print (keyword + u" 유사도(most_similar)").encode('utf-8')
for  i in model.most_similar(keyword, topn=20):
	print "\t", i[0].encode('utf-8'), i[1]
print "-----------------------------------------------"
print "model.most_similar(positive=[u'여자/Noun', u'왕/Noun'], negative=[u'남자/Noun']):" 
for i in model.most_similar(positive=[u'여자/Noun', u'왕/Noun'], negative=[u'남자/Noun']):
        print "\t", i[0].encode('utf-8'), i[1]
print "model.most_similar(positive=[u'컴퓨터/Noun', u'언어/Noun']):" 
for i in model.most_similar(positive=[u'컴퓨터/Noun', u'언어/Noun']):
        print "\t", i[0].encode('utf-8'), i[1]


