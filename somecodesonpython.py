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


## more codes on function 
"""
def wishCARD(name,wish="Happy birthday"):
    print(wish,name)
wishCARD("Nayeem",)
wishCARD("NAYEEM")
wishCARD("Nayeem","Happy friendship day")
print("\u2764\ufe0f")

"""
var=10
def summe():
    print(var)
summe()
def change():
    global var #here we declare that var is a global variable, so let us use it everywhere
               #boys! as we wish.
    var=var+1  #output=11 !!we cant change it like this,error will show
    print(var)
    loc=var   #we maked a copy of 'var' using 'loc' and now we
              # can do everything with 'loc' ,there will be no problem
    loc=loc+1 #output=12 !! like this
    print(loc)#here 12 will be print(11+1=12)
change()
print(var)  #output=11 ...when 'var' was used as a global variable !at that 
            # time we changed its value

def tryy():
    global var  # to change the value of var permanently we have to first declare it
               #as a 'global var/any variable',,,to change it and work with it
    var=var+4
    print(var)  #output=15!!!!!(11+4)=15
tryy()
