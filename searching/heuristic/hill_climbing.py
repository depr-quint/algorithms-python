from searching.graph import Graph
from searching.search import Search
from searching.heuristic.beam_search import BeamSearch


class HillClimbing(Search):
    # hill climbing one
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
                queue.sort(key=lambda x: weights[(x[-1], x[-2])])
                queue.insert(0, path + [child])
        return []

    # hill climbing two
    def search_alt(self, graph, weights, start, goals):
        bs = BeamSearch()
        path = bs.search(graph, weights, start, goals, 1)
        self.checked = bs.checked
        self.left = bs.left
        return path


def main():
    print("HILL CLIMBING ONE:")
    hc = HillClimbing()
    path = hc.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    hc.print_path(path)

    print("\nHILL CLIMBING TWO:")
    hc = HillClimbing()
    path = hc.search_alt(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    hc.print_path(path)


if __name__ == "__main__":
    main()
