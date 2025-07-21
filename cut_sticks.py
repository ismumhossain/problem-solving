def cutTheSticks(arr):
    result = []
    sticks = arr[:]
    while sticks:
        result.append(len(sticks))
        min_length = min(sticks)
        sticks = [s - min_length for s in sticks if s - min_length > 0]
    return result