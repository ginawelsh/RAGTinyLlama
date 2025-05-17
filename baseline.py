import os
import json
import math
from nltk import WordPunctTokenizer
import pandas as pd


def tokenize(string_input):
     """tokenize input text data"""
     punctuation = ",!'.()"
     tk = WordPunctTokenizer()
     tokens = [token.lower() for token in tk.tokenize(string_input) if token not in punctuation]
     return tokens

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

def calculate_tf_idf(term, corpus_dictionary):
     """calculate tf_idf score for a given term and corpus"""
     tf_idfs = {}
     for document in corpus_dictionary:
          tf = corpus_dictionary[document].count(term) / len(corpus_dictionary[document])
          idf = math.log(len(corpus_dictionary) / len([document for document in corpus_dictionary if term in corpus_dictionary[document]])+1)
          tf_idf = tf * idf 
          tf_idfs[document] = tf_idf
     return tf_idfs

def process_query(user_query):
     tokens = tokenize(user_query)
     return tokens

def main():
     return

if __name__ == '__main__':
    corpus = create_corpus()
    print(calculate_tf_idf('how', corpus))
    consensus = calculate_tf_idf('consensus', corpus)
    ranked_term = sorted([(consensus[c],c) for c in consensus if consensus[c] > 0], reverse=True)
    print(ranked_term)
    