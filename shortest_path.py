## 백준 최단경로 문제
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

start = int(input())
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def dijkstra(start):
  distance[start] = 0
  heapq.heappush(heap, (0, start))

  while heap:
    weight, now = heapq.heappop(heap)

    if distance[now] < weight: 
      continue

    for w, next_node in graph[now]:
      next_wei = w+ weight
      if next_wei < distance[next_node]:
        distance[next_node] = next_wei
        heapq.heappush(heap,(next_wei, next_node))


    
dijkstra(start)

for i in range(1,n+1): print("INF" if distance[i] == INF else distance[i])