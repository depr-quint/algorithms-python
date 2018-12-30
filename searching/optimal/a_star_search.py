from test.colors import Colors
from searching.graph import Graph


class AStarSearch:
    def __init__(self):
        self.checked = []
        self.left = []

    def search(self, graph, weights, estimate, start, goal):
        queue, visited, found = [[start]], set(), []
        while queue:
            path = queue.pop(0)
            visited.add(path[-1])
            self.checked.append(path)
            for child in graph[path[-1]]:
                if child in visited:
                    continue
                if child == goal:
                    found = path + [child]
                if not found or \
                        Graph.estimate(path + [child], weights, estimate, goal) < \
                        Graph.estimate(found, weights, estimate, goal):
                    queue.append(path + [child])
                    for p in queue:
                        if p[-1] is not (path + [child])[-1]:
                            continue
                        if Graph.cost(p, weights) < Graph.cost(path + [child], weights):
                            queue.remove(path + [child])
            queue.sort(key=lambda x: Graph.estimate(x, weights, estimate, goal))
        return found


def main():
    ass = AStarSearch()
    path = ass.search(Graph.graph, Graph.weights, Graph.distance, Graph.start, Graph.goal)

    if path:
        Colors.success(
            "%s, cost %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)), "\tFOUND")
    else:
        Colors.fail("[]", "\tNO PATH")

    if ass.checked:
        print("\n\tCHECKED:")
        for i, path in enumerate(ass.checked):
            Colors.log("%s, cost: %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)),
                       "\t%.3d" % i)

    if ass.left:
        print("\n\tNOT CHECKED:")
        for i, path in enumerate(ass.left):
            Colors.warning("%s, cost: %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)),
                           "\t%.3d" % i)


if __name__ == "__main__":
    main()
