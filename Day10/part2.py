reg_x = 1
current_cycle = 0

full_picture = []

add_cycles = 2

def do_cycle(reg_x):
    global current_cycle
    global full_picture
    
    if current_cycle % 40 == reg_x -1 or current_cycle % 40 == reg_x or current_cycle % 40 == reg_x +1:
        full_picture.append(True)
    else:
        full_picture.append(False)
    
    current_cycle += 1
    return 

with open("input.txt", "r") as f:
    for next_line in f:
        next_line = next_line.strip()
        if next_line == "":
            continue
        if next_line == "noop":
            do_cycle(reg_x)
        if next_line.startswith("addx"):
            amount = int(next_line.split(" ")[1])
            for i in range(add_cycles):
                do_cycle(reg_x)
            reg_x += amount

for i,next in enumerate(full_picture):
    if next:
        print("#", end="")
    else:
        print(".", end="")
    if (i +1 )% 40 == 0:
        print("")