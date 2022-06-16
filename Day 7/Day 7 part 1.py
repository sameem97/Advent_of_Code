with open("Input.txt") as f:
    my_list_of_h_positions_str = f.read().split(",")

my_list_of_h_positions_int = [int(_) for _ in my_list_of_h_positions_str]

max_h = max(my_list_of_h_positions_int)
min_h = min(my_list_of_h_positions_int)

def find_optimal_h(input):
    fuel_for_all_h = {}
    for t in range(min_h, max_h):
        fuel_used = 0
        for h in my_list_of_h_positions_int:
            delta = abs(h - t)
            fuel_used += delta
        fuel_for_all_h[fuel_used] = t
    return min(fuel_for_all_h.items())

print(find_optimal_h("Input.txt"))
        