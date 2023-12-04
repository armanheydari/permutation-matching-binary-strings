from four_russian_trick import ones


def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    result = False
    pattern_ones = ones(pattern)
    for i in range(n - m + 1):
        if ones(text[i:i + m]) == pattern_ones:
            result = True
    return result
