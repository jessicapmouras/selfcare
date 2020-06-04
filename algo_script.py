#general imports
import numpy as np
import pandas as pd


import unicodedata
import string
import re

#sklearn imports
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


#nltk imports
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import  SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

stop = stopwords.words('english')
stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()

np.set_printoptions(linewidth=100)

sw = stopwords.words('english')
pt = string.punctuation
stemmer = SnowballStemmer('english')

import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
import numpy as np
import re

from similarity.jarowinkler import JaroWinkler
from similarity.cosine import Cosine

#clean inital dataframe input
testingdf = pd.read_csv('data/training.csv')
testingdf.set_index(['Product'], inplace=True)
testingdf.dropna(inplace=True)
testingdf.info()


def select_category(df, category):
    return df.loc[df['Category'] == category]

#input text function

def user_input(df, tags):
    """INPUT: df > resulting dataframe from select category function
        tags > user enters in a string of words 6 total from a
        from a dropdown list"""
    """OUTPUT: dataframe with column of input tags """
    
    df.loc[df.UserInput < 1, 'UserInput'] = str(tags)
    df['UserInput'] = df['UserInput'].astype("string")
    df['Tags2'] = df['Tags2'].astype("string")
    
    return df

def jw(df):
    jarowinkler = JaroWinkler()
    df["jarowinkler_sim"] = [jarowinkler.similarity(i,j) for i,j in zip(df["Tags2"],df["UserInput"])]
    df.sort_values(by=['jarowinkler_sim'], inplace=True, ascending=False)
    final = df.drop(['Category','ReviewText2', 'Tags2'], axis=1).iloc[:5,:]
    
    
    return final

# tags = input("Input your tags: ")