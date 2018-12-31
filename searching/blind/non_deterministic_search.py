from searching.graph import Graph
from searching.search import Search

from random import randint


class NonDeterministicSearch(Search):
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
                queue.insert(randint(0, len(queue)), path + [child])
        return []


def main():
    nds = NonDeterministicSearch()
    path = nds.search(Graph.graph, Graph.start, Graph.goals)
    nds.print_path(path)


if __name__ == "__main__":
    main()
