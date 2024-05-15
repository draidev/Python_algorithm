def solution(k, dungeons):
    """
    BFS 알고리즘을 이용하여 유저가 하루에 최대 탐험 가능한 던전 수를 반환합니다.

    Args:
        k (int): 유저의 피로도
        dungeons (list[list[int]]): 2차원 배열, 각 행은 [최소 필요 피로도, 소모 피로도]를 의미합니다.

    Returns:
        int: 유저가 하루에 최대 탐험 가능한 던전 수
    """

    visited = [0] * len(dungeons)
    explored = []
    current_fatigue = k

    queue = [(current_fatigue, [])]

    while queue:
        current_fatigue, explored_dungeons = queue.pop(0)

        if current_fatigue <= 0:
            break

        for i, dungeon in enumerate(dungeons):
            if not visited[i] and current_fatigue >= dungeon[0]:
                visited[i] = 1
                explored.append(i)
                remaining_fatigue = current_fatigue - dungeon[1]
                next_explored = explored_dungeons + [i]
                queue.append((remaining_fatigue, next_explored))

    return len(explored)

