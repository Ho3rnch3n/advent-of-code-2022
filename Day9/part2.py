rope_len = 10
rope = [[0,0] for x in range(rope_len)]

tail_visited = set([(0,0)])


def perform_move(dir, rope):
    move_x = 0
    move_y = 0
    if dir == "U":
        move_y = 1
    elif dir == "D":
        move_y = -1
    elif dir == "R":
        move_x = 1
    elif dir == "L":
        move_x = -1

    head = rope[0]
    tail = rope[1]

    head[0] += move_x
    head[1] += move_y

    for i in range(len(rope) - 1):
        head = rope[i]
        tail = rope[i+1]

        delta_x = head[0] - tail[0]
        delta_y = head[1] - tail[1]
        
        if delta_x > 1 or delta_x < -1 or delta_y > 1 or delta_y < -1:
            # overlapping or same y position
            if delta_y == 0:
                if delta_x > 1:
                    tail[0] += 1
                if delta_x < -1:
                    tail[0] -= 1
            # not on same y but on same x
            elif delta_x == 0:
                if delta_y > 1:
                    tail[1] += 1
                if delta_y < -1:
                    tail[1] -= 1
            # diagonal
            else:
                if delta_x >= 1:
                    tail[0] += 1
                if delta_x <= -1:
                    tail[0] -= 1
                if delta_y >= 1:
                    tail[1] += 1
                if delta_y <= -1:
                    tail[1] -= 1
    return



with open("input.txt","r") as f:
    for next_line in f:
        if next_line.strip == "":
            continue
        dir, amount = next_line.strip().split(" ")
        amount = int(amount)
        for i in range(amount):
            perform_move(dir, rope)
            
            tail_visited.add((rope[-1][0],rope[-1][1]))

print(len(tail_visited))