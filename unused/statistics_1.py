import csv

#thanks ChatGPT
def count_csv_rows(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        row_count = sum(1 for row in csv_reader)
    return row_count

def calculate_average_word_count(csv_file, column_number):
    total_word_count = 0
    row_count = 0

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) > column_number:
                column_data = row[column_number]
                words = column_data.split()  # Split the column data into words
                word_count = len(words)      # Count the words in the column
                total_word_count += word_count
                row_count += 1

    if row_count == 0:
        return 0  # Avoid division by zero if there are no rows with data in the column

    average_word_count = total_word_count / row_count
    return average_word_count

import csv

def count_word_occurrences_in_column(csv_file, column_number, target_word):
    # Initialize a count variable
    count = 0

    # Convert the target word to lowercase
    target_word_lower = target_word.lower()

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            # Check if the column number is within the bounds of the row
            if len(row) > column_number:
                column_data = row[column_number]
                # Convert the column data to lowercase
                column_data_lower = column_data.lower()
                # Split the column data into words using whitespace as the delimiter
                words = column_data_lower.split()
                # Increment the count for each occurrence of the target word
                count += words.count(target_word_lower)

    return count


if __name__ == "__main__":
    print("STATISTICS\n")
    ham_file = 'ham.csv'
    spam_file = 'spam.csv'

    num_ham_rows = count_csv_rows(ham_file)
    num_spam_rows = count_csv_rows(spam_file)

    print(f"number of Ham emails {num_ham_rows}")
    print(f"number of Spam emails {num_spam_rows}")
    print("~"*20)

    print(f"Average word in Ham Subject: {calculate_average_word_count(ham_file, 0):.3f}")
    print(f"Average word in Spam Subject: {calculate_average_word_count(spam_file, 0):.3f}")
    print("~"*20)

    print(f"Average word in Ham Message: {calculate_average_word_count(ham_file,1):.3f}")
    print(f"Average word in Spam Message: {calculate_average_word_count(spam_file,1):.3f}")
    print("~"*20)

    word_list = ["free", "you", "miss", "here"]
    for word in word_list:

        print(f"The number of Times \"{word}\" occured")
        ham_occurances = count_word_occurrences_in_column(ham_file, 1, word)
        spam_occurances = count_word_occurrences_in_column(spam_file, 1, word)
        print(f"\tHam: {ham_occurances} with a rate of {ham_occurances/num_ham_rows:.3f}")
        print(f"\tSpam: {spam_occurances} with a rate of {spam_occurances/num_spam_rows:.3f}")
        if(ham_occurances/num_ham_rows > spam_occurances/num_spam_rows):
            print(f"\tHam was {(ham_occurances/num_ham_rows) / (spam_occurances/num_spam_rows):.3f} as often")
        else:
            print(f"\tSpam was {(spam_occurances/num_spam_rows) / (ham_occurances/num_ham_rows):.3f} as often")
        print()
