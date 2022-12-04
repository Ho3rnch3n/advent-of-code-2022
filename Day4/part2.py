res = 0

with open("input.txt","r") as f:
	for next_line in f:
		elv_ranges = []
		elv_raw = next_line.strip().split(",")
		elv_raw_1 = list(map(int,elv_raw[0].split("-")))
		elv_raw_2 = list(map(int,elv_raw[1].split("-")))

		elv_range_1 = range(elv_raw_1[0],elv_raw_1[1] + 1)
		elv_range_2 = range(elv_raw_2[0],elv_raw_2[1] + 1)

		if (elv_range_1.start in elv_range_2 or elv_range_1[-1] in elv_range_2) or (elv_range_2.start in elv_range_1 or elv_range_2[-1] in elv_range_1):
			res += 1
print(res)
