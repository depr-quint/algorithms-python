from test.colors import Colors
from searching.graph import Graph


# b = (average) branching factor of the tree
# m = depth of the shallowest solution
# NOTE: approximations w/o loop-detection into account
#       and no space of representation of paths.

# shortest path:                        YES
# loop detection:                       NO (remains complete)
# speed (worst case):                   O(b^m)
# memory (worst case, length queue):    O(b^m)


class BreadthFirstSearch:
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
                queue.append(path + [child])
        return []


def main():
    bfs = BreadthFirstSearch()
    path = bfs.search(Graph.graph, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if bfs.checked:
        print("\nCHECKED:")
        for i, path in enumerate(bfs.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if bfs.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(bfs.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
