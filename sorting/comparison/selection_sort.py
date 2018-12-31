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


def main():
    selection_sort = SelectionSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    selection_sort.sort(a)
    selection_sort.print_array(a)


if __name__ == "__main__":
    main()
