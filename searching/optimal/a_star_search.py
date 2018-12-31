from searching.graph import Graph
from searching.search import OptimalSearch


class AStarSearch(OptimalSearch):
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

    def iterative_deepening(self, graph, weights, estimate, start, goal, bound):
        new_bound = 99
        queue, visited, found = [[start]], set(), []
        while queue:
            path = queue.pop(0)
            visited.add(path[-1])
            cost = Graph.estimate(path, weights, estimate, goal)
            if cost > bound:
                if cost < new_bound:
                    new_bound = cost
                continue
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
        return found, new_bound


def main():
    print("A* SEARCH")
    ass = AStarSearch()
    path = ass.search(Graph.graph, Graph.weights, Graph.distance, Graph.start, Graph.goal)
    ass.print_estimate(path)

    print("\nITERATIVE DEEPENING")
    ass = AStarSearch()
    path, new_bound = ass.iterative_deepening(Graph.graph, Graph.weights, Graph.distance, Graph.start, Graph.goal, 5)
    print("\tBOUND: 5")

    while not path:
        ass.print_estimate(path)
        print("\n\tBOUND: %d" % new_bound)
        path, new_bound = ass.iterative_deepening(Graph.graph, Graph.weights, Graph.distance, Graph.start, Graph.goal,
                                                  new_bound)
    ass.print_estimate(path)


if __name__ == "__main__":
    main()
