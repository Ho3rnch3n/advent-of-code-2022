head_x = 0
head_y = 0

tail_x = 0
tail_y = 0

tail_visited = set([(0,0)])


def perform_move(dir,head_x, head_y, tail_x, tail_y):
    if dir == "U":
        # overlapping or same y position
        if head_y == tail_y:
            head_y += 1
        # not on same y but on same x
        elif head_x == tail_x:
            head_y += 1
            if tail_y != head_y:
                tail_y += 1
        # diagonal
        else:
            head_y += 1
            if tail_y != head_y:
                tail_y += 1
                tail_x = head_x
    elif dir == "D":
        # overlapping or same y position
        if head_y == tail_y:
            head_y -= 1
        # not on same y but on same x
        elif head_x == tail_x:
            head_y -= 1
            if tail_y != head_y:
                tail_y -= 1
        # diagonal
        else:
            head_y -= 1
            if tail_y != head_y:
                tail_y -= 1
                tail_x = head_x
    elif dir == "L":
        # overlapping or same x position
        if head_x == tail_x:
            head_x -= 1
        # not on same x but on same y
        elif head_y == tail_y:
            head_x -= 1
            if tail_x != head_x:
                tail_x -= 1
        # diagonal
        else:
            head_x -= 1
            if tail_x != head_x:
                tail_x -= 1
                tail_y = head_y

    elif dir == "R":
        # overlapping or same x position
        if head_x == tail_x:
            head_x += 1
        # not on same x but on same y
        elif head_y == tail_y:
            head_x += 1
            if tail_x != head_x:
                tail_x += 1
        # diagonal
        else:
            head_x += 1
            if tail_x != head_x:
                tail_x += 1
                tail_y = head_y
    return head_x, head_y, tail_x, tail_y


with open("input.txt","r") as f:
    for next_line in f:
        if next_line.strip == "":
            continue
        dir, amount = next_line.strip().split(" ")
        amount = int(amount)
        for i in range(amount):
            head_x, head_y, tail_x, tail_y = perform_move(dir,head_x, head_y, tail_x, tail_y)
            tail_visited.add((tail_x,tail_y))

print(len(tail_visited))