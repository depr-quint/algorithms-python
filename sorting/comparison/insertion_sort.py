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


def main():
    insertion_sort = InsertionSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    insertion_sort.sort(a)
    insertion_sort.print_array(a)


if __name__ == "__main__":
    main()
