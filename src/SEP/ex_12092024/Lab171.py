# deque -
# fifo -
# A list like
from collections import  deque

d = deque([1,2,3])
print(d)
d.append(4)
print(d)
d.append(5)
d.appendleft(0)
d.pop()
d.popleft()

l =list(d)
print(l)