import time
from collections import deque


class QueueList:

    def __init__(self):
        self.data = list()

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop()

    def __repr__(self):
        return f"QueueList({self.data})"


ql = QueueList()
ql.enqueue(15)
ql.enqueue(20)
ql.enqueue(55)

ql.dequeue()

[5, 1, 55, 20, 15]

class QueueDeque:

    def __init__(self):
        self.data = deque()

    def enqueue(self, item):
        self.data.appendleft(item)

    def dequeue(self):
        return self.data.pop()

    def __repr__(self):
        return f"QueueDeque({self.data})"



qd = QueueDeque()
qd.enqueue(15)
qd.enqueue(20)
qd.enqueue(55)

qd.dequeue()

N = 500_000

t0 = time.time()
ql = QueueList()
for i in range(N):
    ql.enqueue(i)
t1 = time.time()
for i in range(N):
    ql.dequeue()
t2 = time.time()

print("Time total", t2-t0)
print("Time enqueue", t1-t0)
print("Time dequeue", t2-t1)


N = 100_000
# QueueList
# Time total 1.6630280017852783
# Time enqueue 1.6506261825561523
# Time dequeue 0.012401819229125977

# N = 500_000
# QueueList
# Time total 60.95418953895569
# Time enqueue 60.88298058509827
# Time dequeue 0.07120895385742188


t0 = time.time()
qd = QueueDeque()
for i in range(N):
    qd.enqueue(i)
t1 = time.time()
for i in range(N):
    qd.dequeue()
t2 = time.time()


print("Time total", t2-t0)
print("Time enqueue", t1-t0)
print("Time dequeue", t2-t1)


N = 100 000
QueueDeque
Time total 0.027611255645751953
Time enqueue 0.01355123519897461
Time dequeue 0.014060020446777344


N = 500_000
QueueDeque
Time total 0.1623852252960205
Time enqueue 0.09324789047241211
Time dequeue 0.0691373348236084

Time total 0.1417238712310791
Time enqueue 0.07326102256774902
Time dequeue 0.06846284866333008