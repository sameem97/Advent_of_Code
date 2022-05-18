import collections
import statistics
from statistics import mode
from venv import create

#my_list_str is the list of binaries
with open("Input.txt") as inputs:
    my_list_str = inputs.read().splitlines()

#define function that creates new list called 'counts' which is essentially a transpose of my_list_str
#each element in the list counts i.e. counts[0] can be visualised as a 'column' (or bit position) of my_list_str
def create_new_counts_list(my_list_str):
    counts = [[] for _ in range(len(my_list_str[0]))]
    for bin in my_list_str:
        for column, bit in enumerate(bin):
            counts[column].append(bit)
    return counts

#defined least common function here.
def least_common(array):
    return collections.Counter(array).most_common()[-1][0]

def oxygen_generator_rating(my_list_str):
    counts = create_new_counts_list(my_list_str)
    my_list_str_o = my_list_str[:]
    for index, _ in enumerate(counts):
        o_counts = create_new_counts_list(my_list_str_o)
        if o_counts[index].count("0") == o_counts[index].count("1"):
            for h_list in my_list_str_o[:]:
                if h_list[index] == "0":
                    my_list_str_o.remove(h_list)
        else:
            for h_list in my_list_str_o[:]:
                if mode(o_counts[index]) != h_list[index]:
                    my_list_str_o.remove(h_list)
    return my_list_str_o[0]

def co2_scrubber_rating(my_list_str):
    counts = create_new_counts_list(my_list_str)
    my_list_str_c = my_list_str[:]
    for index, _ in enumerate(counts):
        c_counts = create_new_counts_list(my_list_str_c)
        if c_counts[index].count("0") == c_counts[index].count("1"):
            for h_list in my_list_str_c[:]:
                if h_list[index] == "1":
                    my_list_str_c.remove(h_list)
        else:
            for h_list in my_list_str_c[:]:
                if least_common(c_counts[index]) != h_list[index]:
                    my_list_str_c.remove(h_list)
    return my_list_str_c[0]

o_rating = (int(oxygen_generator_rating(my_list_str),2))
c_rating = (int(co2_scrubber_rating(my_list_str), 2))
print(o_rating * c_rating)
