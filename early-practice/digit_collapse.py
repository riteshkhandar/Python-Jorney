
# find sum of num util signle digit is left

num = int(input("enter a number :"))


while num >10:
    sum = 0

    while num != 0 :



      last_digit = num % 10 

      sum = sum+last_digit

      num = num //10
    
    num = sum


print(num)



