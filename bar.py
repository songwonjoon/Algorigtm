## 백준 막대기
x = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

for stick in sticks:
  if stick <= x:
    count += 1
    x -= stick

  if x == 0:
    break;
    
print(count)