ship_state_raw = ""
moves_raw = ""

def parse_move(move_str):
    next, ret_to = move_str.split("to")
    next, ret_from = next.split("from")
    _, ret_amout = next.split("move")
    return int(ret_amout), int(ret_from), int(ret_to)

with open("input.txt","r") as f:
    for next_line in f:
        if next_line.strip() == "":
            break
        ship_state_raw += next_line
    
    for next_line in f:
        moves_raw += next_line

ship_state_raw = ship_state_raw.split("\n")[:-1] # last part is empty

# last row has how many stacks there are one stack always is defined by 4 chars (exept the last one), so calculate amount by len + 1 / 4
stack_amount = (len(ship_state_raw[-1]) + 1) // 4

print(str(stack_amount) + " stacks detected")

stacks = [[] for i in range(stack_amount)]

# going through the layers in reverse order
for next_layer in ship_state_raw[-2::-1]:
    for i in range(stack_amount):
        if next_layer[i*4:i*4 + 3].strip() != "":
            stacks[i].append(next_layer[i*4+1])

moves = moves_raw.split("\n")

for move in moves:
    if move.strip() == "":
        continue
    move_amout, move_from, move_to = parse_move(move)
    # because we start with 0
    move_from -= 1
    move_to -= 1

    moved_chars = []
    for i in range(move_amout):
        moved_chars.append(stacks[move_from].pop())
    for next_char in moved_chars[-1::-1]:
        stacks[move_to].append(next_char)

sol = ""
for i in range(stack_amount):
    sol += stacks[i][-1]

print(sol)