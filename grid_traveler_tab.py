def grid_traveler(n, m):
    grid = [[0] * n for _ in range(m)]
    grid[0][0] = 1
    pprint(grid)
    for i in range(n):
        for j in range(m):
            current = grid[i][j]
            if i + 1 < n:
                grid[i + 1][j] += current
            if j + 1 < m:
                grid[i][j + 1] += current
    pprint(grid)
    return grid[n - 1][m - 1]

def pprint(grid):
    print("------")
    for row in grid:
        print(row)

print(grid_traveler(3, 3)) # 6