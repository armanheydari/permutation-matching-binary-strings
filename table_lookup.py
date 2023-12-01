import math
from four_russian_trick import ones, max_one_dp


def compare_left_right_characters(left, right):
    if left == '1' and right == '0':
        return -1
    elif left == '0' and right == '1':
        return 1
    return 0


def table_lookup(text, a):
    n = len(text)
    s = int(math.log2(n))
    C = {'initial_position_max_ones': max_one_dp(text, a), 'initial_position_min_ones': min_one_dp(text, a)}
    # Fill the table
    for i in range(n):
        for window_size in range(a, a+s+1):
            if window_size>i:
                window_ones = ones(text[:i+1])
                # signature number, current_ones_number for each of the l values
                C[window_size] = (max(0, window_ones-initial_position_max_ones), window_ones)
            else:
                signature_max, windows_ones = C[window_size]
                window_ones = windows_ones + compare_left_right_characters(text[i-window_size], text[i])
                C[window_size] = (max(signature_max, window_ones - initial_position_max_ones), window_ones)
    return C



table_lookup('0110101101010010', 3)

