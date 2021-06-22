"""ইউজার যেকোনো একটা পূর্ণসংখ্যা ইনপুট দেবে। আর ওই 
পূর্ণসংখ্যার নামতা আউটপুট হিসেবে দেখাতে হবে।"""
#              The python code
#____________________________________________

print('Please, input the number:')
number = int(input())
count = 1
while count <= 10:
    print(number, 'x', count, '=', number*count)
    count += 1
