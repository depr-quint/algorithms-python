from searching.graph import Graph
from searching.search import Search


# b = (average) branching factor of the tree
# m = depth of the shallowest solution
# NOTE: approximations w/o loop-detection into account
#       and no space of representation of paths.

# shortest path:                        YES
# loop detection:                       NO (remains complete)
# speed (worst case):                   O(b^(m/2))
# memory (worst case, length queue):    O(b^(m/2))


class BiDirectionalSearch(Search):
    def search(self, graph, start, goal):
        queue1, queue2 = [[start]], [[goal]]
        visited1, visited2 = set(), set()
        while queue1 and queue2:
            path1 = queue1.pop(0)
            visited1.add(path1[-1])
            self.checked.append(path1)
            for child in graph[path1[-1]]:
                if child in visited1:
                    continue
                if child in visited2:
                    return path1 + self._get_shared_state(queue2, child)
                queue1.append(path1 + [child])

            path2 = queue2.pop(0)
            visited2.add(path2[-1])
            self.checked.append(path2)
            for child in graph[path2[-1]]:
                if child in visited2:
                    continue
                if child in visited1:
                    return path2 + self._get_shared_state(queue1, child)
                queue2.append(path2 + [child])
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
    bds.print_path(path)


if __name__ == "__main__":
    main()
