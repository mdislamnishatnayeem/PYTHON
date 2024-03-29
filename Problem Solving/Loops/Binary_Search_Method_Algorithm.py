"""এখন আমরা অনন্ত জলিলের খোঁজ দ্য সার্চ-এর প্রবলেম সলভ করব।
ধরা যাক, ছোট থেকে বড় সাজানো বিভিন্ন সংখ্যার একটা তালিকা আছে। 
তালিকাটা নিচের মতো—
  1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56,
 65, 77, 94, 100

এই তালিকা থেকে ইউজারের ইনপুট দেওয়া নির্দিষ্ট একটি সংখ্যা খোঁজ দ্য 
সার্চ করে বের করতে হবে। এ আর কঠিন কী!
==আমরা যে সংখ্যাটা খুঁজছি সেটাকে বের করার জন্য আমরা একটা ট্যাকটিস 
ফলো করেছি। আমরা প্রথমে লিস্টের ঠিক মধ্যখানের সংখ্যাটা বের করেছি। 
তারপর দেখেছি এটাই আমাদের সংখ্যা কি না। যদি না হয় তখন দেখেছি
 আমাদের সংখ্যাটা এটার তুলনায় ছোট নাকি বড়। ছোট হলে, মধ্যখানের 
সংখ্যাটার বামের সব সংখ্যা লিস্ট হিসেবে বিবেচনায় নিয়েছি। আর বড় হলে 
মধ্যখানের সংখ্যাটার ডানের সব সংখ্যা লিস্ট হিসেবে বিবেচনায় নিয়েছি। 
তারপর লিস্ট হিসেবে বিবেচনায় নেওয়া সংখ্যাগুলোর ভেতর আগের সিস্টেম 
চালিয়েছি যতক্ষণ না নির্দিষ্ট সংখ্যাটা খুঁজে পাওয়া যায়। এভাবে দুভাগ করে 
করে খোঁজ দ্য সার্চ করার এই পদ্ধতিকে বলে বাইনারি সার্চ মেথড।
"""
#             The Python Code:
#___________________________________________________________

my_list = [1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]

print('Input the number:')
number = int(input())

first = 0
last = len(my_list)-1
found = False
cycle = 0

while first <= last and not found:
    midpoint = (first + last)//2
    if(my_list[midpoint] == number):
        found =True
    else:
        if(my_list[midpoint]>number):
            last = midpoint-1
        else:
            first = midpoint+1
    cycle +=1

print('Found the number after', cycle, 'cycle.')
