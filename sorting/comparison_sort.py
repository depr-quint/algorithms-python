from test.colors import Test, Colors


class ComparisonSort:
    def __init__(self):
        self.comparisons = 0
        self.exchanges = 0
        self.n = 0

    def less(self, e1, e2):
        self.comparisons += 1
        return True if e1 < e2 else False

    def less_or_equal(self, e1, e2):
        self.comparisons += 1
        return True if e1 <= e2 else False

    def exch(self, array, idx1, idx2):
        self.exchanges += 1
        array[idx1], array[idx2] = array[idx2], array[idx1]

    def min(self, one, two):
        return one if self.less(one, two) else two

    def print_array(self, a):
        print("LENGTH %d" % self.n)
        Test.is_sorted(a)
        Colors.log("%.4d" % self.comparisons, "COMPARES ")
        Colors.log("%.4d" % self.exchanges, "EXCHANGES")
        print("ARRAY", a)
