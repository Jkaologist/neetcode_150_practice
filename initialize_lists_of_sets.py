def build_lists_of_sets(N):
    cols = [set()] * N
    cols_again = [set() for _ in range(N)]
    cols_again_again = []
    for _ in range(N):
        cols_again_again.append(set())
    return cols == cols_again == cols_again_again


print(build_lists_of_sets(10))  # True
