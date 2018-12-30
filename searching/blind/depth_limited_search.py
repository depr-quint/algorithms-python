from test.colors import Colors
from searching.graph import Graph


class DepthLimitedSearch:
    def __init__(self):
        self.checked = []
        self.left = []
        self.depth = 0

    def search(self, graph, start, goals, depth):
        queue, visited = [[start]], set(start)
        self.depth = depth
        while queue:
            path = queue.pop(0)
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
                visited.add(child)
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
    print("DEPTH LIMITED:\n")
    for depth in range(4, 6):
        print("\tDEPTH: %d" % depth)

        dls = DepthLimitedSearch()
        path = dls.search(Graph.graph, Graph.start, Graph.goals, depth)

        if path:
            Colors.success("%s" % path, "\tFOUND")
        else:
            Colors.fail("[]", "\tNO PATH")
            print()
            continue

        if dls.checked:
            print("\n\tCHECKED:")
            for i, path in enumerate(dls.checked):
                Colors.log("%s" % path, "\t%.3d" % i)

        if dls.left:
            print("\n\tNOT CHECKED:")
            for i, path in enumerate(dls.left):
                Colors.warning("%s" % path, "\t%.3d" % i)

    print("\nITERATIVE DEEPENING ALGORITHM:\n")
    dls = DepthLimitedSearch()
    path = dls.iterative_deepening(Graph.graph, Graph.start, Graph.goals)

    print("\tDEPTH: %d" % dls.depth)
    if path:
        Colors.success("%s" % path, "\tFOUND")
    else:
        Colors.fail("[]", "\tNO PATH")
        print()

    if dls.checked:
        print("\n\tCHECKED:")
        for i, path in enumerate(dls.checked):
            Colors.log("%s" % path, "\t%.3d" % i)

    if dls.left:
        print("\n\tNOT CHECKED:")
        for i, path in enumerate(dls.left):
            Colors.warning("%s" % path, "\t%.3d" % i)


if __name__ == "__main__":
    main()
