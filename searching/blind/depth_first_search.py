from test.colors import Colors
from searching.graph import Graph


# d = depth of the tree
# b = (average) branching factor
# NOTE: approximations w/o loop-detection into account
#       and no space of representation of paths.

# shortest path:                        NO
# loop detection:                       YES
# speed (worst case):                   O(b^d)
# memory (worst case, length queue):    O(b*d)


class DepthFirstSearch:
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
                queue.insert(0, path + [child])
        return []


def main():
    dfs = DepthFirstSearch()
    path = dfs.search(Graph.graph, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if dfs.checked:
        print("\nCHECKED:")
        for i, path in enumerate(dfs.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if dfs.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(dfs.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
