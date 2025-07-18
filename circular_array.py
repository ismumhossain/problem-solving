def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n
    result = []
    for q in queries:
        idx = (q - k) % n
        result.append(a[idx])
    return result