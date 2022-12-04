result_dict = {	"A Y": 4,
		"B Y": 5,
		"C Y": 6,
		"A X": 3,
		"B X": 1,
		"C X": 2,
		"A Z": 8,
		"B Z": 9,
		"C Z": 7}

score = 0
with open("input.txt", "r") as f:
	for next_line in f:
		score += result_dict[next_line.strip()]

print(score)
