"""
Nodes connected by edges
Vertexes
Vertices
Vertes

LL:

cur = head
while cur is not None:
    print(cur)
    cur = cur.net

Binary Tree:

traverse(node):
    if not is None: 
        return
    traverse(node.left)
    print(node)
    traverse(node.right)

General graph:


"""

class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return f'Node({repr(self.value)})'

a = Node('A')
b = Node('B')
c = Node('C')

a.neighbors.append(b)
a.neighbors.append(c)

print(a.neighbors)

