from collections import Counter

with open("Input.txt") as f:
    my_list_of_lines = f.read().splitlines()

def split_coords(input):
    splitted_coords = []
    for line in input:
        splitted_coords.append([coord for coords in line.split(' -> ') for coord in coords.split(",")])
    return splitted_coords

splitted_coords = split_coords(my_list_of_lines)

my_full_list_of_coordinates = []

for line in splitted_coords:
    if line[0] == line[2]:
        diff = abs(int(line[1]) - int(line[3]))
        starting_y = min(int(line[1]), int(line[3]))
        for i in range(starting_y, starting_y + diff + 1):
            my_full_list_of_coordinates.append(f'{line[0]},{i}')
    elif line[1] == line[3]:
        diff = abs(int(line[2]) - int(line[0]))
        starting_x = min(int(line[2]), int(line[0]))
        for i in range(starting_x, starting_x + diff + 1):
            my_full_list_of_coordinates.append(f'{i},{line[1]}')

# print(my_full_list_of_coordinates)

counter = Counter(my_full_list_of_coordinates)

total = 0

for value in counter.values():
    if value > 1:
        total += 1

print(total)