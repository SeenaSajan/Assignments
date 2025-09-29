num1=float(input('enter the first number: '))
num2=float(input('enter the second number: '))
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.floor")
print("7.Exponention")
operation=input('which operation do you want to perform: ')
if operation == "1" :
    result=num1+num2
elif operation=="2":
    result=num1-num2
elif operation=="3":
    result=num1*num2
elif operation=="4":
    result=num1/num2
elif operation=="5":
    result=num1%num2
elif operation=="6":
    result=num1//num2
elif operation=="7":
    result=num1**num2
else:
     result=print('wrong selection')
print(result)



#task 2
for i in range (1,6):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()
