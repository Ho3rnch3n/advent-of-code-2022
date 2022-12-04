import string

priority_string = string.ascii_letters

res = 0
with open("input.txt","r") as f:
	for next_line in f:
		next_line = next_line.strip()
		split = int(len(next_line) / 2)
		common = list(set(next_line[:split]) & set(next_line[split:]))
		for next_chr in common:
			res += priority_string.index(next_chr) + 1

print(res)
