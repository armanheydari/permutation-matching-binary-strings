import random
import csv


def generate_binary_string(length):
    # Appending a random integer (either 0 or 1) to the string for each iteration of the loop
    binary_string = ""
    for i in range(length):
        binary_string += str(random.randint(0, 1))
    return binary_string


def generate_dataset(number_of_samples, maximum_length=100):
    with open('dataset.csv', mode='w', newline='') as file:
        # Write the data to a CSV file
        writer = csv.writer(file)
        writer.writerow(['text', 'pattern'])
        for i in range(number_of_samples):
            # Determine the length of the binary text
            text_length = random.randint(1, maximum_length)
            # Determine the length of the binary pattern, pattern should be shorter than the text
            pattern_length = random.randint(1, text_length)
            writer.writerow([generate_binary_string(text_length), generate_binary_string(pattern_length)])


def load_dataset():
    data = []
    # Open the CSV file
    with open('dataset.csv', mode='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Iterate over each row in the CSV file
        data = [row for row in reader]
    return data


def write_labels(column_name, algorithm_results):
    # Read the csv file into a list
    data = load_dataset()
    # Append the results as a new column to the list
    data[0].append(column_name)
    for i in range(1, len(data)):
        data[i].append(algorithm_results[i-1])
    # Write the data to the CSV file again
    with open('dataset.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)