from sorting.comparison_sort import ComparisonSort
from random import randint
from math import floor


class ShellSort(ComparisonSort):
    def sort(self, array):
        self.n = len(array)
        gap = floor(self.n / 2)
        while self.less(0, gap):
            for i in range(gap, self.n):
                tmp, j = array[i], i
                while self.less_or_equal(gap, j) and self.less(tmp, array[j - gap]):
                    array[j], j = array[j - gap], j - gap
                array[j] = tmp
                self.exchanges += 1
            gap = floor(gap / 2)


def main():
    shell_sort = ShellSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    shell_sort.sort(a)
    shell_sort.print_array(a)


if __name__ == "__main__":
    main()
