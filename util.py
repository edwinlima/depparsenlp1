# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:51:47 2016

@author: edwinlima
"""

# TUTORIAL WORD2VE: https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors

import numpy as np
import pandas as pd
from gensim.models import word2vec 
import gensim

def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as myfile:
        f = myfile.readlines()
        s_num = 0
        i =0
        word_s = []
        tag_s = []
        s  = []
        p = []
        for l in f:
            
            v = l.replace('\n','').split("\t")
            v.append(s_num)
            if len(l) != 1:
                data.append(v)
                print(v)
                s.append(v[1].lower())
                p.append(v[3])
                i +=1
            else:
                word_s.append(s)
                tag_s.append(p)
                s_num +=1
                s  = []
                p = []
        
    return data, word_s, tag_s

if __name__ == "__main__":
    data, words, tags = read_data('.//data//train-stanford-raw.conll')
    print('data=',data[:10])
    print('words sentences=', words[:10])
    print('tags sentences=', tags[:10])
    print("training word2vec model")
    model = word2vec.Word2Vec(words,size=189, min_count=1) # here moeten we wat tweaken met de parameters
    
    
    

        