with open("input.txt", "r") as f:
    data = f.read()

grid = []

for next_line in data.split("\n"):
    line = []
    if next_line == "":
        continue
    next_line = next_line.strip()
    for tree in next_line:
        line.append(int(tree))
    
    grid.append(line)

grid_height = len(grid)
grid_width = len(grid[0])

# trees visible because they are on the outside
trees_visible = grid_height * 2 + (grid_width - 2) * 2

for y in range(1,grid_height - 1):
    for x in range(1,grid_width - 1):
        this_height = grid[y][x]
        # look top
        max_top = max(list(zip(*grid))[x][:y])
        if max_top < this_height:
            trees_visible += 1
            continue
        # look bottom
        max_bottom = max(list(zip(*grid))[x][y + 1:])
        if max_bottom < this_height:
            trees_visible += 1
            continue
        # look left
        max_left = max(grid[y][:x])
        if max_left < this_height:
            trees_visible += 1
            continue
        # look right
        max_right = max(grid[y][x + 1:])
        if max_right < this_height:
            trees_visible += 1
            continue

print(trees_visible)