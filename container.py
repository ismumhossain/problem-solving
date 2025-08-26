def organizingContainers(container):
    container_sum = [sum(row) for row in container]
    ball_type_sum = [sum(col) for col in zip(*container)]

    return "Possible" if sorted(container_sum) == sorted(ball_type_sum) else "Impossible"
