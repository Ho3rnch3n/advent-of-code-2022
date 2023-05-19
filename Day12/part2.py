import heapq
import string
import copy

def find_steps(start_pos, stop_pos, hill_map):
    y_max = len(hill_map) - 1
    x_max = len(hill_map[0]) - 1

    queue = [(0,[start_pos[0],start_pos[1]])]
    heapq.heapify(queue)

    while True:
        try:
            steps,(y,x) = heapq.heappop(queue)
        except:
            return 999

        if hill_map[y][x]["visited"]:
            continue

        hill_map[y][x]["steps"] = steps
        hill_map[y][x]["visited"] = True

        if y == stop_pos[0] and x == stop_pos[1]:
            return hill_map[y][x]["steps"]
            

        for dy,dx in [[y,x-1],[y-1,x],[y,x+1],[y+1,x]]:
            if dy < 0 or dx < 0 or y_max < dy or x_max < dx:
                continue
            if hill_map[dy][dx]["visited"]:
                continue
            current_hight = hill_map[y][x]["height"]
            if hill_map[dy][dx]["height"] not in range(current_hight+2):
                continue
            heapq.heappush(queue,(steps + 1,[dy, dx]))

with open("input.txt","r") as f:
    hill_map = []
    
    start_pos = []
    stop_pos = None

    for y, line in enumerate(f):
        line = line.strip()
        positions = []
        for x, pos in enumerate(line):
            if pos == "S":
                pos = "a"
            if pos == "E":
                stop_pos = (y,x)
                pos = "z"
            if pos == "a":
                start_pos.append((y,x))
            positions.append({"steps": 0, "height": string.ascii_lowercase.index(pos), "visited": False})

        hill_map.append(positions)

solutions = []

for next_start in start_pos:
    solutions.append(find_steps(next_start, stop_pos, copy.deepcopy(hill_map)))


solutions.sort()
print(solutions[0])