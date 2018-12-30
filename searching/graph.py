class Graph:
    # todo: create random graphs

    graph = {
        #   A--B--C
        #  /|  |
        # S |  |    G
        #  \|  |   /
        #   D--E--F

        'a': ['s', 'd', 'b'],
        'b': ['e', 'c', 'a'],
        'c': ['b'],
        'd': ['s', 'e', 'a'],
        'e': ['f', 'd', 'b'],
        'f': ['g', 'e'],
        'g': ['f'],
        's': ['d', 'a'],
    }

    start = 's'
    goal = 'g'
    goals = ['g']
