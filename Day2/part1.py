result_dict = {	"A Y": 8,
		"B Y": 5,
		"C Y": 2,
		"A X": 4,
		"B X": 1,
		"C X": 7,
		"A Z": 3,
		"B Z": 9,
		"C Z": 6}

score = 0
with open("input.txt", "r") as f:
	for next_line in f:
		score += result_dict[next_line.strip()]

print(score)
