# find out the number is palindrome or not

num = int(input())

p_num=num 

rev=0

while num!=0:

  last_digit = num%10

  rev = rev*10+last_digit

  num = num//10


if rev==p_num:
  print("YES")
else:
  print("NO")