def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            known = combined.count('1')

            if known > max_topics:
                max_topics = known
                team_count = 1
            elif known == max_topics:
                team_count += 1

    return [max_topics, team_count]