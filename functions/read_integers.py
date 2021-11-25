def read_integers(filename):
    with open(filename) as f:
        return list(map(int, f))
