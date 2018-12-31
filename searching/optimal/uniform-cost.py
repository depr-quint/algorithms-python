from searching.graph import Graph
from searching.search import OptimalSearch


class UniformCost(OptimalSearch):
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

    def estimate_extended(self, graph, weights, estimate, start, goal):
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
            queue.sort(key=lambda x: Graph.estimate(x, weights, estimate, goal))
        return found

    def path_deletion(self, graph, weights, start, goals):
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
                    for p in queue:
                        if p[-1] is not (path + [child])[-1]:
                            continue
                        if Graph.cost(p, weights) < Graph.cost(path + [child], weights):
                            queue.remove(path + [child])
            queue.sort(key=lambda x: Graph.cost(x, weights))
        return found


def main():
    print("UNIFORM COST:")
    uc = UniformCost()
    path = uc.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    uc.print_cost(path)

    print("\nBRANCH AND BOUND:")
    uc = UniformCost()
    path = uc.branch_and_bound(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    uc.print_cost(path)

    print("\nESTIMATE EXTENDED")
    uc = UniformCost()
    path = uc.estimate_extended(Graph.graph, Graph.weights, Graph.distance, Graph.start, Graph.goal)
    uc.print_estimate(path)

    print("\nPATH DELETION")
    uc = UniformCost()
    path = uc.path_deletion(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    uc.print_cost(path)


if __name__ == "__main__":
    main()
