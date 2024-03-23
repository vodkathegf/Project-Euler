# Starting in the top left corner of a  2 * 2 grid, and only being able to move to the right and down,
#  there are exactly 6 routes to the bottom right corner.
# how many routes are there in 20 * 20 grid

def count_paths(grid_size):
    paths_grid = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]
    
    for i in range(grid_size + 1):
        paths_grid[i][grid_size] = 1
        paths_grid[grid_size][i] = 1

    for i in range(grid_size - 1,-1,-1):
        for j in range(grid_size -1 ,-1,-1):
            paths_grid[i][j] = paths_grid[i +1 ][j] + paths_grid[i][j+1]

    return paths_grid[0][0]

grid_size = 20

result = count_paths(grid_size)

print(f"there are {result} routes in 20 * 20 sized grid")