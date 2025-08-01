def equalizeArray(arr):
    from collections import Counter
    
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq