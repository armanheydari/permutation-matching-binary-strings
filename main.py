from dataset import generate_dataset, write_labels, load_dataset
from sub_quadratic import sub_quadratic
from table_lookup import table_lookup
from four_russian_trick import four_russian_trick
import time

if __name__ == '__main__':
    generate_dataset(100)
    data = load_dataset()[1:]
    sub_quadratic_results, table_lookup_results, four_russian_trick_results = [], [], []
    sub_quadratic_time, table_lookup_time, four_russian_trick_time = 0, 0, 0
    flag = True
    # Iterate samples and call each of the algorithms for each sample
    for i, row in enumerate(data):
        t = time.time()
        # Save the result for each algorithm to compare
        sub_quadratic_results.append(sub_quadratic(row[0], row[1]))
        # Save the running time for each algorithm to compare
        sub_quadratic_time += (time.time() - t)

        t = time.time()
        table_lookup_results.append(table_lookup(row[0], row[1]))
        table_lookup_time += (time.time() - t)

        t = time.time()
        four_russian_trick_results.append(four_russian_trick(row[0], row[1]))
        four_russian_trick_time += (time.time() - t)
        # Check the compatibility of the results
        if sub_quadratic_results[i] != table_lookup_results[i] or sub_quadratic_results[i] != \
                four_russian_trick_results[i] or table_lookup_results[i] != four_russian_trick_results[i]:
            print(f"Row {i} is different")
            flag = False

    # Write the results in the csv files
    write_labels('table_lookup', table_lookup_results)
    write_labels('four_russian_trick', four_russian_trick_results)
    write_labels('sub_quadratic', sub_quadratic_results)

    if flag:
        print("Results of the algorithms are same.")

    print("sub quadratic algorithm time:", sub_quadratic_time)
    print("table lookup algorithm time:", table_lookup_time)
    print("sub quadratic algorithm time:", four_russian_trick_time)
