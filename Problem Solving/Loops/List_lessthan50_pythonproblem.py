"""ধরা যাক, বিভিন্ন সংখ্যার একটি তালিকা রয়েছে। তালিকাটা
 নিচের মত -
13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 
91, 58, 52, 82, 70, 43, 88, 55, 97, 16, 22,
 25, 79, 85, 40, 64, 94, 67, 37
এই তালিকা থেকে ৫০-এর চেয়ে ছোট সংখ্যাগুলোকে নিয়ে 
একটি লিস্ট বানিয়ে আউটপুট হিসেবে দেখাতে হবে।
""" 
#            The python code
#______________________________________________
a = [13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 91, 58, 52, 82, 70, 43, 88, 55, 97, 16, 22, 25, 79, 85, 40, 64, 94, 67, 37]
my_list = []

for i in a:
    if i < 50:
        my_list.append(i)

print(my_list)