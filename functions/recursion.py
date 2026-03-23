# Problem 1. Write a recursive function called countdown that prints numbers from n down to 1 then prints "Blast off!".

# def countdown(n):

#   if n == 0:
#     print("Blast off!")
#     return 0
  
#   print(n)
#   countdown(n-1)
  

# countdown(5) 


# Problem 2. Write a recursive function called power that takes a base and exponent and returns base to the power of exponent. Do not use **.

# def power(num1,num2):
#   if num2 ==1:
#     print("done")
#     return result
  
#   result = power(num1,num1*num2) 

#   return result

  


# print(power(2, 3) )
# print(power(3, 4) )


# Problem 3. Write a recursive function called sum_digits that takes a number and returns the sum of its digits.

def sum_digits(num):

  number = num

  sum = 0

  

  if number>0:
      last_num = number% 10 
      sum = sum+last_num*10

      

    
  sum_digits(number/10)

  return sum

      




print(sum_digits(123)) 

     


    

   

  

   

  


 

