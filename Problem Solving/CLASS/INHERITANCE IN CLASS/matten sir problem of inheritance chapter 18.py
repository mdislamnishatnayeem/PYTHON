""" এবার বাড়ির কাজ। ক্লাস কন্সট্রাক্টর __init__() কে ওভাররাইড করে একটা সুপারক্যালকুলেটর ক্লাস বানিয়ে প্রোগ্রাম লিখতে হবে।
পারা যাবে তো? অবশ্যই। কারণ, মানুষ আমাদের পাশে আছে।"""

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a + self.b
    def Substraction(self):
        return self.a - self.b
    def Multiplication(self):
        return self.a * self.b
    def Division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return "The number can not be divided by 0"

class Supercalculator(Calculator):
    def __init__(self, a, b,c):
        super().__init__(a, b)
        self.c=c
    def squre(self):
        return self.c * self.c
    def cube(self):
        return self.c * self.c * self.c
        

A=int(input("GIVE NUMBER 1: "))
B=int(input("GIVE NUMBER 2: "))
C=int(input("GIVE NUMBER 3: "))
MYCALCULATOR=Supercalculator(A,B,C)
temp=MYCALCULATOR.addition()
print(A,"+",B,"= ",temp)
temp=MYCALCULATOR.Substraction()
print(A,"-",B,"= ",temp)
temp=MYCALCULATOR.Multiplication()
print(A,"*",B,"= ",temp)
temp=MYCALCULATOR.Division()
print(A,"/",B,"= ",temp)
temp=MYCALCULATOR.squre()
print(C,"*",C,"= ",temp)
temp=MYCALCULATOR.cube()
print(C,"*",C,"*",C,"= ",temp)
