reg_x = 1
current_cycle = 0
signal = 0

add_cycles = 2

def do_cycle(reg_x):
    global current_cycle
    ret = 0
    current_cycle += 1
    if (current_cycle % 40) == 20:
        ret = reg_x * current_cycle
    return ret

with open("input.txt", "r") as f:
    for next_line in f:
        next_line = next_line.strip()
        if next_line == "":
            continue
        if next_line == "noop":
            signal += do_cycle(reg_x)
        if next_line.startswith("addx"):
            amount = int(next_line.split(" ")[1])
            for i in range(add_cycles):
                signal += do_cycle(reg_x)
            reg_x += amount

print(signal)          