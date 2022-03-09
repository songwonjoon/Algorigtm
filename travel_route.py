## 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) 여행경로

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    #dictionary에 스택의 top으로 시작하는 경로가 있는지 확인
    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]: # 있는경우
            answer.append(stack.pop())
        else: # 없는 경우
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer