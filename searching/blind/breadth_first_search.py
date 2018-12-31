from searching.graph import Graph
from searching.search import Search


# b = (average) branching factor of the tree
# m = depth of the shallowest solution
# NOTE: approximations w/o loop-detection into account
#       and no space of representation of paths.

# shortest path:                        YES
# loop detection:                       NO (remains complete)
# speed (worst case):                   O(b^m)
# memory (worst case, length queue):    O(b^m)


class BreadthFirstSearch(Search):
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
    bfs.print_path(path)


if __name__ == "__main__":
    main()
