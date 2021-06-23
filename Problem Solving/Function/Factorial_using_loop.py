while(1):
    number=int(input("Input the number: "))
    factorial=1
    while(number>0):
	      	factorial=factorial*number
      		number-=1
    print(factorial)


#Anotherway______________________________By_Maateen sir

print('Please input your number:')
number = int(input())
temp = number

while number > 1:
    number -= 1
    temp = temp*number

if temp == 0:
    print(1)
else:
    print(temp)
