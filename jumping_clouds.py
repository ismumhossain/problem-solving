def jumpingOnClouds(c):
    jumps = 0
    position = 0
    while position < len(c) - 1:
        if position + 2 < len(c) and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1
    return jumps