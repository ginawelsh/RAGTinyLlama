import os
import nltk
from nltk import WordPunctTokenizer
import pandas as pd

def extract_files():
    """convert text data into document ID and token list key-value pairs"""
    dct = {}
    punctuation = ",!'.()"
    tk = WordPunctTokenizer()
    for file in os.listdir(path="group_project/text_data"):
            if file.endswith(".clean"):
                f = open(os.path.join("group_project/text_data", file), encoding="latin-1")
                file_name = file
                file_contents = f.read()
                tokens = [token.lower() for token in tk.tokenize(file_contents) if token not in punctuation]
                dct[file_name] = tokens
                with open("group_project/corpus_dct.txt", "a") as created_file:
                    created_file.write(str(dct))
                    print(f"{file_name} added to corpus")
    print("corpus created")
    return

def calculate_tf_idf():
     """
To calculate the TF-IDF score for a term in a document, we need to multiply the
 term frequency (TF) by the inverse document frequency (IDF):
TF-IDF(t, d) = TF(t, d) * IDF(t)
	1. Term Frequency (TF) is calculated as the number of times a term (t) appears in document (d) divided by the total number of terms in that document:
TF(t, d) = count(t, d) / total_terms(d)
	2. Inverse Document Frequency (IDF) measures the importance of a term across the entire document collection. It is calculated as the logarithm of the total number of documents (N) divided by the number of documents containing the term (n_t):
IDF(t) = log(N / n_t)

     
     """
     return

def process_query():
     return 

def main():
     return

if __name__ == '__main__':
    extract_files()