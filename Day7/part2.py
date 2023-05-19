pwd = []
file_struct = {"/": {}}

max_disk_space = 70000000
disk_size_needed = 30000000

def get_current_dir():
    current_dir = None
    for next_layer in pwd:
        if next_layer == "/":
            current_dir = file_struct["/"]
            continue
        current_dir = current_dir[next_layer]
    return current_dir

def parse_ls_line(ls_line):
    sizeordir, name = ls_line.split(" ")
    size = -1
    dir = False
    try:
        size = int(sizeordir)
    except:
        dir = True
        size = -1
    
    return dir, size, name

def parse_ls(f):
    while True:
        file_pos = f.tell()
        next_line = f.readline()
        if not next_line:
            break
        next_line = next_line.strip()
        if next_line == "":
            continue
        if next_line[0] == "$":
            # return to last line because we need to parse it outside
            f.seek(file_pos)
            break
        else:
            isdir, size, name = parse_ls_line(next_line)
            current_dir = get_current_dir()
            if isdir:
                current_dir[name] = {}
            else:
                current_dir[name] = size



def parse_cd(cd_command):
    global pwd
    cd = cd_command.split(" ")[2]
    cd = cd.strip()
    if cd == "/":
        pwd = ["/"]
    elif cd == "..":
        pwd.pop()
    else:
        pwd.append(cd)

def get_dir_size(dir):
    size = 0
    for next_item in dir.values():
        if type(next_item) == dict:
            size += get_dir_size(next_item)
        else:
            size += next_item
    return size

def calculate_solution(size_currently_used, dir):
    candidates = []
    this_size = 0
    for next_name, next_item in dir.items():
        if type(next_item) == dict:
            this_size += get_dir_size(next_item)
            candidates.extend(calculate_solution(size_currently_used, next_item))
        else:
            this_size += next_item
    if size_currently_used - this_size <= max_disk_space - disk_size_needed:
        candidates.append(this_size)
        return candidates
    else:
        return candidates
        

with open("input.txt","r") as f:
    while True:
        next_line = f.readline()
        if not next_line:
            break
        next_line = next_line.strip()
        if next_line == "":
            continue
        if next_line[0] == "$":
            if next_line.startswith("$ cd"):
                parse_cd(next_line)
            if next_line.startswith("$ ls"):
                parse_ls(f)


size_currently_used = get_dir_size(file_struct)

# root is in there two times...
delete_candidates = calculate_solution(size_currently_used, file_struct)[:-1]

delete_candidates.sort()

print(delete_candidates[0])