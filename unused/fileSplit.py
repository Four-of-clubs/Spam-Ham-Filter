import csv

#ignore this file

#thanks ChatGPT
def split_csv_by_column_value(input_file, output_file_0, output_file_1):
    ''' This function can be used to split a csv by a lable column - can turn one dataset into one file of spam and one file of ham'''
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read and store the header

        with open(output_file_0, 'w', newline='') as file_0:
            with open(output_file_1, 'w', newline='') as file_1:
                csv_writer_0 = csv.writer(file_0)
                csv_writer_1 = csv.writer(file_1)

                for row in csv_reader:
                    # Assuming column 4 is at index 3 (0-based)
                    column_4_value = int(row[3])
                    text = row[2]

                    subject = text.split('\n', 1)[0][9:]
                    message = text.split('\n', 1)[1]

                    if column_4_value == 0:
                        csv_writer_0.writerow([subject, message])
                    elif column_4_value == 1:
                        csv_writer_1.writerow([subject, message])

if __name__ == "__main__":
    split_csv_by_column_value('spam_ham_dataset.csv', 'ham.csv', 'spam.csv')