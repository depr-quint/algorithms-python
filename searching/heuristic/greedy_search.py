from test.colors import Colors
from searching.graph import Graph


class GreedySearch:
    def __init__(self):
        self.checked = []
        self.left = []

    def search(self, graph, weights, start, goals):
        queue, visited = [[start]], set(start)
        while queue:
            path = queue.pop(0)
            self.checked.append(path)
            for child in graph[path[-1]]:
                if child in visited:
                    continue
                if child in goals:
                    self.left = queue
                    return path + [child]
                queue.append(path + [child])
                visited.add(child)
            queue.sort(key=lambda x: weights[(x[-1], x[-2])])
        return []


def main():
    gs = GreedySearch()
    path = gs.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if gs.checked:
        print("\nCHECKED:")
        for i, path in enumerate(gs.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if gs.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(gs.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
