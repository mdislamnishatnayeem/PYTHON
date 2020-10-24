TEXT="Two ans two makes "
math=2+2
result=str(math)
print(TEXT +result)

#another code

x,y,z=(3,4,45)
print(x+y+z)
if x+y+z<=45:
    print("you are not old even now!congratulation")
elif x+y+z<=35:
    print("you are even young man")
else:
    print("you are old")
    
    

# the bellow code of multiplication(NAMOTA) is made by myself 
#But even also this code is not perfect at all,
#many things are missing here


i=0
while i<=9:
	i=i+1
	j=1
	while j<=10:
		gun=i*j
		j=j+1
		print( gun)

		
		
#Now i will try a very very general a function
#look bellow
def Function_sum():
    print("Say hello man")
    a,b=(45,32)
    sum=a+b
    print(sum)

Function_sum()
a,b=(31,68)
Function_sum()


#i use some general function here,look bellow

def summ(num1,num2):
    sum=num1+num2
    print(sum)
summ(45,65)#output will=110
summ(45,5832409)#output will=5832454
print("--------")
def sammm(digit1=20,digit2=45):#here 20 and 45 amout is set as
    summ=digit1+digit2         #defalt!if we donot give any input
    print(summ)                #then the compiler will automically set it

sammm(65345,28372)#here the defalt value doesnt need to work
sammm()#here the defalt value will work
