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

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    path = [starting_node]
    q.enqueue(path)

    while q.size() >  0:
        current_path = q.dequeue()
        new_path = []
        changed = False

        for vertexId in current_path:
            for ancestor in ancestors:
                if ancestor[1] == vertexId:
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)

        #loop through final path of largest value
        if changed is False:
            if current_path[0] == starting_node:
                return -1
            else:
                return min(current_path)