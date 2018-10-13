"""
Text mining and analyzing module. 

What you can do -

- Morphological analysis
- Categorying documents
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.corpus import gutenberg
nltk.download("gutenberg")
import pprint
pp = pprint.PrettyPrinter(indent=4)
stemmer = PorterStemmer()


def corpus_list():
    """Get corpus data

    Return
    ------
    corpus_data: dict
        {
            "file_id": file_id, 
            "word_num": word_num, 
            "sent_num": sent_num, 
            "raw_text": raw_text
        }
    """

    corpus_data = []
    for file_id in gutenberg.fileids():
        raw_text = gutenberg.raw(file_id)
        word_num = len(gutenberg.words(file_id))
        sent_num = len(gutenberg.sents(file_id))
        d = {
            "file_id": file_id,
            "word_num": word_num,
            "sent_num": sent_num,
            "raw_text": raw_text,
        }
        corpus_data.append(d)

    return corpus_data


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


def tf_idf(tokens):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(tokens)
    return tfs


def clustering_text(docs, cluster_num=10):
    """Clustering text document with KMeans algorithm.

    Parameters
    ----------
    docs : list
        Documents to be clustering. 

    cluster_num : integer
        Number of cluster to create. 

    Return
    ------
    result : list
        [
            {"label": label, "value": value},
            {"label": label, "value": value},
            {"label": label, "value": value},
            ...
        ]
    """

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    vecs = tfidf.fit_transform(docs)

    k_model = KMeans(n_clusters=cluster_num).fit(vecs)

    results = []
    for label, value in zip(k_model.labels_, docs):
        label_value = {"label": label, "value": value}
        results.append(label_value)

    return results


if __name__ == '__main__':
    corpora = corpus_list()

    raw_texts = []
    for corpus in corpora:
        raw_texts.append(corpus["raw_text"])

    clustering_result = clustering_text(raw_texts, cluster_num=10)
    show_result(clustering_result)
