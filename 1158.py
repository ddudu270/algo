import sys
from _collections import deque

num, idx = map(int, sys.stdin.readline().rstrip().split())
count = 1
result = []

dq = deque([str(i) for i in range(1, num + 1)])

while dq:  # dq가 빌때까지 반복
    if count % idx != 0:
        dq.append(dq.popleft())
        count += 1
    else:
        result.append(dq.popleft())
        count = 1

print("<", end='')
print(", ".join(i for i in result), end='')
print(">")

# count = 0 설정한 후, pop & append가 count 1
# count가 3의 배수면 아예 뺌. 그러고 결국 큐가 비면 실행 종료
# 왜 while을 사용할까? 큐에서 빠지면 다시 count는 0
