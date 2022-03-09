### 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) 네트워크
 
def DFS(n, computers, i, visited):
    visited[i] = True
    for connect in range(n):
        if connect != i and computers[i][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            DFS(n, computers, i, visited)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
