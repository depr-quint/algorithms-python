from random import shuffle
from sorting.comparison_sort import ComparisonSort

from random import randint


class QuickSort(ComparisonSort):
    def sort(self, array):
        shuffle(array)
        self.n = len(array)
        self._quick(array, 0, self.n - 1)

    def _quick(self, array, low, high):
        if low < high:
            j = self._partition(array, low, high)
            self._quick(array, low, j - 1)
            self._quick(array, j + 1, high)

    def _partition(self, array, low, high):
        p, left, right = array[low], low + 1, high

        done = False
        while not done:
            while self.less_or_equal(left, right) and self.less_or_equal(array[left], p):
                left += 1
            while self.less_or_equal(left, right) and self.less_or_equal(p, array[right]):
                right -= 1
            if self.less(right, left):
                done = True
            else:
                self.exch(array, left, right)
        self.exch(array, low, right)

        return right


def main():
    quick_sort = QuickSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    quick_sort.sort(a)
    quick_sort.print_array(a)


if __name__ == "__main__":
    main()
