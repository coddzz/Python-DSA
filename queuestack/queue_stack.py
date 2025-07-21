
from collections import deque

queue = deque([1, 2, 3])  # Queue using collections.deque 
print(queue.popleft())  # 1 -->  we can use popleft()
print(queue.pop())      # 3  --> pop()


stack = [1, 2, 3]
print(stack.pop())   # 3   --> pop()
print(stack.pop())   # 2