"""ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে। সেটির ওপর ভিত্তি 
করে আমরা *এর ত্রিভুজ ডিজাইন করব। অর্থাৎ ইউজার যদি 
5 ইনপুট দেয় তাহলে নিচের মত একটা ত্রিভুজ ডিজাইন করব।
*
**
***
****
*****
"""
#.             The python code
#______________________________________________
num=int(input("Input a number:"))
k=1
i=1
while(i<=num):
	for j in range(k):
		print("*",end='')
	k=k+1
	i+=1
	print()

"""এখন আমি যদি চাই Traingel টিউনটা ভাবে ডিজাইন হবে।
যেমন:

*****
****
***
**
*
তাহলে নিচের কোডটি লিখতে হতো

"""
num=int(input("Input the number:"))
for i in range(-1,num):
    for j in range(-1,num):
        	print('*',end='')
    num=num-1
    print()
