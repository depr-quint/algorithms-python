from test.colors import Colors
from searching.graph import Graph


# b = (average) branching factor of the tree
# m = depth of the shallowest solution
# NOTE: approximations w/o loop-detection into account
#       and no space of representation of paths.

# shortest path:                        YES
# loop detection:                       NO (remains complete)
# speed (worst case):                   O(b^(m/2))
# memory (worst case, length queue):    O(b^(m/2))


class BiDirectionalSearch:
    def __init__(self):
        self.checked = []
        self.left = []

    def search(self, graph, start, goal):
        queue1, queue2 = [[start]], [[goal]]
        visited1, visited2 = set(start), set(goal)
        while queue1 and queue2:
            path1, path2 = queue1.pop(0), queue2.pop(0)
            self.checked.append(path1)
            for child in graph[path1[-1]]:
                if child in visited1:
                    continue
                if child in visited2:
                    return path1 + self._get_shared_state(queue2, child)
                queue1.append(path1 + [child])
                visited1.add(child)

            self.checked.append(path2)
            for child in graph[path2[-1]]:
                if child in visited2:
                    continue
                if child in visited1:
                    return path2 + self._get_shared_state(queue1, child)
                queue2.append(path2 + [child])
                visited2.add(child)
        return []

    @staticmethod
    def _get_shared_state(queue, state):
        for path in queue:
            if state not in path:
                continue
            return list(reversed(path))
        return []


def main():
    bds = BiDirectionalSearch()
    path = bds.search(Graph.graph, Graph.start, Graph.goal)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if bds.checked:
        print("\nCHECKED:")
        for i, path in enumerate(bds.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if bds.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(bds.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
