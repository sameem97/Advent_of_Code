import collections
import statistics
from statistics import mode

#my_list_str is the list of binaries
with open("Input.txt") as inputs:
    my_list_str = inputs.read().splitlines()

#creates (dynamically) a number of empty lists. In this case, 12, based on the length of my_list_str[0]. All 12 lists stored under counts list i.e. this is a 2D list.
counts = [[] for _ in range(len(my_list_str[0]))]

#first line iterates over my_list_str
#second line: enumerate (bin) will return (index, value) i.e. it indexes the string. So you're looping over the string now i.e. going bit by bit.
#third line: for each 'bit' i.e. column essentially here, it appends the corresponding bit to the 12 empty lists within counts we created earlier. 
#i.e. see my_list_str[0] 011010010110 0 appends to counts[0], 1 appends to counts [1], 1 appends to counts [2] etc...
#essentially this section is a loop within a loop, appending each bit to the corresponding list within counts.
for bin in my_list_str:
    for (column, bit) in enumerate(bin):
        counts[column].append(bit)

#ESSENTIALLY UP TO THIS POINT WE'VE DONE A TRANSPOSE.

#defined least common function here.
def least_common(array):
    return collections.Counter(array).most_common()[-1][0]

#list comprehension, loops over each list in counts (which itself is a list of the column bits) and returns the mode of that list. 
#these mode values are stored in gamma_rate_list.
gamma_rate_list = [mode(count) for count in counts]
epsilon_rate_list = [least_common(count) for count in counts]

#.join is a string method which converts any iterable into a string. "" not anything here but if "-" would give you "1-0-1"
#int(value, 2) 2 defines what base you will be inputting in the value. By default assumes base 10. 
gamma_rate = int("".join(gamma_rate_list), 2)
epsilon_rate = int("".join(epsilon_rate_list), 2)

power_consumption = gamma_rate * epsilon_rate

print(f"Gamma Rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}\nPower Consumption: {power_consumption}")


