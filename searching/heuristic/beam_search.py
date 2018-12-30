from test.colors import Colors
from searching.graph import Graph


class BeamSearch:
    def __init__(self):
        self.checked = []
        self.left = []

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

        if path:
            Colors.success("%s" % path, "\tFOUND")
        else:
            Colors.fail("[]", "\tNO PATH")

        if bs.checked:
            print("\n\tCHECKED:")
            for i, path in enumerate(bs.checked):
                Colors.log("%s" % path, "\t%.3d" % i)

        if bs.left:
            print("\nNOT CHECKED:")
            for i, path in enumerate(bs.left):
                Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
