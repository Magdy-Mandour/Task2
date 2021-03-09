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
        new_list.append(int(i))
new_list.sort(reverse=True)        
for x in new_list:
    print(x)
######################################
# numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9]
new_numbers = set(numbers)
for i in new_numbers:
    if i == 'A':
        continue
    elif i == True:
        i = 1
    elif i == False:
        i = 0
    else:
        i = int(i)
    print(i)    