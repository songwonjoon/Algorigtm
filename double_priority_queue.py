import heapq

def solution(operations):
    heap = []
    max_heap = []

    for i in operations:
        current = i.split()
        if current[0] == 'I':
            num = int(current[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        else:
            if len(heap) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)

            elif current[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))

    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]
    


print(solution(["I 2", "I 3", "I 5", "I 7", "D -1", "D -1", "D -1", "I 2","D 1"]))