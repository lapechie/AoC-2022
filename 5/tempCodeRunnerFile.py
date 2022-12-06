import re

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
            #stacks[i + 1] 
            file.seek(0)
            x = x + 4
            y = y + 4
    return stacks

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

temp_stack = []

for i in range(len(move_list)):

    #print("Move {0} from {1} to {2}".format(move_list[i], from_list[i], to_list[i]))

    #for key, value in stacks.items():
        #print(key, value)

    for j in range(move_list[i]):
        lift_item = stacks[from_list[i]].pop()
        temp_stack.append(lift_item)
    for k in range(len(temp_stack)):
        drop_item = temp_stack.pop()
        stacks[to_list[i]].append(drop_item)

for key, value in stacks.items():
    print(key, value)