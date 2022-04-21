#opens input2.txt and saves each line as an input into my_list_str. splitlines() function used to remove line breaks before input.
with open("input2.txt") as inputs:
    my_list_str = inputs.read().splitlines()

#maps each string to an integer
integer_map = map(int, my_list_str)

#converts mapped output to a list of integers
my_list_int = list(integer_map)

#define count variable
count = 0 

#for loop over list
#sums to add the three consecutive elements
#conditional if statement to compare the two sums
#add 1 to current value of count if statement is true
for i in range(len(my_list_int)-3):
    sum1 = my_list_int[i] + my_list_int[i+1] + my_list_int[i+2]
    sum2 = my_list_int[i+1] + my_list_int[i+2] + my_list_int[i+3]
    if sum2 > sum1:
        count += 1
            
print(count)