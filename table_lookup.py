import math
from four_russian_trick import ones
from dynamic_programming import max_min_one_dp


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
            max_indexes.append((i, i+window_size))
        if ones(text[i:i+window_size]) == min_ones:
            min_indexes.append((i, i + window_size))
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

        for start, end in initial_max_indexes:
            if start > 0 and text[start-1] == '1':
                current_max = initial_max + 1
                current_max_indexes.append((start-1, end))
            if end < n and text[end] == '1':
                current_max = initial_max + 1
                current_max_indexes.append((start, end+1))
        if current_max == initial_max:
            current_max_indexes = max_min_indexes(text, window_size, current_max, current_min)[0]

        for start, end in initial_min_indexes:
            if start > 0 and text[start-1] == '0':
                current_min = initial_min
                current_min_indexes.append((start-1, end))
            if end < n and text[end] == '0':
                current_min = initial_min
                current_min_indexes.append((start, end+1))
        if current_min == initial_min+1:
            current_min_indexes = max_min_indexes(text, window_size, current_max, current_min)[1]

        C[window_size] = current_max, current_min, list(set(current_max_indexes)), list(set(current_min_indexes))

    return C
