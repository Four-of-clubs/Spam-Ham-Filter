SPAM OR HAM
========================
Origional Data: spam_ham_dataset.csv (1=spam, 0=ham)

From: https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset?select=completeSpamAssassin.csv

# TODO

https://towardsdatascience.com/email-spam-detection-1-2-b0e06a5c0472
https://www.kaggle.com/code/puding6x6/filtering-spam-e-mails-power-of-naive-baye-4b7070 
## Cleaning Data
- Convert all characters to lowercase  - [x]
- Removing numbers (optional) - [ ]
- Removing Hyperlinks - [ ]
- Cleaning non-alphabetical and numerical characters (removing punctuation) - [ ]
- Word Stemming (totally optional, and probably not worth it) - [ ]
- Lemmatizing - [ ]


## Formating Data (potential list)
- num words in subject - [ ]
- num words in message - [ ]
- average word length - [ ]
- longest word length - [ ]
- shortest word length - [ ]
- number of exclamation marks - [ ]
- number of our 5 indicator words - [ ]
- number of the 10 most common words - [ ]

## Build Models
- Neural Network - [x]
- Naive Bayse - [ ]

I struggled to find good resources to implement Naive Bayse, but chatGPT is a godsend here
prompt like:
write me python code to run naive bayse algorithm on a csv file where the first column is the lable (1=spam, 0 = ham) and columns 1-15 are some sort of numeric data