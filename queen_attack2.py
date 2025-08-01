def queensAttack(n, k, r_q, c_q, obstacles):
    obstacle_set = set(map(tuple, obstacles))

    directions = [
        (1, 0),   
        (-1, 0),  
        (0, 1),  
        (0, -1),  
        (1, 1),   
        (1, -1),  
        (-1, 1),  
        (-1, -1)  
    ]

    total_moves = 0

    for dx, dy in directions:
        x, y = r_q, c_q
        while True:
            x += dx
            y += dy
            if x < 1 or x > n or y < 1 or y > n or (x, y) in obstacle_set:
                break
            total_moves += 1

    return total_moves