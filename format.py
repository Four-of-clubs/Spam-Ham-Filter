import csv

from collections import Counter
import re

# DON'T TOUCH THIS FILE

#TODO:
'''
- longest word length - [ ]
- shortest word length - [ ]
- number of exclamation marks - [ ]
'''

input_file_name = "cleaned_data.csv"
output_file_name = "formated_data.csv"
indicator_words = ["free", "now", "click", "here", "buy", "time", "offer"]
bag_of_words_size = 30      #how many of the most common words to use for measurements

def read_file(filepath):
    data = []
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skipping the header, the first row in our data is a column lable, so we remove it
        for row in csv_reader:
            data.append(row)
    return data

def write_file(data, filepath, header_row=None):
    with open(filepath, 'w', newline='') as file:
        csv_writer = csv.writer(file)

        # Write the header row if provided
        if header_row:
            csv_writer.writerow(header_row)

        # Write the data rows
        for row in data:
            csv_writer.writerow(row)

#thanks ChatGPT
def find_most_common_words(data, num_words):
    word_dict = Counter()
    
    # Iterate through each row in the data
    for row in data:
        body = row[2]
        
        # Use regex to extract words from the subject string
        words = re.findall(r'\b\w+\b', body)
        
        # Update the word count dictionary
        word_dict.update(words)

    # Get the most common words
    most_common_word_list = word_dict.most_common(num_words)

    return [word for word, count in word_dict.most_common(num_words)]

#thanks ChatGPT
def count_words(data, word_list):
    count_of_words_in_list = []

    # Iterate through each row in the data
    for row in data:
        body = row[2]

        # Use regex to extract words from the body string
        words_in_body = re.findall(r'\b\w+\b', body)

        # Count occurrences of each word in the word_list
        word_counts = {word: words_in_body.count(word) for word in word_list}

        # Append the word counts for the current row to the result list
        count_of_words_in_list.append(list(word_counts.values()))

    return count_of_words_in_list

#thanks ChatGPT
def find_num_words_in_subject(data):
    num_words_in_subject = []

    # Iterate through each row in the data
    for row in data:
        subject = row[1]

        # Use regex to extract words from the subject string
        words = re.findall(r'\b\w+\b', subject)

        # Update the count of words in the subject for the current row
        num_words_in_subject.append(len(words))

    return num_words_in_subject

#thanks ChatGPT
def find_num_words_in_body(data):
    num_words_in_body = []

    # Iterate through each row in the data
    for row in data:
        body = row[2]

        # Use regex to extract words from the subject string
        words = re.findall(r'\b\w+\b', body)

        # Update the count of words in the subject for the current row
        num_words_in_body.append(len(words))

    return num_words_in_body

#thanks ChatGPT
def find_average_word_length_in_body(data):
    avg_word_length = []

    # Iterate through each row in the data
    for row in data:
        body = row[2]

        # Use regex to extract words from the body string
        words = re.findall(r'\b\w+\b', body)

        # Calculate the average word length
        if words:
            average_length = sum(len(word) for word in words) / len(words)
        else:
            average_length = 0

        # Update the average word length for the current row
        avg_word_length.append(average_length)

    return avg_word_length

if __name__ == "__main__":
    data = read_file(input_file_name)

    most_common_word_list = find_most_common_words(data, bag_of_words_size)
    count_of_most_common_words = count_words(data, most_common_word_list)
    count_of_indicator_words = count_words(data, indicator_words)

    num_words_in_subject = find_num_words_in_subject(data)
    num_words_in_body = find_num_words_in_body(data)
    avg_word_length = find_average_word_length_in_body(data)


    print(most_common_word_list)

    #thanks ChatGPT
    numeric_data = [
        [
            row[0],         #label
            #row[1],         #subject
            #row[2],         #body
            num_words_in_subject[i],
            num_words_in_body[i],
            avg_word_length[i],
            *count_of_indicator_words[i],
            *count_of_most_common_words[i]
        ]
        for i,row in enumerate(data)
    ]

    header_row = [
        "Label",
        "Num Words in Subject",
        "Num Words in Body",
        "Avg Word Length in Body",
        *indicator_words,
        *most_common_word_list
    ]

    print(f"Number of Columns: {len(numeric_data[0])}")

    write_file(numeric_data , output_file_name, header_row = header_row)