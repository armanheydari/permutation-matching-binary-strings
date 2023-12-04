from four_russian_trick import ones


def max_min_one_dp(text, l):
    n = len(text)
    w = text[:l]
    w_ones = ones(w)
    max_ones, min_ones = w_ones, w_ones
    for i in range(1, n - l + 1):
        temp = 0
        w = text[i:i + l]
        if text[i - 1] == '0' and text[i + l - 1] == '1':
            temp = 1
        elif text[i - 1] == '1' and text[i + l - 1] == '0':
            temp = -1
        w_ones = w_ones + temp
        max_ones = max(max_ones, w_ones)
        min_ones = min(min_ones, w_ones)

    return max_ones, min_ones


def dynamic_programming(text, pattern):
    m = len(pattern)
    max_ones, min_ones = max_min_one_dp(text, m)
    pattern_ones = ones(pattern)
    if max_ones > min_ones + 1 and max_ones >= pattern_ones >= min_ones:
        return True
    elif pattern_ones == max_ones or pattern_ones == min_ones:
        return True
    return False


dynamic_programming('0001110010', '01100')
