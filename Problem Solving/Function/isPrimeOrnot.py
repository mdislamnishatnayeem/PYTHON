def is_prime(n):
    if n <= 1:
        raise ValueError('The number must be greater than 1.')
    elif n <= 3:
        return True
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    else:
        i = 5
        while (i * i) <= n:
            if (n % i) == 0 or (n % i+2) == 0:
                return False
            i = i + 6
        return True

print('Please input your number:')
number = int(input())

if is_prime(number):
    print(number, 'is a prime number.')
else:
    print(number, 'is a composite number.')

#______________________________________________

"""is_prime() ফাংশনটি ট্রায়াল ডিভিশন মেথডের উপর ভিত্তি
 করে লেখা।

#__________________________________________________
The algorithm of the last programm of prime number:

i)যদি ১ বা তার সমান হয় তাহলে সংখ্যাটি কে অবশ্যই ১ এর 
চেয়ে বড় হতে হবে তা না হলে প্রোগ্রাম রান করবো না।

ii)৩ বা তার চেয়ে ছোট হলে (২)সংখ্যাটি প্রাইম।

iii)2 বা ৩ দ্বারা নিঃশেষে বিভাজ্য হলে সংখ্যাটি প্রাইম নয়।

iv)১১,১৭,২৩,২৯,৩৫,৪১,৪৭ ,৫৩---
i=5
যখন n>=i*i:
n যদি i অথবা i+2 দ্বারা নিঃশেষে বিভাজ্য হয় তাহলে সংখ্যাটি প্রাইম নয়।
n=n+6

___________________
১২৩ সংখ্যাটি কি প্রাইম?
=>
ii)2 বা 3 দ্বারা নিঃশেষে বিভাজ্য কিনা? বিভাজ্য হলে প্রাইম নয়।
এই শর্তটি সত্য না হলে পরের শর্তে যাবে -

123 এর ক্ষেত্রে iv নাম্বারে i এর যেসব মান দিয়ে আমরা নিঃশেষে
বিভাজ্য কিনা তা প্রমাণ করব সেই মান গুলো হল-
First round of the loop: 5,7
Second round of the loop:11,13
Third round: চলবে না loop

এই চারটি মান দ্বারা নিঃশেষে বিভাজ্য হলে প্রাইম নয়।
এই শর্তটি ও যদি সত্য না হয় তাহলে নাম্বারটি নিশ্চিত প্রাইম নাম্বার।

অন্যতায় যে কোন শর্তে /ক্ষেত্রে নাম্বারটি প্রাইম।

"""
