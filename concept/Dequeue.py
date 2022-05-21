import collections

DoubleEnded = collections.deque([1, 2, 3, 4, 5])
print(DoubleEnded)
DoubleEnded.append(10)

print(DoubleEnded)

DoubleEnded.appendleft(0)
print(DoubleEnded)

DoubleEnded.pop()
print(DoubleEnded)

DoubleEnded.popleft()
print(DoubleEnded)
