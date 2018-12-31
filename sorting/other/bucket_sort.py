from sorting.comparison_sort import ComparisonSort
from sorting.comparison.insertion_sort import InsertionSort
from random import randint
from math import floor, ceil


class BucketSort(ComparisonSort):
    def sort(self, array, n):
        self.n = len(array)
        m = 0
        for i in range(self.n):
            if self.less(m, array[i]):
                m = array[i]

        divider = ceil((m + 1) / n)
        buckets = []
        for k in range(n):
            buckets.append([])
        for i in range(self.n):
            buckets[floor(array[i] / divider)].append(array[i])
        for b in buckets:
            insertion = InsertionSort()
            insertion.sort(b)
            self.exchanges += insertion.exchanges
            self.comparisons += insertion.comparisons

        k = 0
        for i in range(len(buckets)):
            for j in range(len(buckets[i])):
                array[k] = buckets[i][j]
                k += 1


def main():
    bucket_sort = BucketSort()
    a = [randint(0, 99) for _ in range(20)]
    print("ARRAY", a)
    bucket_sort.sort(a, 4)
    bucket_sort.print_array(a)


if __name__ == "__main__":
    main()
