

i = 1
 

while i <=100:
  print (i)
  i+=1

i = 1
numbers = []

while i <=100:
  numbers.append(i)
  i+=1


numbers.sort(reverse=True)
print(numbers)



num = int(input("enter a num :"))


i = 1

while i<=10:
  print(num*i)

  i+=1

list = [1,2,3,4,5,6,7,8,9,10]


i = 0 

while i<= len(list)-1:
  print(list[i])
  i +=1


tup = (1,2,3,4,5,6,7,8,9,10)

check = int(input("enter number to check :"))

i = 0



while i<= len(tup)-1:

  if (tup[i]==check):
     print(f" the number {tup[i]} found at idx {i}")
     break

 

  i+=1


