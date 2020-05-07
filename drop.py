import pandas as pd
from googleapiclient import discovery
import json
import numpy as np
from collections import Counter
from nltk.corpus import stopwords
from nltk import word_tokenize
from string import punctuation
stoplist = set(stopwords.words('english') + list(punctuation))
df = pd.read_json('250k_data_toxicity_0.5/marvelstudios_250k_data_toxicity_0.5.json', orient='split')
#df.drop_duplicates(subset ="author", keep = False, inplace = True)
#print(df)
texts = df['body'].str.lower()
word_counts = Counter(word_tokenize('\n'.join(texts)))
print(word_counts)

#print(word_counts.most_common())
