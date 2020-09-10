"""
using graphs to solve problems

1. translate problem
2. build the graph from the data
3. traverase/search or whatever combination you need


Word Ladders Problem
"""
words = set()

with open("words.txt") as f:
    for word in f:
        words.add(word.lower().strip())

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

def get_neighbors(word):
    neighbors = []

    for w in words:
        if len(w) != len(word):
            continue

        diffs = 0

        for i in range(len(w)):
            if w[i] != word[i]:
                diffs += 1

        if diffs == 1:
            neighbors.append(w)

    return neighbors

def bfs(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                #path_copy.append(neighbor)
                #q.enqueue(path_copy)

print(bfs("thing", "zings"))