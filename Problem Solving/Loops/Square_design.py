"""ইউজার একটা পূর্ণসংখ্যা ইনপুট দেবে। সেটির ওপর ভিত্তি করে 
আমরা *এর স্কয়ার ডিজাইন করব। অর্থাৎ ইউজার যদি 5 ইনপুট
 দেয় তাহলে নিচের মতো একটা স্কয়ার ডিজাইন করব।
      *****
      *****
      *****
      *****
      *****

=>
   এখানে আমরা দুটি while লুপ (নেস্টেড লুপ) নিয়ে কাজ করেছি।
 বিষয়টা এ রকম যে একটা while লুপ দিয়ে আমরা *এর লাইন প্রিন্ট 
করব আর আরেকটা while দিয়ে আমরা লাইন ব্রেক নেব। ভেতরের 
লুপটাতে আমরা print('*', end='') ব্যবহার করেছি। print()
 ফাংশনটা যখন কাজ করে তখন সেটা স্ট্রিংয়ের শেষে নিজ থেকেই 
একটা \n যোগ করে নিউ লাইন প্রিন্ট করে দেয়। কিন্তু আমরা তো 
পাশাপাশি প্রিন্ট করব। সে ক্ষেত্রে নতুন একটা লাইন প্রিন্ট হলে ঝামেলা
 আমাদের জন্য। তাই আমরা প্রিন্ট ফাংশনকে বলে দিয়েছি যে বাপু, 
তোমার শেষে গিয়ে নতুন কিছু যোগ করার দরকার নেই। এবং বাইরের
 লুপের ভেতর আমরা print() ফাংশন ব্যবহার করেছি কিন্তু ভেতরে 
কোনো কিছু পাস করিনি। কিছু পাস করি আর না করি, সে কিন্তু নিজ 
উদ্যোগে একটা নিউ লাইন প্রিন্ট করতে ভুল করেনি।
"""
#            The python code
#__________________________________________________

number=int(input('Please, input the number:'))
temp = number

while number > 0:
    count = temp
    while count > 0:
        print('*', end='')
        count -= 1
    print()
    number -= 1
