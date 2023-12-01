import math
from four_russian_trick import ones, max_min_one_dp


def compare_left_right_characters(left, right):
    if left == '1' and right == '0':
        return -1
    elif left == '0' and right == '1':
        return 1
    return 0


def table_lookup(text, a):
    n = len(text)
    s = int(math.log2(n))
    temp1, temp2 = max_min_one_dp(text, a)
    C = {'initial_position_max_ones': temp1, 'initial_position_min_ones': temp2}
    # Fill the table
    for i in range(n):
        for window_size in range(a, a + s + 1):
            if window_size > i:
                window_ones = ones(text[:i + 1])
                # signature max number, signature min number, current ones number for each of the l values
                C[window_size] = (max(0, window_ones - C['initial_position_max_ones']),
                                  max(0, window_ones - C['initial_position_min_ones']),
                                  window_ones)
            else:
                signature_max, signature_min, windows_ones = C[window_size]
                window_ones = windows_ones + compare_left_right_characters(text[i - window_size], text[i])
                C[window_size] = (max(signature_max, window_ones - C['initial_position_max_ones']),
                                  min(signature_min, window_ones - C['initial_position_min_ones']),
                                  window_ones)
    return C
