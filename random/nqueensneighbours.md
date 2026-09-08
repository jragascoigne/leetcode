from itertools import combinations

def n_queens_neighbours(state):
    return sorted(
        state[:i] + (state[j],) + state[i+1:j] + (state[i],) + state[j+1:]
        for i, j in combinations(range(len(state)), 2)
    )
