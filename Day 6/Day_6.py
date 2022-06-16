from collections import Counter
import time

start_time = time.time()

def num_of_fish(Input_File):
    with open(Input_File) as f:
        my_list_of_fish_str = f.read().split(",")

    my_list_of_fish_int = [int(fish) for fish in my_list_of_fish_str]
    
    my_dict_of_fish_timers = dict(Counter(my_list_of_fish_int))

    for i in range(9):
        if i not in my_dict_of_fish_timers.keys():
            my_dict_of_fish_timers[i] = 0

    i = 0

    while i < 256:
        fish = {j:0 for j in range(9)}
        for t,f in my_dict_of_fish_timers.items():
            new_t = t-1
            if new_t >= 0:
                fish[new_t] += f
            else:
                fish[6] += f 
                fish[8] += f
        my_dict_of_fish_timers = fish

        i += 1
    
    total = 0

    for value in fish.values():
        total += value
    
    return total
    
print(num_of_fish("Input.txt"))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
