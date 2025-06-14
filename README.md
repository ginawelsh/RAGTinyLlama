# Exploring Retrieval-Augmented Generation with TinyLlama
A repository for our group project in Uppsala University's course Information Retrieval (5LN712). 

Our project explores how well TinyLlama works in an information retrieval setting.

## Our key research questions:

Document retrieval: How does a RAG document retrieval pipeline with SBERT and TinyLlama compare to a simple baseline?

Answer generation: How does TinyLlama’s one-shot answer generation performance compare to that of its zero-shot performance?

## Data source
Kaggle's Question Answer Dataset (https://www.kaggle.com/datasets/rtatman/questionanswer-dataset) which contains:


1. 150 text files, each file corresponding to a topic (=150 topics), n words = 696229
2. 4000 question-answer pairs, each pair corresponding to a text file
3. A word count summary file (text_data_toc.csv), with the number of words in each text file

## Findings

- Document retrieval: TF-IDF baseline retrieved documents better than Chroma
- Answer generation: No distinct difference between the RAG with database and Zero-/One-Shot
- Further tests needed; different embedding model with chroma, combining evaluation methods, generating answers with larger models

## Author Contributions

Authors: Gina Welsh, Yanista Stoykova, Ida Nilsson. 
Gina implemented the TF-IDF baseline and conducted most of the background research for the study. Yanitsa implemented the code for the Zero- and One-Shot experiments. Ida implemented the classic RAG-pipeline.
