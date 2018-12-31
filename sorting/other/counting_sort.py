from sorting.comparison_sort import ComparisonSort
from random import randint


class CountingSort(ComparisonSort):
    def sort(self, array, n):
        self.n = len(array)
        c = [0 for _ in range(n + 1)]
        for i in array:
            c[i] += 1

        for i in range(n + 1):
            if self.less(0, i):
                c[i] += c[i - 1]

        a_ = array[:]
        for i in a_:
            array[c[i] - 1] = i
            c[i] -= 1
            self.exchanges += 1


def main():
    counting_sort = CountingSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    counting_sort.sort(a, 99)
    counting_sort.print_array(a)


if __name__ == "__main__":
    main()
