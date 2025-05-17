import os
import json
import math
from nltk import WordPunctTokenizer
import pandas as pd
import numpy as np


def tokenize(string_input):
     """tokenize input text data"""
     punctuation = ",!'.()"
     tk = WordPunctTokenizer()
     tokens = [token.lower() for token in tk.tokenize(string_input) if token not in punctuation]
     return tokens

def calculate_tf_idf(term, document, corpus_dictionary):
     """calculate tf_idf score for a given term and corpus"""
     tf = document.count(term) / len(document)
     idf = math.log(1 + (len(corpus_dictionary)/(len([document for document in corpus_dictionary if term in corpus_dictionary[document]])+1)))
     tf_idf = tf * idf 
     return tf_idf

def create_corpus():
    """extract files and create a dictionary of each file and their contents"""
    corpus = {}
    for file in os.listdir(path="group_project/text_data"):
            if file.endswith(".clean"):
                f = open(os.path.join("group_project/text_data", file), encoding="latin-1")
                file_name = file
                file_contents = f.read()
                tokens = tokenize(file_contents)
                corpus[file_name] = tokens
    return corpus


def calculate_cosine_similiarity(doc_vector_a, doc_vector_b):
     """calculate cosine similarity in order to compare query vector with document vector"""
     co_sim = (doc_vector_a * doc_vector_b)/(len(doc_vector_a)*len(doc_vector_b))
     return co_sim

def process_query(user_query, corpus):
     tokens = tokenize(user_query)
     query_vector = np.array([calculate_tf_idf(i, tokens, corpus) for i in tokens])
     return query_vector

def main():
     corpus = create_corpus()
     test1 = process_query("I got a lotsa apples", corpus)
     test2 = process_query("Did Lincoln sign the National Banking Act of 1863?", corpus)
     print(test2)

if __name__ == '__main__':
     main()