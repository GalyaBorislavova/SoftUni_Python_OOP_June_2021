from collections import deque

queue1 = deque([i for i in range(1, 11)])
queue2 = deque([])

first_part = deque([])
for _ in range(5):
    first_part.append(queue1.popleft())

while first_part:
    queue2.appendleft(first_part.popleft())

while queue1:
    queue2.append(queue1.popleft())

print(queue1)
print(queue2)
print(first_part)