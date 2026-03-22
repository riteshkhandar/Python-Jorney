# list comprehension and function


list = [i for i in range(1,6)]

def get_sum(l):
  sum =0

  for item in l:

    sum+=item
  return sum


print(get_sum(list))

