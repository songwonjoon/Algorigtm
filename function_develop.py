## 프로그래머스 스택/큐 기능개발

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
     
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)       

    return answer

print(solution([1, 2, 3, 2, 3]))