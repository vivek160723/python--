#reverse of a number using while loop an counting the digits in the number.
num = int(input("Enter a number: "))
reverse = 0
count=0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
    count+=1


print("Reversed number:", reverse)
print("Total number of digits:",count)