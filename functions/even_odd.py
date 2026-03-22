# find the number is even or odd using function


def is_even(n):

  if n%2==0:
    return True
  
  else:
    return False


print(is_even(5))


# checking the number in range to print only even number using is_even function
for i in range(1,21):

  if is_even(i):
    print(i)


    

