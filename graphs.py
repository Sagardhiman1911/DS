class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        return self._graph_dict[vertice]

    def all_vertices(self):
        return self._graph_dict.keys()

    def all_edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        edges = []
        for vertex in self._graph_dict:
            for nbr in self._graph_dict[vertex]:
                if {nbr, vertex} not in edges:
                    edges.append({vertex, nbr})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }



from queue import Queue
def bfs(g):
    visited = {}
    level = {}
    parent = {}
    bfs_trav = []
    q = Queue()

    for node in g.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    s = 'a'
    visited[s] = True
    level[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        bfs_trav.append(u)

        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                q.put(v)
    # print(bfs_trav)
    # print(level)

bfs(g)

time = 0
color = {}
parent = {}
trav_time = {} # {start, end}
dfs_trav = []

for node in g.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_trav.append(u)
    time += 1
    for v in g[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

dfs_util('a')
print(dfs_trav)

















