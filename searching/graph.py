class Graph:
    # todo: create random graphs

    graph = {
        #    4   4
        #   A--B--C
        # 3/|  |
        # S |5 |5   G
        # 4\|  |   /3
        #   D--E--F
        #    2   4

        'a': ['s', 'd', 'b'],
        'b': ['e', 'c', 'a'],
        'c': ['b'],
        'd': ['s', 'e', 'a'],
        'e': ['f', 'd', 'b'],
        'f': ['g', 'e'],
        'g': ['f'],
        's': ['d', 'a'],
    }

    weights = {
        ('a', 'b'): 4, ('a', 'd'): 5, ('a', 's'): 3,
        ('b', 'a'): 3, ('b', 'c'): 4, ('b', 'e'): 5,
        ('c', 'b'): 4,
        ('d', 'a'): 5, ('d', 'e'): 2, ('d', 's'): 4,
        ('e', 'b'): 5, ('e', 'd'): 2, ('e', 'f'): 4,
        ('f', 'e'): 4, ('f', 'g'): 3,
        ('g', 'f'): 3,
        ('s', 'a'): 3, ('s', 'd'): 4,
    }

    start = 's'
    goal = 'g'
    goals = ['g']

    @staticmethod
    def cost(path, weights):
        return sum([weights[(path[i], path[i + 1])] for i in range(len(path) - 1)])
