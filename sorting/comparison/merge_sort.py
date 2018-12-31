from math import floor
from sorting.comparison_sort import ComparisonSort

from random import randint


class MergeSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        self._merge(array, 0, self.n - 1)

    def _merge(self, array, low, high):
        if self.less(low, high):
            mid = floor((low + (high - 1)) / 2)
            self._merge(array, low, mid)
            self._merge(array, mid + 1, high)
            self._combine(array, low, mid, high)

    def _combine(self, a, low, mid, high):
        l, r = mid - low + 1, high - mid
        left, right = [0] * l, [0] * r

        for i in range(0, l):
            left[i] = a[low + i]
        for j in range(0, r):
            right[j] = a[mid + 1 + j]

        i, j, k = 0, 0, low

        while self.less(i, l) and self.less(j, r):
            if self.less_or_equal(left[i], right[j]):
                a[k], i = left[i], i + 1
            else:
                a[k], j = right[j], j + 1
            self.exchanges += 1
            k += 1
        while self.less(i, l):
            a[k], i, k = left[i], i + 1, k + 1
            self.exchanges += 1
        while self.less(j, r):
            a[k], j, k = right[j], j + 1, k + 1
            self.exchanges += 1


def main():
    merge_sort = MergeSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    merge_sort.sort(a)
    merge_sort.print_array(a)


if __name__ == "__main__":
    main()
