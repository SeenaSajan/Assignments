num_1 = float(input('enter the first number: '))
num_2 = float(input('enter the second number: '))
print('1. Addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')
select_operation = input ('which operation do you want to choose')
if select_operation  == '1':
    result = num_1 + num_2
elif select_operation  == '2':
    result = num_1 - num_2
elif select_operation  == '3':
    result = num_1 * num_2
else:
    result = num_1 / num_2
print(result)



   


