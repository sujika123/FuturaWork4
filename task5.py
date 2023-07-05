num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of digits
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit
   temp //= 10
print(sum)