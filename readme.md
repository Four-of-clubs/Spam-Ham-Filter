SPAM OR HAM
========================
Origional Data: spam_ham_dataset.csv (1=spam, 0=ham)

From: https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset?select=completeSpamAssassin.csv

# TODO

https://towardsdatascience.com/email-spam-detection-1-2-b0e06a5c0472
https://www.kaggle.com/code/puding6x6/filtering-spam-e-mails-power-of-naive-baye-4b7070 
## Cleaning Data
- Convert all characters to lowercase  - [x]
- Removing numbers - [X]
- Removing Hyperlinks - [X] (ish)
- Cleaning non-alphabetical and numerical characters (removing punctuation) - [X]
- Word Stemming - [X]
- Lemmatizing - [X]


## Formating Data
- num words in subject - [X]
- num words in message - [X]
- average word length - [X]
- number of our 5 indicator words - [X]
- number of the 30 most common words - [X]

## Build Models
- Neural Network - [x]
- Naive Bayse - [X]

I struggled to find good resources to implement Naive Bayse, but chatGPT is a godsend here
prompt like:
write me python code to run naive bayse algorithm on a csv file where the first column is the lable (1=spam, 0 = ham) and columns 1-15 are some sort of numeric data

Project Paper/Writeup:
https://docs.google.com/document/d/1SWEeWRDbxG5Hx476MlMTuFZFrfPs7dQBvcWofx4etME/edit

Notes Doc:
https://docs.google.com/document/d/1_AYqfDkDcg-ANJG1D0ioVEE7hKIubpQxwNx4qPhyh7E/edit

Naive Bayes Colab:
https://colab.research.google.com/drive/1GJ__zDnE89heQVGQLpjKitrCjm1gHBCm?usp=sharing

Neural Net Colab:
https://colab.research.google.com/drive/1ew7swnpD-3XXSnolG7HLeqb5_aESgKs3?usp=sharing#scrollTo=UnfFfuaQoh4B
