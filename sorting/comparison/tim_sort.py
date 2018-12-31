from sorting.comparison_sort import ComparisonSort

from random import randint


class TimSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        run = 32
        for low in range(0, self.n, run):
            mid = self.min(low + 31, self.n - 1)
            self._insertion(array, low, mid)
        size = run
        while self.less(size, self.n):
            for low in range(0, self.n, 2 * size):
                mid = self.min(low + size - 1, self.n - 1)
                high = self.min(low + 2 * size - 1, self.n - 1)
                self._combine(array, low, mid, high)
            size *= 2

    def _insertion(self, a, low, high):
        for i in range(low, high + 1):
            for j in range(i, low, -1):
                if self.less(a[j], a[j - 1]):
                    self.exch(a, j, j - 1);
                else:
                    break

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
    tim_sort = TimSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    tim_sort.sort(a)
    tim_sort.print_array(a)


if __name__ == "__main__":
    main()
