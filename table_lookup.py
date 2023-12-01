import math
from four_russian_trick import ones, max_min_one_dp


def compare_left_right_characters(left, right):
    if left == '1' and right == '0':
        return -1
    elif left == '0' and right == '1':
        return 1
    return 0


def max_min_indexes(text, window_size, max_ones, min_ones):
    max_indexes, min_indexes = [], []
    for i in range(len(text)-window_size):
        if ones(text[i:i+window_size]) == max_ones:
            max_indexes.append(i)
        if ones(text[i:i+window_size]) == min_ones:
            min_indexes.append(i)
    return max_indexes, min_indexes


def table_lookup(text, a):
    n = len(text)
    s = int(math.log2(n))

    initial_max, initial_min = max_min_one_dp(text, a)
    initial_max_indexes, initial_min_indexes = max_min_indexes(text, a, initial_max, initial_min)
    C = {a: (initial_max, initial_min, initial_max_indexes, initial_min_indexes)}
    # Fill the table
    for window_size in range(a+1, a + s + 1):
        initial_max, initial_min, initial_max_indexes, initial_min_indexes = C[window_size-1]
        current_max, current_min, current_max_indexes, current_min_indexes = initial_max, initial_min+1, [], []
        flag = False
        for i in initial_max_indexes:
            try:
                if text[i+window_size-1] == '1':
                    current_max = initial_max + 1
                    current_max_indexes.append(i)
            except:
                flag = True
        if current_max == initial_max:
            if flag:
                temp = initial_max_indexes[-1]
                if temp - 1 not in initial_max_indexes:
                    initial_max_indexes[-1] = temp - 1
                else:
                    initial_max_indexes = initial_max_indexes[:-1]
            current_max_indexes = initial_max_indexes[:-1]

        flag = False
        for i in initial_min_indexes:
            try:
                if text[i+window_size-1] == '0':
                    current_min = initial_min
                    current_min_indexes.append(i)
            except:
                flag = True

        if current_min == initial_min + 1:
            if flag:
                temp = initial_min_indexes[-1]
                if temp - 1 not in initial_min_indexes:
                    initial_min_indexes[-1] = temp - 1
                else:
                    initial_min_indexes = initial_min_indexes[:-1]
                current_min_indexes = initial_min_indexes
        C[window_size] = current_max, current_min, current_max_indexes, current_min_indexes

    return C


print(table_lookup('0110101101010010', 3))
