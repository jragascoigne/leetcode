from itertools import combinations

def n_queens_cost(state):
    return sum(
        abs(state[i] - state[j]) == abs(i - j)
        for i, j in combinations(range(len(state)), 2)
    )
