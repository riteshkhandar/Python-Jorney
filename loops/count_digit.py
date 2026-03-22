# count digit in the integer
# Input: 12345
# Output: 5 digits


number = int(input("Enter a Number :"))

count = 0

while number!=0:

  number = number//10

  count+=1



print(count)

