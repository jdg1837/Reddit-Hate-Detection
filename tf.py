import sys
import re
import nltk
from nltk.corpus import wordnet
import csv
import string
import file_io
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter

if len(sys.argv) < 2:
    print("Please include parameter file and API file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]

#gather data on stopwords and symbols to be ignored
from nltk.corpus import stopwords
stopwords.words('english')
stop_words = set(stopwords.words('english'))
punctuation = list(string.punctuation)
lemmatizer = WordNetLemmatizer()

syn = file_io.load_dict('syn.txt')
slurs = file_io.load_slurs('slurs')

for sub in subreddits:
    word_count = {}
    input_file = src + '/' + sub.lower() + '_' + src + '_comments.txt'
    output_file = src + '/' + sub.lower() + '_' + src + '_tf.txt'

    with open(input_file,'r',encoding='utf-8') as f:
        data = f.readlines()

    for datum in data:
        #tokenize listing, remove unwanted elements
        tokens = re.findall(r"[\w']+", datum)
        filtered_data = [w for w in tokens if not (w in stop_words or w in punctuation or w.isnumeric())]

        for i in range(len(tokens)):
            tok = tokens[i].lower()
            tok = tok.replace(',','')
            tok = lemmatizer.lemmatize(tok)
            if tok in syn:
                tok = syn[tok]
            tokens[i] = tok            

        #count occurances of each word, save (keyword,count) tuple in csv
        count = Counter(filtered_data)

        for w in count:
            c = count[w]
            if w in word_count:
                word_count[w] += c
            else:
                word_count[w] = c

    with open(output_file,'w',encoding='utf-8') as f:
        for w in sorted(word_count, key=word_count.get, reverse=True):
            if w in slurs:
                f.write('{},{},{}\n'.format(w,word_count[w],slurs[w]))          