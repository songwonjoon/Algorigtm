## 프로그래머스 정렬 가장 큰수

def solution(numbers):
  numbers = list(map(str, numbers))
  numbers.sort(key=lambda x : x*3, reverse=True)
    
  return str(int(''.join(numbers)))