from test.colors import Colors
from searching.graph import Graph
from searching.heuristic.beam_search import BeamSearch


class HillClimbing:
    def __init__(self):
        self.checked = []
        self.left = []

    # hill climbing one
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
                queue.sort(key=lambda x: weights[(x[-1], x[-2])])
                queue.insert(0, path + [child])
                visited.add(child)
        return []

    # hill climbing two
    def search_alt(self, graph, weights, start, goals):
        bs = BeamSearch()
        path = bs.search(graph, weights, start, goals, 1)
        self.checked = bs.checked
        self.left = bs.left
        return path


def main():
    print("HILL CLIMBING ONE")
    hc = HillClimbing()
    path = hc.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if hc.checked:
        print("\nCHECKED:")
        for i, path in enumerate(hc.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if hc.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(hc.left):
            Colors.warning("%s" % path, "%.3d" % i)

    print("\nHILL CLIMBING TWO")
    hc = HillClimbing()
    path = hc.search_alt(Graph.graph, Graph.weights, Graph.start, Graph.goals)

    if path:
        Colors.success("%s" % path, "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if hc.checked:
        print("\nCHECKED:")
        for i, path in enumerate(hc.checked):
            Colors.log("%s" % path, "%.3d" % i)

    if hc.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(hc.left):
            Colors.warning("%s" % path, "%.3d" % i)


if __name__ == "__main__":
    main()
