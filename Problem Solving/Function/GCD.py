def gcd(a, b):
    if b > a:
        gcd(b, a) # Value of 'a' will be value
                  # of 'b'

                  # Value of 'b' will be value
                  # of 'a'
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

print("Please input two integers:")
a, b = map(int, input().split())
print(gcd(a, b))


"""
8)20(2
  16
 ________
  4)16(4
    16
    _____
     0
 The GCD:4
""'
