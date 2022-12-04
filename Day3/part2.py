import string

priority_string = string.ascii_letters

res = 0
with open("input.txt","r") as f:
	group = []
	for next_line in f:
		group.append(next_line.strip())
		if len(group) < 3:
			continue

		common = list(set(group[0]) & set(group[1]) & set(group[2]))
		for next_chr in common:
			res += priority_string.index(next_chr) + 1
		group = []

print(res)
