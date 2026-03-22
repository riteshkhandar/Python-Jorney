# Q1. Print numbers 1 to 10 using a for loop.

for i in range(1,11):
  print(i)

i = 1

while i<=10:
  print(i)
  i+=1

# Q2. Print even numbers 1 to 10 using a for loop.

for i in range(1,20):
  if i % 2 == 0:
    print(i)


# Q3. Print names in a list using a for loop.

names = ["Tony", "Sara", "John", "Emma"]

for i in names:
  print(i)

# Q4. Print multipliacation of  numbers with 5 from 1 to 10 using a for loop.

for i in range(1,11):
  print(5*i)

# Q5. sum numbers  1 to 100 using a for loop.

sum= 0

for i in range(1,101):

  sum = sum+i


print(sum)

# Q6. Print  reverse  numbers 10 to 1 using a for loop.

for i in range(10,0 ,-1):
  print(i)

# Q7. Print numbers  greater than 10 in a list  using a for loop.

numbers = [3, 15, 7, 22, 8, 19, 4]


for num in numbers:
  if num >10:
    print(num)

# Q8. ask for input until user not enter his name numbers 1 to 10 using a while loop.

while num == " ":
  num = (input('enter a number :'))

# Q9. Print factorial of number  using a while loop.

i = 1
fact=1

while i <=5:
  fact = fact*i
  i+=1


print(fact)  







