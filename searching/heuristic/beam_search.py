from searching.graph import Graph
from searching.search import Search


class BeamSearch(Search):
    def search(self, graph, weights, start, goals, width):
        queue, visited = [[start]], set()
        while queue:
            children = []
            while queue:
                path = queue.pop(0)
                visited.add(path[-1])
                self.checked.append(path)
                for child in graph[path[-1]]:
                    if child in visited:
                        continue
                    children.append(path + [child])
            children.sort(key=lambda x: weights[(x[-1], x[-2])])
            queue = children[:width]
            for path in children[:width]:
                if path[-1] in goals:
                    return path
        return []


def main():
    for width in range(1, 3):
        print("\n" * (width - 1) + "WIDTH: %d" % width)
        bs = BeamSearch()
        path = bs.search(Graph.graph, Graph.weights, Graph.start, Graph.goals, width)
        bs.print_path(path)
        print()


if __name__ == "__main__":
    main()
