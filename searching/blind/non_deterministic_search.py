from test.colors import Colors
from searching.graph import Graph

from random import randint


class NonDeterministicSearch:
    def __init__(self):
        self.checked = []
        self.left = []

    def search(self, graph, start, goals):
        queue, visited = [[start]], set()
        while queue:
            path = queue.pop(0)
            visited.add(path[-1])
            self.checked.append(path)
            for child in graph[path[-1]]:
                if child in visited:
                    continue
                if child in goals:
                    self.left = queue
                    return path + [child]
                queue.insert(randint(0, len(queue)), path + [child])
        return []


def main():
    nds = NonDeterministicSearch()
    path = nds.search(Graph.graph, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if nds.checked:
        print("\nCHECKED:")
        for i, path in enumerate(nds.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if nds.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(nds.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
