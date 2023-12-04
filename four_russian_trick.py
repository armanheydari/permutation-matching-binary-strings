import math


# Function to count the number of '1's in a binary string
def ones(binary_string):
    return binary_string.count('1')


# Function to calculate the maximum value of k
def calculate_k_max(F, G):
    # If F is longer than G, pad G with '0's
    if len(F) > len(G):
        G += (len(F) - len(G)) * '0'
    max_k = 0
    k = 0
    # Iterate over the length of F
    for i in range(len(F)):
        # If the bits are the same, k remains the same
        if F[i] == G[i]:
            k += 0
        # If F has a '1' and G has a '0', decrement k
        elif F[i] == '1' and G[i] == '0':
            k -= 1
        # If F has a '0' and G has a '1', increment k
        elif F[i] == '0' and G[i] == '1':
            k += 1
        # Update max_k if k is greater
        max_k = max(max_k, k)
    return max_k


# Function to calculate the minimum value of k
def calculate_k_min(F, G):
    # If F is longer than G, pad G with '1's
    if len(F) > len(G):
        G += (len(F) - len(G)) * '1'
    min_k = 0
    k = 0
    # Iterate over the length of F
    for i in range(len(F)):
        # If the bits are the same, k remains the same
        if F[i] == G[i]:
            k += 0
        # If F has a '1' and G has a '0', decrement k
        elif F[i] == '1' and G[i] == '0':
            k -= 1
        # If F has a '0' and G has a '1', increment k
        elif F[i] == '0' and G[i] == '1':
            k += 1
        # Update min_k if k is smaller
        min_k = min(min_k, k)
    return min_k


# Function to implement the Four Russians trick
def max_min_one_frt(text, l):
    # Initialize values
    n = len(text)
    s = int(math.log2(n))
    A_max, A_min = {}, {}
    B = 0
    max_one_result, min_one_result = 0, n
    # If s is 0, return the count of '1's in text
    if s == 0:
        s = 1
    # Iterate over the text in chunks of size s
    for i in range(0, n-l+1, s):
        w = text[i:i + l]
        F = w[:s]
        G = text[i + l: i + l + s]
        B = ones(w)
        # If (F, G) is not in A, calculate k_max and k_min and assign in A
        if (F, G) not in A_max:
            A_max[F, G], A_min[F, G] = calculate_k_max(F, G), calculate_k_min(F, G)
        # Update results
        max_one_result = max(max_one_result, B + A_max[F, G])
        min_one_result = min(min_one_result, B + A_min[F, G])
    return max_one_result, min_one_result


def four_russian_trick(text, pattern):
    m = len(pattern)
    max_ones, min_ones = max_min_one_frt(text, m)
    pattern_ones = ones(pattern)
    if max_ones > min_ones + 1 and max_ones >= pattern_ones >= min_ones:
        return True
    elif pattern_ones == max_ones or pattern_ones == min_ones:
        return True
    return False
