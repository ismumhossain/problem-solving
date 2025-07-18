def appendAndDelete(s, t, k):
    common_length = 0
    for sc, tc in zip(s, t):
        if sc == tc:
            common_length += 1
        else:
            break

    total_ops = (len(s) - common_length) + (len(t) - common_length)

    if total_ops > k:
        return "No"
    elif (k - total_ops) % 2 == 0 or k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"