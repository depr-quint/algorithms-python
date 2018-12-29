from test.colors import Test, Colors
from sorting.comparison_sort import ComparisonSort

from random import randint


class InsertionSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        for i in range(self.n):
            for j in range(i, 0, -1):
                if not self.less(array[j], array[j - 1]):
                    break
                self.exch(array, j, j - 1)

    def best_comp(self):
        # n - 1
        return self.n - 1

    def worst_comp(self):
        # n * (n - 1) / 2
        return self.n * (self.n - 1) / 2

    def best_exch(self):
        # 0
        return 0

    def worst_exch(self):
        # n * (n - 1) / 2
        return self.n * (self.n - 1) / 2


def main():
    insertion_sort = InsertionSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)

    insertion_sort.sort(a)
    print("LENGTH %d" % insertion_sort.n)

    Test.is_sorted(a)

    Colors.log("%.4d" % insertion_sort.comparisons, "COMPARES ")
    print("--- BEST: %d, WORST: %d" %
          (insertion_sort.best_comp(), insertion_sort.worst_comp()))
    Colors.log("%.4d" % insertion_sort.exchanges, "EXCHANGES")
    print("--- BEST: %d, WORST: %d" %
          (insertion_sort.best_exch(), insertion_sort.worst_exch()))

    print("ARRAY", a)


if __name__ == "__main__":
    main()
