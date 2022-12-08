import re

# parse the starting stack
def read_start_stack():
    stacks = {}
    with open("5/5.in", "r") as file:
        x = 1
        y = 2
        z = len(file.readline())
        file.seek(0)
        for i in range(int(z/4)):
            l = []
            for line in file:
                if line.isspace():
                    break
                if isinstance(line[x:y], int):
                    break
                if line[x:y] == ' ':
                    continue
                l.append(line[x:y])
            l.pop()
            l.reverse()
            stacks[i + 1] = l
            file.seek(0)
            x = x + 4
            y = y + 4
    return stacks

# parse instructions 
def read_instruction(pattern):
    pattern = re.compile(pattern)
    match_list = []
    with open("5/5.in", "r") as file:
        for line in file:
            match = pattern.search(line)
            if match != None:
                match_list.append(int(match.group(0)))
    return match_list


stacks = read_start_stack()
move_list = read_instruction("(?<=move\s)[0-9]+")
from_list = read_instruction("(?<=from\s)[0-9]+")
to_list = read_instruction("(?<=to\s)[0-9]+")

# part 1
for i in range(len(move_list)):

    #print("Move {0} from {1} to {2}".format(move_list[i], from_list[i], to_list[i]))

    #for key, value in stacks.items():
        #print(key, value)

    for j in range(move_list[i]):
        pop_item = stacks[from_list[i]].pop()
        stacks[to_list[i]].append(pop_item)

for key, value in stacks.items():
    print(key, value[-1])

# part 2
stacks = read_start_stack()
for i in range(len(move_list)):

    #print("Move {0} from {1} to {2}".format(move_list[i], from_list[i], to_list[i]))

    #for key, value in stacks.items():
        #print(key, value)

    stacks[to_list[i]] += stacks[from_list[i]][-move_list[i]:]
    stacks[from_list[i]] = stacks[from_list[i]][:-move_list[i]]

for key, value in stacks.items():
    print(key, value[-1])

