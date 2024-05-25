import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def lower_Con(filedata):
    return filedata.lower()

exclude = "!#&\'()*+,-/:;<=>?[\\]^_`{|}~·0123456789%" # dollar,at,percent

def remove_punc(text):
    return text.translate(str.maketrans('', '', exclude))


next = '\n'
space = ' '
def remove_punc1(text):
    return text.translate(str.maketrans(next, space * len(next)))


def remove_stopwords(text):
    new_text = []
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)

ps = PorterStemmer()
def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])

def preprocess(filedata):
    filedata = lower_Con(filedata)
    filedata = remove_punc1(filedata)
    filedata = remove_punc(filedata)
    filedata = remove_stopwords(filedata)
    filedata = stem_words(filedata)
    return filedata


def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

plagiarism_results = set()

def check_plagiarism(text_vector_b, text_vector_a):
    sim_score = similarity(text_vector_b, text_vector_a)[0][1]
    score = (sim_score)
    new_score = score*100
    precision = 2
    precent_simi = format(new_score, f'.{precision}f')  
    return precent_simi
