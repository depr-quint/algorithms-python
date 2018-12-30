from test.colors import Colors
from searching.graph import Graph


class UniformCost:
    def __init__(self):
        self.checked = []
        self.left = []

    def search(self, graph, weights, start, goals):
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
            queue.sort(key=lambda x: Graph.cost(x, weights))
        return []

    def branch_and_bound(self, graph, weights, start, goals):
        queue, visited, found = [[start]], set(), []
        while queue:
            path = queue.pop(0)
            visited.add(path[-1])
            self.checked.append(path)
            for child in graph[path[-1]]:
                if child in visited:
                    continue
                if child in goals:
                    found = path + [child]
                if not found or Graph.cost(path + [child], weights) < Graph.cost(found, weights):
                    queue.append(path + [child])
            queue.sort(key=lambda x: Graph.cost(x, weights))
        return found


def main():
    print("UNIFORM COST")
    uc = UniformCost()
    path = uc.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)

    if path:
        Colors.success("%s, cost %d" % (path, Graph.cost(path, Graph.weights)), "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if uc.checked:
        print("\nCHECKED:")
        for i, path in enumerate(uc.checked):
            Colors.log("%s, cost: %d" % (path, Graph.cost(path, Graph.weights)), "%.3d" % i)

    if uc.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(uc.left):
            Colors.warning("%s, cost: %d" % (path, Graph.cost(path, Graph.weights)), "%.3d" % i)

    print("\nBRANCH AND BOUND")
    uc = UniformCost()
    path = uc.branch_and_bound(Graph.graph, Graph.weights, Graph.start, Graph.goals)

    if path:
        Colors.success(
            "%s, cost %d" % (path, sum([Graph.weights[(path[i], path[i + 1])] for i in range(len(path) - 1)])), "FOUND")
    else:
        Colors.fail("[]", "NO PATH")

    if uc.checked:
        print("\nCHECKED:")
        for i, path in enumerate(uc.checked):
            Colors.log(
                "%s, cost: %d" % (path, sum([Graph.weights[(path[i], path[i + 1])] for i in range(len(path) - 1)])),
                "%.3d" % i)

    if uc.left:
        print("\nNOT CHECKED:")
        for i, path in enumerate(uc.left):
            Colors.warning(
                "%s, cost: %d" % (path, sum([Graph.weights[(path[i], path[i + 1])] for i in range(len(path) - 1)])),
                "%.3d" % i)


if __name__ == "__main__":
    main()
