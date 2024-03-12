

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.data})"

    def __str__(self):
        return f"Krasna reprezentace Node({self.data})"






n1 = Node(1)
n1


repr(n1)
str(n1)
print(n1)


n2 = Node(3)
n3 = Node(7)

print(n1.next)
print(n2.next)
print(n3.next)

n1.next = n2
n2.next = n3

print(n1.next)
print(n2.next)
print(n3.next)




class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        all_nodes = [str(node) for node in self.go_thru_all_nodes()]

        return f"LinkedList({'->'.join(all_nodes)})"

    def go_thru_all_nodes(self):
        node: Node = self.head
        while node is not None:
            yield node
            node = node.next


ll = LinkedList(n1)

for node in ll.go_thru_all_nodes():
    print(node)

print(ll)


