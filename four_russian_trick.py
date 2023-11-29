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
def four_russian_trick(text, l):
    # Initialize values
    n = len(text)
    s = int(math.log2(n))
    A_max, A_min = {}, {}
    B = 0
    max_one_result, min_one_result = 0, n
    # If s is 0, return the count of '1's in text
    if s == 0:
        return ones(text), ones(text)
    # Iterate over the text in chunks of size s
    for i in range(0, n, s):
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


# The dynamic programming approach, implemented just to compare
def max_one_dp(text, l):
    n = len(text)
    s = int(math.log2(n) / 6)
    w = text[:l]
    w_ones = ones(w)
    result = w_ones
    for i in range(1, n - l + 1):
        temp = 0
        w = text[i:i + l]
        if text[i - 1] == '0' and text[i + l - 1] == '1':
            temp = 1
        elif text[i - 1] == '1' and text[i + l - 1] == '0':
            temp = -1
        w_ones = w_ones + temp
        result = max(result, w_ones)

    return result
