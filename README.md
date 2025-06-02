# Information Retrieval Group Project
A repository for our Information Retrieval Group Project (the ChatBot Baddies). In this project, we explore how well TinyLlama works for Retrieval-Augmented Generation.

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
