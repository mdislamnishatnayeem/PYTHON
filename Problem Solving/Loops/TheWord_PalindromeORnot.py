"""ইউজার একটি শব্দ ইনপুট দেবে। আমাদের প্রোগ্রাম দেখবে সেটি 
একটি প্যালিনড্রোম (Palindrome) কি না! প্যালিনড্রোম হলো কোনো
 শব্দ, সংখ্যা বা সিক্যুয়েন্স যাদের ওলটালেও ওই এক জিনিসই থাকে।
 যেমন : 707 কে ওলটালেও 707 ই থাকে। আবার Madam-কে 
ওলটালে Madam ই থাকে।

=>আমরা ইউজারের কাছে থেকে একটা ওয়ার্ড (স্ট্রিং) ইনপুট নিয়েছি।
 word[::-1] দিয়ে আমরা ওয়ার্ডটাকে রিভার্স করেছি মানে উল্টে 
দিয়েছি। তারপর নরমাল ওয়ার্ড আর রিভার্সড ওয়ার্ডের মধ্যে তুলনা 
করে সিদ্ধান্ত নিয়েছি। (casefold ফাংশনের কাজ হলো পুরো string 
কে lower case এ পরিণত করা.

"""
#             The python Code
#___________________________________________________


print('Please input your word:')
word = input()
word = word.casefold()
reversed_word = word[::-1]

if word == reversed_word:
    print('Great! It is a pallindrome.')
else:
    print('LOL! It is not a pallindrome.')
