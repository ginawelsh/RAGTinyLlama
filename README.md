# Information Retrieval Group Project
A repository for our Information Retrieval Group Project (the ChatBot Baddies). In this project, we explore the performance of three major LLMs in their improvement of an IR system (compared to a baseline).

## Our research question

We will be comparing the performance of Large Language Models (LLMs) for Retrieval Augmentation Generation (RAG), a task which retrieves and incorporates relevant documentation into a generated answer for a user's query. We will compare their performance to a baseline IR system that uses TF-IDF. 

## Data source
We will use Kaggle's Question Answer Dataset (https://www.kaggle.com/datasets/rtatman/questionanswer-dataset) which contains:
    1. 150 text files, each file corresponding to a topic (=150 topics)
    2. 4000 question-answer pairs, each pair corresponding to a text file
    3. A word count summary file (text_data_toc.csv), with the number of words in each text file
