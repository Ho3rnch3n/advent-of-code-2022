with open("input.txt","r") as f:
    data = f.read()

data = data.strip()

sol = -1

marker_len = 14

for i in range(len(data)-marker_len + 1):
    chunk = data[i:i+marker_len]
    x = list(set(chunk))
    y = list(chunk)
    x.sort()
    y.sort()
    if x == y:
        sol = i + marker_len
        break

print(sol)