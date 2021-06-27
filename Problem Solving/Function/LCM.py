def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)

print("Please input two integers:")
a, b = map(int, input().split())
print(lcm(a, b))


"""
দুটি সংখ্যার ল.সা.গু. বের করার একটা চমৎকার 
সূত্র আছে। দুটি সংখ্যার গুণফলকে ঐ দুটি সংখ্যার
গ.সা.গু. দিয়ে ভাগ করলে সংখ্যা দুটির ল.সা.গু. 
পাওয়া যায়"""
