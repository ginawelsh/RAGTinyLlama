import os
import json
import math
import nltk
nltk.download('stopwords')
from nltk import WordPunctTokenizer
from nltk.stem.porter import *
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import collections
from sklearn.feature_extraction.text import TfidfVectorizer

# tokenize then stem - remove punctuation and stop words
# calculating idf 
# stem the words - having --> hav
# get vocabulary after preprocessing
# calculate idf after getting tokens 
# precompute the semantic vectors - chatbot should refer to stored values; need to think about how to store 
# open-source vectors that are being indexed by the baseline
# lexical vs semantic search


#def preprocess(corpus):
 #    doc_ids = list(corpus.keys())
  #   convert_corpus_contents = [' '.]


def tokenize(string_input):
     """tokenize input text data"""
     punctuation = ",!'.()"
     stemmer = PorterStemmer() # nltk stemmer
     tk = WordPunctTokenizer() # nltk tokenizer
     stops = set(stopwords.words('english'))
     tokens = [stemmer.stem(token.lower()) for token in tk.tokenize(string_input) if token not in punctuation and token not in stops]
     return tokens

def calculate_tf(term, document):
     tf = document.count(term)/len(document)
     return tf

def calculate_idf(term, corpus_dictionary):
     idf = math.log(1 + (len(corpus_dictionary)/(len([document for document in corpus_dictionary if term in corpus_dictionary[document]])+1)))
     return idf

def calculate_tf_idf(term, document, corpus_dictionary):
     """calculate tf_idf score for a given term and corpus"""
     tf = calculate_tf(term, document) #document.count(term)/len(document)
     idf = calculate_idf(term, corpus_dictionary) 
     tf_idf = tf * idf 
     return tf_idf

def create_corpus():
    """extract files and create a dictionary of each file and their contents"""
    corpus = dict()
    for file in os.listdir(path="group_project/text_data"):
            if file.endswith(".clean"):
                f = open(os.path.join("group_project/text_data", file), encoding="latin-1")
                file_name = file
                file_contents = f.read()
                tokens = tokenize(file_contents)
                corpus[file_name] = tokens
    return corpus

def create_vocabulary(corpus):
     """create unique set of tokens that occur across all documents in corpus"""
     vocabulary = set()
     for file in corpus:
          for token in corpus[file]:
               vocabulary.add(token)
     return sorted(vocabulary) # must be in order 

def document_vectorisation(corpus, vocabulary):
     """create vectorised versions of contents within documents across all corpus (in order to do cosine similarity with queries)"""
     # to do: precompute IDF values for the entire vocabulary
     # precompute TF values per document (not per token)
     # compute TF-IDF once per unique token in each doc
     idf_values = dict()
     # get term frequencies for vocabulary - save in dictionary 
     for item in vocabulary:
          # precompute idf values (fixed for whole vocabulary)
         idf_values[vocabulary] = calculate_idf(item, vocabulary) # {term: idf_value}, retrieve idf value by calling idf_values[term]
         vectorised_corpus = dict()
         for document in corpus:
              tf_values = dict() # tf calculation occurs within the document
              document_unique_vocabulary = set(corpus[document])
              for token in corpus[document]:
                   tf_idf_values = []
                   tf_idf_values.append(calculate_tf_idf(token, document, corpus))
     vector = np.array(tf_idf_values)
     vectorised_corpus[document] = vector
     return vectorised_corpus

def calculate_cosine_similiarity(doc_vector_a, doc_vector_b):
     """calculate cosine similarity in order to compare query vector with document vector"""
     co_sim = (doc_vector_a * doc_vector_b)/(len(doc_vector_a)*len(doc_vector_b))
     return co_sim

def process_query(user_query, corpus):
     """process user query - tokenize, then calculate tf_idf"""
     tokens = tokenize(user_query) # apply same tokeizer used on corpus data
     query_vector = np.array([calculate_tf_idf(i, tokens, corpus) for i in tokens]) # revise this?
     return query_vector

def main():
     corpus = create_corpus() # {key = document_id: value = tokenised contents of document}
     print("corpus created")
     vocabulary = create_vocabulary(corpus) # create unique set of terms that occur across all documents, n = 42,729
     print("vocabulary created")
     # idf_values = {term: calculate_idf(term, corpus) for term in vocabulary} # calculate and store one IDF value per vocab term
     print("idf_values created")
     #inverted_index = {term: [] for term in vocabulary}
    # document_norms = {}

     """
     for document, tokens in corpus.items():
          print("this loop")
          tf_counts = collections.Counter(tokens)
          document_len = len(tokens)
          norm_squared = 0.0 # initialise document norm
          for term, count in tf_counts.items():
               tf = count/document_len
               tf_idf = tf*idf_values[term]
               norm_squared = tf_idf**2
               inverted_index[term].append((document, tf_idf))
          document_norms[document] = math.sqrt(norm_squared)
     """

     print(tokenize("Did Horace Greenley lose in the presidential elections of 1872"))
     print(len(vocabulary))
     test1 = process_query("I got a lotsa apples", corpus)
     test2 = process_query("Did Lincoln sign the National Banking Act of 1863?", corpus)
     #corpus_vectors = document_vectorisation(corpus)
     print(test2)

if __name__ == '__main__':
     main()