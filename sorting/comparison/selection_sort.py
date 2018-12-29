from test.colors import Test, Colors
from sorting.comparison_sort import ComparisonSort

from random import randint


class SelectionSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        for i in range(self.n):
            m = i
            for j in range(i + 1, self.n):
                if self.less(array[j], array[m]):
                    m = j
            self.exch(array, i, m)

    def best_comp(self):
        # n * (n - 1) / 2
        return self.n * (self.n - 1) / 2

    def worst_comp(self):
        # n * (n - 1) / 2
        return self.n * (self.n - 1) / 2

    def best_exch(self):
        # n
        return self.n

    def worst_exch(self):
        # n
        return self.n


def main():
    selection_sort = SelectionSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)

    selection_sort.sort(a)
    print("LENGTH %d" % selection_sort.n)

    Test.is_sorted(a)

    Colors.log("%.4d" % selection_sort.comparisons, "COMPARES ")
    print("--- BEST: %d, WORST: %d" %
          (selection_sort.best_comp(), selection_sort.worst_comp()))
    Colors.log("%.4d" % selection_sort.exchanges, "EXCHANGES")
    print("--- BEST: %d, WORST: %d" %
          (selection_sort.best_exch(), selection_sort.worst_exch()))

    print("ARRAY", a)


if __name__ == "__main__":
    main()
