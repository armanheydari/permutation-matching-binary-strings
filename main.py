import math
from dataset import generate_dataset, write_labels, load_dataset, generate_binary_string
from brute_force import brute_force
from table_lookup import table_lookup
from four_russian_trick import four_russian_trick
from dynamic_programming import dynamic_programming, max_min_one_dp
import time


def four_russian_trick_comparison(sample_number, sample_length):
    four_russian_trick_time, dp_time = 0, 0
    for i in range(sample_number):
        random_binary = generate_binary_string(sample_length)
        t = time.time()
        res_1 = four_russian_trick(random_binary, 4)
        four_russian_trick_time += (time.time() - t)

        t = time.time()
        res_2 = max_min_one_dp(random_binary, 4)
        dp_time += (time.time() - t)

        if res_1 != res_2:
            print("The results are not match! something is wrong! results:", res_1, res_2)
            print("The sample, ", random_binary)
            break

        if i % 10 == 0:
            print('time for maxOne', four_russian_trick_time)
            print('time for maxOne_normal', dp_time)
            print('-------------')


def table_lookup_comparison(sample_number, sample_length):
    table_lookup_time, dp_time = 0, 0
    for i in range(sample_number):
        random_binary = generate_binary_string(sample_length)
        t = time.time()
        res_1 = table_lookup(random_binary, 4)
        table_lookup_time += (time.time() - t)

        for l in range(4, 4 + int(math.log2(sample_length)) + 1):
            t = time.time()
            res_2 = max_min_one_dp(random_binary, l)
            dp_time += (time.time() - t)
            temp1, temp2, temp3, temp4 = res_1[l]
            if (temp1, temp2) != res_2:
                print("The results are not match! something is wrong! for l=", l, "results:", temp1, temp2, res_2)
                # print("The sample, ", random_binary)
                break

        if i % 10 == 0:
            print('time for table_lookup', table_lookup_time)
            print('time for simple dynamic programming', dp_time)
            print('-------------')


if __name__ == '__main__':
    generate_dataset(100, 100000)
    data = load_dataset()[1:]
    brute_force_results, dynamic_programming_results, four_russian_trick_results = [], [], []
    brute_force_time, dynamic_programming_time, four_russian_trick_time = 0, 0, 0
    flag = True
    # Iterate samples and call each of the algorithms for each sample
    for i, row in enumerate(data):
        t = time.time()
        # Save the result for each algorithm to compare
        brute_force_results.append(brute_force(row[0], row[1]))
        # Save the running time for each algorithm to compare
        brute_force_time += (time.time() - t)

        t = time.time()
        dynamic_programming_results.append(dynamic_programming(row[0], row[1]))
        dynamic_programming_time += (time.time() - t)

        t = time.time()
        four_russian_trick_results.append(four_russian_trick(row[0], row[1]))
        four_russian_trick_time += (time.time() - t)
        # Check the compatibility of the results
        if brute_force_results[i] != dynamic_programming_results[i] or brute_force_results[i] != \
                four_russian_trick_results[i] or dynamic_programming_results[i] != four_russian_trick_results[i]:
            print(f"Row {i} is different")
            flag = False

        if i % 5 == 0:
            print("brute force algorithm time:", brute_force_time)
            print("dynamic programming algorithm time:", dynamic_programming_time)
            print("four russian trick algorithm time:", four_russian_trick_time)

    # Write the results in the csv files
    write_labels('brute_force', brute_force_results)
    write_labels('dynamic_programming', dynamic_programming_results)
    write_labels('four_russian_trick', four_russian_trick_results)

    if flag:
        print("Results of the algorithms are same.")

    print("brute force algorithm time:", brute_force_time)
    print("dynamic programming algorithm time:", dynamic_programming_time)
    print("four russian trick algorithm time:", four_russian_trick_time)

    # four_russian_trick_comparison(100, 100000)
    # table_lookup_comparison(100, 100000)
