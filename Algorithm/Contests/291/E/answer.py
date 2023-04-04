from collections import deque

n, m = map(int, input().split())

class Node:
    def __init__(self,index):
        self.index = index
        self.parents = []
        self.children = []
        self.toporo = 0
        self.memo = []

nodes = []
for i in range(n + 1):
    nodes.append(Node(i))

for _ in range(m):
    s,g = map(int,input().split()) # start, goal
    nodes[s].children.append(g)
    nodes[g].parents.append(s)
    nodes[g].memo.append(s)

for i in range(1,n+1):
    print(nodes[i].children)
    print(nodes[i].parents)

queue = deque()

for node in nodes:
    if len(node.parents) == 0:
        queue.append(node)

order = 1

while queue:
    node = queue.pop()

    nodes[node.index].toporo = order
    order += 1

    children = node.children

    for child in children:
        nodes[child].parents.remove(node.index)

        if len(nodes[child].parents) == 0:
            queue.append(nodes[child])

toporo_nodes = sorted(nodes, key=lambda x: x.toporo)[:-1]

toporo_order = list(map(lambda x: str(x.index), toporo_nodes))

print(toporo_order)

ans = True
for i in range(n-1):
    if int(toporo_order[i+1]) not in set(nodes[int(toporo_order[i])].children):
        ans = False
        break

if ans:
    print('Yes')
    print(' '.join(toporo_order))
else:
    print('No')
