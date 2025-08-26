def encryption(s):
    s = s.replace(" ", "")
    n = len(s)
    
    rows = int(math.floor(math.sqrt(n)))
    cols = int(math.ceil(math.sqrt(n)))
    
    if rows * cols < n:
        rows += 1
    
    # Build the encrypted message
    encrypted_words = []
    for col in range(cols):
        word = ""
        for row in range(rows):
            idx = row * cols + col
            if idx < n:
                word += s[idx]
        encrypted_words.append(word)
    
    return " ".join(encrypted_words)
