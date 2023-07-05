n = int(input("Enter the range : "))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i

av = sum/n
print("Average of", n, "numbers = ",av)
