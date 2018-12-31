from test.colors import Colors
from searching.graph import Graph


class Search:
    def __init__(self):
        self.checked = []
        self.left = []

    def print_path(self, path):
        if path:
            Colors.success("%s" % path, "\tFOUND")
        else:
            Colors.fail("[]", "\tNO PATH")

        if self.checked:
            print("\n\tCHECKED:")
            for i, path in enumerate(self.checked):
                Colors.log("%s" % path, "\t%.3d" % i)

        if self.left:
            print("\n\tNOT CHECKED:")
            for i, path in enumerate(self.left):
                Colors.warning("%s" % path, "\t%.3d" % i)


class OptimalSearch(Search):
    def print_cost(self, path):
        if path:
            Colors.success("%s, cost %d" % (path, Graph.cost(path, Graph.weights)), "\tFOUND")
        else:
            Colors.fail("[]", "\tNO PATH")

        if self.checked:
            print("\n\tCHECKED:")
            for i, path in enumerate(self.checked):
                Colors.log("%s, cost: %d" % (path, Graph.cost(path, Graph.weights)), "\t%.3d" % i)

        if self.left:
            print("\n\tNOT CHECKED:")
            for i, path in enumerate(self.left):
                Colors.warning("%s, cost: %d" % (path, Graph.cost(path, Graph.weights)), "\t%.3d" % i)

    def print_estimate(self, path):
        if path:
            Colors.success(
                "%s, cost %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)), "\tFOUND")
        else:
            Colors.fail("[]", "\tNO PATH")

        if self.checked:
            print("\n\tCHECKED:")
            for i, path in enumerate(self.checked):
                Colors.log("%s, cost: %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)),
                           "\t%.3d" % i)

        if self.left:
            print("\n\tNOT CHECKED:")
            for i, path in enumerate(self.left):
                Colors.warning(
                    "%s, cost: %0.1f" % (path, Graph.estimate(path, Graph.weights, Graph.distance, Graph.goal)),
                    "\t%.3d" % i)