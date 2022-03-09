## 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) 여행경로

from collections import deque

def BFS(i, tickets, visited):
    queue = deque()

def solution(tickets):
    answer = []

    tickets = [False] * len(tickets)
    
    for i in range(len(tickets)):
        if not visited[i]:
            BFS(i, tickets, visited)

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))