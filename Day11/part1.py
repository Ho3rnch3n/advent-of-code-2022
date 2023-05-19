
class monkey:

    def __init__(self,monkey_string):
        self.inspect_count = 0
        self.items = []
        parts = monkey_string.split("\n")
        item_string = parts[1].split(":")[1]
        for next_item in item_string.split(","):
            self.items.append(int(next_item))

        operation_string = parts[2].split("=")[1]
        if "*" in operation_string:
            operation_parts = operation_string.split("*")
            try:
                val = int(operation_parts[1])
                self.operation = lambda x: x*val
            except:
                self.operation = lambda x: x*x
        if "+" in operation_string:
            operation_parts = operation_string.split("+")
            try:
                val = int(operation_parts[1])
                self.operation = lambda x: x+val
            except:
                self.operation = lambda x: x+x
        
        test_string = parts[3].split(" ")
        self.test_value = int(test_string[5])

        true_string = parts[4].split(":")[1]
        self.test_true = int(true_string.split(" ")[4])

        false_string = parts[5].split(":")[1]
        self.test_false = int(false_string.split(" ")[4])

    def test(self, item_val):
        self.inspect_count += 1
        if item_val % self.test_value == 0:
            return self.test_true
        else:
            return self.test_false

    

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

monkeys = []

for monkey_string in data:
    next_monkey = monkey(monkey_string)
    monkeys.append(next_monkey)

# round
for round_num in range(20):
    # monkeys turns:
    for next_monkey in monkeys:
        # inspect items
        while next_monkey.items:
            next_item = next_monkey.items.pop(0)
            next_item = next_monkey.operation(next_item) // 3

            throw_monkey = next_monkey.test(next_item)

            monkeys[throw_monkey].items.append(next_item)

inspect_counts = []

for next_monkey in monkeys:
    inspect_counts.append(next_monkey.inspect_count)

inspect_counts.sort(reverse=True)

print(inspect_counts[0] * inspect_counts[1])