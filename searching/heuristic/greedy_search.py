from searching.graph import Graph
from searching.search import Search


class GreedySearch(Search):
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
            queue.sort(key=lambda x: weights[(x[-1], x[-2])])
        return []


def main():
    gs = GreedySearch()
    path = gs.search(Graph.graph, Graph.weights, Graph.start, Graph.goals)
    gs.print_path(path)


if __name__ == "__main__":
    main()
