"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exhist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store visited verts
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if vertext has not been visited 
            if v not in visited:
                print(v)
                visited.add(v)
                # print for debugging
                
                # add all neighbors to back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

                    


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack push a starting vertex
        s = Stack()
        s.push(starting_vertex)

        # create a set to store visited verts
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop the first vert
            v = s.pop()
            # if vert has not been visited
            if v not in visited:
                # mark vert as visited
                visited.add(v)
                # print for debug
                print(v)
                # push all neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for nbrs in self.get_neighbors(starting_vertex):
                self.dft_recursive(nbrs, visited)
        

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()

            vert = path[-1]

            if vert not in visited:
                visited.add(vert)

                if vert == destination_vertex:
                    return path
                
                else:
                    for ngbr in self.get_neighbors(vert):
                        new_path = list(path)
                        new_path.append(ngbr)
                        queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            path = stack.pop()

            vert = path[-1]

            if vert not in visited:
                visited.add(vert)
            if vert == destination_vertex:
                return path
            else:
                for ngbr in self.get_neighbors(vert):
                    new_path = list(path)
                    new_path.append(ngbr)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited == None and path == None:
            visited = set()
            path = []
        
        if starting_vertex not in visited:
            new_path = list(path)
            new_path.append(starting_vertex)

            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return new_path
            
            for ngbr in self.get_neighbors(starting_vertex):
                next_path = self.dfs_recursive(ngbr, destination_vertex, visited, new_path)
                if next_path:
                    return next_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))