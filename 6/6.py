# read input
with open("6/6.in", "r") as file:
    for line in file:
        datastream = line

# part 1
x, y = 0, 4
for i in range(len(datastream)):
    print(list(datastream[x:y]))
    print(set(datastream[x:y]))
    if len(list(datastream[x:y])) == len(set(datastream[x:y])):
        break
    x += 1
    y += 1

print(y)

# part 2
x, y = 0, 14
for i in range(len(datastream)):
    print(list(datastream[x:y]))
    print(set(datastream[x:y]))
    if len(list(datastream[x:y])) == len(set(datastream[x:y])):
        break
    x += 1
    y += 1

print(y)