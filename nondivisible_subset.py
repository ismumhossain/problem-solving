def nonDivisibleSubset(k, s):
    count = [0] * k
    for num in s:
        count[num % k] += 1

    result = min(count[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            result += max(count[i], count[k - i])
        else:
            result += 1 if count[i] > 0 else 0
    return result