# Problem 1. Write a function called stats that takes a list of numbers and returns the minimum, maximum, and average. Print all three.

def stats(*args):

 
  high = args[0]

  sm = 0

  low = args[0]



  for n in args:
    if n > high:
      high= n

    if n <low:
      low = n

    sm =sm+n

 
  avg = sm / len(args)

  return high, avg, low


print(stats(1,2,3,4,5))



# Problem 2. Write a function called add_all using *args that takes any number of numbers and returns their sum. Test with 2, 5, and 10 numbers.

def add_all(*args):
  total = 0

  for s in args:
    total+=s

  return total

print(add_all(3,3,4,325,3,3))


# Problem 3. Write a function called build_profile using **kwargs that takes any named details and returns a dictionary. Test with name, age, city, job.

def build_profile(**kwargs):

  return kwargs


print(build_profile(name = "tony", city ="pune",job = "sf"))
    
# Problem 4. Sort this list by length, shortest first using lambda:

words = ["banana", "apple", "cherry", "date", "elderberry"]

short_words  = sorted(words,key=lambda x: len(x))

print(short_words)

# Problem 5. Write a function called apply that takes a function and a list, applies that function to every item, and returns the new list. Test it with a lambda that squares each number.

def apply(func,lst):

  squre = []

  for item in lst:
    squre.append(func(item))
 
  return squre


print(apply(lambda x : x*x,[1,2,3,4,5,6]))

# Problem 6. Write a function called calculator that takes two numbers and an operation as a string — "add", "subtract", "multiply", "divide" — and returns the result.


def calculator(a,b,opr):
  if opr == "add":
    return a+b
  
  elif   opr == "multiply":
    return a*b
  
  elif   opr == "divide":
    return a/b
  
  elif opr == "sub":
    

    return a-b
   
  else:
    print("use correct operation")
  
print(calculator(1,1,"add"))



# Problem 7. Write a function called count_above that takes a list and a threshold and returns how many numbers are above the threshold.

def count_above(list, treshold):

  count = 0

  for l in list :

    if l > treshold:
      count+=1
  return count


print(count_above([1,2,3,4,5,3,4,3,3,55,3564,333,123 ,133],3))


# Problem 8. Filter this list to only names longer than 4 characters using lambda and filter:

names = ["tony", "banner", "hulk", "peter","spidey"]

four_char_names=list(filter(lambda x : len(x)>4 ,names))

print(four_char_names)