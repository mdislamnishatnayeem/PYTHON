"""A = {1, 2, 3, 4, 5} ও B = {5, 6, 7, 8} দুটি সেট।
 union() ও intersection() ফাংশন (আসলে মেথড) ব্যবহার 
না করে তাদের ইউনিয়ন ও ইন্টারসেকশন সেট C বের করতে হবে।
অর্থাৎ শুধুমাত্র লুপ সিস্টেম টা ইউজ করতে হবে:set এর কোন
 ফাংশন ইউজ করা যাবে না।
"""
#            The python code
___________________________________________________

A = {1, 2, 3, 4,47,27,85,76,5,5}
B = {5,6, 7,5,5 ,8}
C=[]
D=[]
#intersection সেটের অংশ বা আলগরিদম:
for i in A:
    for j in B:
        if(i==j):
           C.append(i)
   

# universal set এর অংশ বা অ্যালগরিদম:
for x in A:
    if(x not in B):
        D.append(x)
          
for y in B:
    if(y not in A):
        D.append(y)

for z in C:
    D.append(z)



#ফলাফল প্রিন্ট এর অংশ
print(set(C))
print(set(D))
        
      
