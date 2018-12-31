from sorting.comparison_sort import ComparisonSort
from random import randint


class HeapSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify(array, self.n, i)
        for i in range(self.n - 1, 0, -1):
            self.exch(array, 0, i)
            self._heapify(array, i, 0)

    def _heapify(self, array, n, i):
        c, l, r = i, 2 * i + 1, 2 * i + 2
        if self.less(l, n) and self.less(array[c], array[l]):
            c = l
        if self.less(r, n) and self.less(array[c], array[r]):
            c = r
        if c != i:
            self.exch(array, i, c)
            self._heapify(array, n, c)


def main():
    heap_sort = HeapSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    heap_sort.sort(a)
    heap_sort.print_array(a)


if __name__ == "__main__":
    main()
