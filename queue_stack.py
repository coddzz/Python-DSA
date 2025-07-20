# Queue using collections.deque
from collections import deque

queue = deque()  # Queue using collections.deque
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)            # [1, 2, 3]
print(queue.popleft())  # 1
print(queue.pop())      # 3
print(queue.popleft())  # 2

print(deque([1,2,3,4]))

#Stack
stack = [1, 2, 3] # using array

print(stack.pop())      # 3
print(stack.pop())      # 2
print(stack.pop())      # 1