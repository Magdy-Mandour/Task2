import math
numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9]
new_numbers = set(numbers)
new_list = []
for i in new_numbers:
    if i == 'A':
        continue
    elif i == True:
        i = 1
    elif i == False:
        i = 0
    else:
        i = int(i)
    #print(i)
    new_list.append(i)
new_list.sort(reverse=True)        
for x in new_list:
    print(x)
sum_first_last = new_list[0] + new_list[-1]  
print(sum_first_last)
sum_second_last = new_list[1] + new_list[-2]  
print(sum_second_last)
sum_third_last = new_list[2] + new_list[-3]  
print(sum_third_last)
mult_left_last = new_list[4] * new_list[-4]  
print(mult_left_last)