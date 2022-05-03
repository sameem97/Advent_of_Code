import math

with open("Input.txt") as inputs:
    my_list_str = inputs.read().splitlines()

depth = 0
horizontal_position = 0

for i in range(len(my_list_str)):
    if my_list_str[i][:7] == "forward":
        horizontal_position += int(my_list_str[i][-1:])
    elif my_list_str[i][:4] == "down":
        depth += int(my_list_str[i][-1:])
    else:
        depth -= int(my_list_str[i][-1:])

area = depth * horizontal_position

print(f"Depth: {depth} \nHorizontal Position:{horizontal_position} \nArea: {area}")

