elvs = []
elv_num = 1
elv_cals = 0

with open("input.txt","r") as f:
	for next_line in f:
		if next_line.strip() == "":
			elvs.append(elv_cals)
			elv_num += 1
			elv_cals = 0
			continue
		elv_cals += int(next_line.strip())

elvs.sort(reverse=True)

cals = 0
for i in elvs[:3]:
	cals += i

print(cals)
