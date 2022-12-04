elvs = {}
elv_num = 1
elv_cals = 0

with open("input.txt","r") as f:
	for next_line in f:
		if next_line.strip() == "":
			elvs[elv_num] = elv_cals
			elv_num += 1
			elv_cals = 0
			continue
		elv_cals += int(next_line.strip())

#print(elvs)
elv_max_num = max(elvs, key=elvs.get)
print("elv_num: " + str(elv_max_num))	
print("elv cals: " + str(elvs[elv_max_num]))
