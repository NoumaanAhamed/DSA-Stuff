class Graph:
    def breadth_first_search(self, v):
        visited = set()
        queue = [v]
        result = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph[vertex] - visited)
        return result

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

def main():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('D', 'I')
    g.add_edge('E', 'J')
    g.add_edge('E', 'K')
    g.add_edge('F', 'L')
    g.add_edge('F', 'M')
    g.add_edge('G', 'N')
    g.add_edge('G', 'O')
    print(g.breadth_first_search('A'))