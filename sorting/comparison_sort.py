class ComparisonSort:
    def __init__(self):
        self.comparisons = 0
        self.exchanges = 0
        self.n = 0

    def less(self, e1, e2):
        self.comparisons += 1
        return True if e1 < e2 else False

    def exch(self, array, idx1, idx2):
        self.exchanges += 1
        array[idx1], array[idx2] = array[idx2], array[idx1]

    def best_comp(self):
        raise NotImplementedError

    def worst_comp(self):
        raise NotImplementedError

    def best_exch(self):
        raise NotImplementedError

    def worst_exch(self):
        raise NotImplementedError
