def repeatedString(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    count_a_in_remainder = s[:remainder].count('a')
    return full_repeats * count_a_in_s + count_a_in_remainder