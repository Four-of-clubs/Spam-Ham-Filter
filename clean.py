import csv
import re
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

# Download stopwords resource
nltk.download('stopwords')
# Download WordNet resource
nltk.download('wordnet')
#TODO:
'''
- Removing numbers (optional) - [X]
- Removing Hyperlinks - [X]
- Cleaning non-alphabetical and numerical characters (removing punctuation) - [X]
- Word Stemming (totally optional, and probably not worth it) - [ ]
- Lemmatizing - [X]
'''

input_file_name = "spam_ham_dataset.csv"
output_file_name = "cleaned_data.csv"

def read_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skipping the header, the first row in our data is a column lable, so we remove it
        for row in csv_reader:
            data.append(row)
    return data

def write_file(data, filepath):
    with open(filepath, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in data:
            csv_writer.writerow(row)

def reformat(data):
    '''This function reformats the data. If the origional column order is 0,1,2,3 it becomes 3,2 (and removes the first two columns)
    thus we are left with just the label and text of the email'''
    new_data = []
    for row in data:
        lable = row[3]
        text_body = row[2]
        
        new_data.append([lable, text_body])

    return new_data

def seperate_subject_and_body(data):
    '''seperaets the subject and body into two seperate columns. Assumes text data in col 1 and puts subject in 1 and body in 2'''
    new_data = []
    for row in data:
        label = row[0]

        text = row[1]
        subject = text.split('\n', 1)[0][9:]    #splits on new_line, and cuts off first 9 characters ("Subject: ")
        message = text.split('\n', 1)[1]        #splits on new_line, takes second half

        new_data.append([label, subject, message])

    return new_data

def example_mess_with_data(data):
    new_data = []
    for row in data:
        label = row[0] #don't mess with this
        subject = clean_data(row[1]) #mess with this if you want
        body = clean_data(row[2]) #DO mess with this


        new_data.append([label, subject, body])

    return new_data
    
def clean_data(text):
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove hyperlinks
    text = re.sub(r'http\S+', '', text)
    
    # Remove special characters (except for letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Lemmatize
    lemma = WordNetLemmatizer()
    text = ' '.join(lemma.lemmatize(word) for word in text.split())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word.lower() not in stop_words)
    return text

if __name__ == "__main__":
    data = read_file(input_file_name)
    data = reformat(data)
    data = seperate_subject_and_body(data)

    data = example_mess_with_data(data)


    write_file(data, output_file_name)
