a = 0
b = 1
print("Fibonacci series is :")
print(a)
print(b)
for c in range(0,10,1):
    c = a + b
    print(c)
    a = b
    b = c
