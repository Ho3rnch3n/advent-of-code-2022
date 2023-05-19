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

max_vision_score = 0

def get_score(tree_list, this_height):
    score = 0
    if this_height > max(tree_list):
        score = len(tree_list)
    else:
        for i, next in enumerate(tree_list):
            if next >= this_height:
                score = i + 1
                break
    return score

for y in range(1,grid_height - 1):
    for x in range(1,grid_width - 1):
        this_height = grid[y][x]
        vertical_list = list(zip(*grid))[x]
        horizontal_list = grid[y]

        # look top
        top_list = vertical_list[:y][::-1]
        top_score = get_score(top_list, this_height)

        # look bottom
        bottom_list = vertical_list[y + 1:]
        bottom_score = get_score(bottom_list, this_height)

        # look left
        left_list = horizontal_list[:x][::-1]
        left_score = get_score(left_list, this_height)

        # look right
        right_list = horizontal_list[x + 1:]
        right_score = get_score(right_list, this_height)
        
        this_score = top_score * bottom_score * left_score * right_score
        if max_vision_score < this_score:
            max_vision_score = this_score

print(max_vision_score)