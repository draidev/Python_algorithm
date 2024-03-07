def solution(n, m, grid):
  """
  바이러스 유출 연구소에서 안전 영역 확보 프로그램

  Args:
    n: 연구소 세로 크기
    m: 연구소 가로 크기
    grid: 연구소 지도 정보

  Returns:
    안전 영역 크기의 최댓값
  """

  # 빈 칸 개수
  empty_cnt = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 0:
        empty_cnt += 1

  # 벽 설치 위치 리스트
  wall_pos = []

  # 백트래킹 함수
  def backtracking(depth):
    nonlocal empty_cnt

    # 벽 설치 완료
    if depth == 3:
      # 바이러스 확산 시뮬레이션
      virus_spread(grid, wall_pos)

      # 안전 영역 크기 계산
      safe_area = empty_cnt - count_virus(grid)

      # 최댓값 갱신
      global max_safe_area
      max_safe_area = max(max_safe_area, safe_area)
      return

    # 벽 설치 가능 위치 탐색
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 0 and not is_wall_adjacent(grid, i, j):
          grid[i][j] = 1
          wall_pos.append((i, j))
          backtracking(depth + 1)
          grid[i][j] = 0
          wall_pos.pop()

  # 바이러스 확산 시뮬레이션 함수
  def virus_spread(grid, wall_pos):
    for i, j in wall_pos:
      grid[i][j] = 1

    queue = []
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 2:
          queue.append((i, j))

    while queue:
      x, y = queue.pop(0)
      for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
          grid[nx][ny] = 2
          queue.append((nx, ny))

  # 바이러스 개수 계산 함수
  def count_virus(grid):
    cnt = 0
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 2:
          cnt += 1
    return cnt

  # 백트래킹 시작
  backtracking(0)

  return max_safe_area

M, N = map(int, input().split())

lab_map = [list(map(int, input().split())) for _ in range(N)]

print(solution(M, N, lab_map))