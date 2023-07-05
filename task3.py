print("Prime numbers between 1 and 100 :")
for n in range(1,100,1):
    if(n>1):
        for i in range(2,n,1):
            if(n % i == 0):
                break
        else:
            print(n)