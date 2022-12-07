with open("1/1.in") as file:
    elves = {}
    calories = 0
    counter = 1
    for line in file:
        if not line.isspace():
            calories += int(line)
        if line.isspace():
            elves[counter] = calories
            counter += 1
            calories = 0
    
for key, value in elves.items():
    print(key, value)

# part 1
print(max(elves.values()))

# part 2
print(sorted(elves.values())[-1] + sorted(elves.values())[-2] +sorted(elves.values())[-3])


