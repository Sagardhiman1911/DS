class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.nbr = list()
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_nbr(self, v):
        nset = set(self.nbr)
        if v not in nset:
            self.nbr.append(v)
            self.nbr.sort()


class Graph(object):
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_nbr(v)
                elif key == v:
                    value.add_nbr(u)
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].nbr))

    def _dfs(self, vertex):
        pass

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)


