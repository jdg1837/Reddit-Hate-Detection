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
src,dst = file_io.read_parameters(param_file)[6:8]

#gather data on stopwords and symbols to be ignored
from nltk.corpus import stopwords
stopwords.words('english')
stop_words = set(stopwords.words('english'))
punctuation = list(string.punctuation)
lemmatizer = WordNetLemmatizer()

syn = file_io.load_dict('syn.txt')
slurs = file_io.load_slurs('slurs')

for sub in subreddits:
    sub_data = []
    word_count = {}
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = src + '/' + sub.lower() + '_' + src + '_attack.json'
    file_io.set_output_file(output_file)
    slur_count_file = src + '/' + sub.lower() + '_' + src + '_tf.txt'

    for datum in comment_data:
        comment = datum['body']
        #tokenize listing, remove unwanted elements
        tokens = re.findall(r"[\w']+", comment)
        filtered_data = [w for w in tokens if not (w in stop_words or w in punctuation or w.isnumeric())]
        lemmatized_data = []

        for i in range(len(filtered_data)):
            tok = tokens[i].lower()
            tok = tok.replace(',','')
            if tok in syn:
                tok = syn[tok]
            tok = lemmatizer.lemmatize(tok)
            lemmatized_data.append(tok)    

        #count occurances of each word
        count = Counter(lemmatized_data)
        count = count.most_common()

        identities_attacked = []

        for pair in count:
            w = pair[0]
            c = pair[1]
            if w in slurs:
                identities_attacked.append(slurs[w])
                if w in word_count:
                    word_count[w] += c
                else:
                    word_count[w] = c

        datum['identities'] = identities_attacked
        sub_data.append(datum)

    data = {'data': sub_data}
    file_io.write(data)

    with open(slur_count_file,'w',encoding='utf-8') as f:
        for w in sorted(word_count, key=word_count.get, reverse=True):
            f.write('{},{},{}\n'.format(w,word_count[w],slurs[w]))          