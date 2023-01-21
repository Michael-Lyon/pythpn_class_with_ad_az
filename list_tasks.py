# Take 10 integer inputs from user and store them in a list and print them on screen.

number_list = []
count = 1
while count <= 10:
    value = int(input(f"Enter a number({count}): "))
    number_list.append(value)
    count = count + 1
print(number_list)
    
    
    
for num in number_list:
    if num % 2 == 0:
        print(num)
    else:
        print("ODD!!!!")