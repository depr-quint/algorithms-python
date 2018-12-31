from searching.graph import Graph
from searching.search import Search


class DepthLimitedSearch(Search):
    def __init__(self):
        super().__init__()
        self.depth = 0

    def search(self, graph, start, goals, depth):
        queue, visited = [[start]], set()
        self.depth = depth
        while queue:
            path = queue.pop(0)
            visited.add(path[-1])
            if len(path) > depth:
                continue
            self.checked.append(path)
            for child in graph[path[-1]]:
                if child in visited:
                    continue
                if child in goals:
                    self.left = queue
                    return path + [child]
                queue.insert(0, path + [child])
        return []

    def iterative_deepening(self, graph, start, goals):
        path, depth = [], 1
        while not path:
            path = self.search(graph, start, goals, depth)
            if not path:
                depth += 1
                self.depth = depth
        return path


def main():
    print("DEPTH LIMITED:")
    for depth in range(4, 6):
        print("\tDEPTH: %d" % depth)

        dls = DepthLimitedSearch()
        path = dls.search(Graph.graph, Graph.start, Graph.goals, depth)
        dls.print_path(path)
        print()

    print("ITERATIVE DEEPENING ALGORITHM:")
    dls = DepthLimitedSearch()
    path = dls.iterative_deepening(Graph.graph, Graph.start, Graph.goals)
    print("\tDEPTH: %d" % dls.depth)
    dls.print_path(path)


if __name__ == "__main__":
    main()
