from sorting.comparison_sort import ComparisonSort
from random import randint


class BubbleSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                if self.less(array[j + 1], array[j]):
                    self.exch(array, j, j + 1)


def main():
    bubble_sort = BubbleSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    bubble_sort.sort(a)
    bubble_sort.print_array(a)


if __name__ == "__main__":
    main()
