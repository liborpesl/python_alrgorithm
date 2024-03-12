stack_list = []

stack_list.append(1)
stack_list.append(2)
stack_list.append(3)

stack_list

stack_list.pop()
stack_list

stack_list.append(11)
stack_list.pop()


class StackFromList:

    def __init__(self):
        self.data = list()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def __repr__(self) -> str:
        return f"StackFromList({self.data[:4]})"


stack = StackFromList()
stack.push(1)
stack.push(5)
print(stack)

stack.pop()
print(stack)

from collections import deque

my_deque = deque()
my_list = list()


class StackFromDeque:

    def __init__(self):
        self.data = deque()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def __repr__(self) -> str:
        return f"StackFromDeque({self.data[:4]})"


stack = StackFromDeque()
stack.push(5)
stack.push(10)
stack.pop()


import time

t0 = time.time()
stack = StackFromList()
for i in range(10_000_000):
    stack.push(i)

for i in range(10_000_000):
    stack.pop()

print(time.time() - t0)


sum([3.529953956604004,
3.6938700675964355,
3.6802570819854736,])


import time

t0 = time.time()
stack = StackFromDeque()
for i in range(10_000_000):
    stack.push(i)

for i in range(10_000_000):
    stack.pop()

print(time.time() - t0)


sum([3.124699115753174, 3.315277099609375, 3.4109463691711426])
