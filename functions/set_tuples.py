# Problem 1. Write a function called `common_elements` that takes two lists and returns a set of elements that appear in both. Use set operations, not loops.

# common_elements([1,2,3,4], [3,4,5,6]) → {3, 4}

def common_elements(lst1,lst2):

  s1 = set(lst1)
  s2 = set(lst2)

  return (s1 & s2)  



print(common_elements([1,2,3,4], [3,4,5,6]))



# Problem 3. Write a function called `unique_only` that takes two lists and returns elements that appear in only one of the lists, not both. Use set operations.
# unique_only([1,2,3,4], [3,4,5,6]) → {1, 2, 5, 6}

def unique_only(lst1,lst2):
  s1 = set(lst1)
  s2 = set(lst2)

  return (s1^s2)


print(unique_only([1,2,3,4], [3,4,5,6]))




# Problem 4. Write a function that takes a string and returns the number of unique characters in it. Use a set.

# unique_chars("hello world") → 8

def unique_chars(str):
  s = set(str)





  


  return len(set(s) - {' '})
 
print(unique_chars("hello world"))



# Problem 5. Write a function called `is_subset` that takes two lists and returns True if the first list is a subset of the second — meaning every item in the first list appears in the second list.

# is_subset([1,2,3], [1,2,3,4,5]) → True
# is_subset([1,2,6], [1,2,3,4,5]) → False


def is_subset(lst1,lst2):
  s1 = set(lst1)
  s2 = set(lst2)

  return s1.issubset(s2)


print( is_subset([1,2,3], [1,2,3,4,5]))

print ( is_subset([1,2,6], [1,2,3,4,5]))
      


# Problem 6. You have a list of student tuples — each tuple contains a name and a grade. Write a function that returns the name of the student with the highest grade.


students = [("Ahmed", 88), ("Sara", 95), ("Ali", 72)]


def top_student(s):
  highest = s[0]

  for student in s:
     if student[1]>highest[1]:
       highest = student
     
  return highest[0]

print(top_student(students))
   
  
# Problem 7. Write a function that takes a list of tuples representing items and prices, and returns the most expensive item.

def most_expensive(lst):

  expesive=lst[0]

  for item in lst:
     if item[1] > expesive[1]:
        expesive = item

       
  return expesive[0]



items = [("apple", 1.5), ("mango", 3.0), ("banana", 0.75)]
print(most_expensive(items))




# Problem 8.** Write a function that takes a sentence and returns a sorted list of unique words in it.
# unique_words("the cat sat on the mat the cat") 

def unique_words(str):

  words = str.split()
  s = set(words)

  return sorted(s)




print(unique_words("the cat sat on the mat the cat"))