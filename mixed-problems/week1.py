# Problem 1. Write a function that takes a list of numbers and returns a new list with duplicates removed. Do not use set().

# remove_duplicates([1, 2, 2, 3, 4, 4, 5]) → [1, 2, 3, 4, 5]


def remove_duplicates(lst):

  single = []

  for i in lst:
    if i not in single:
      single.append(i)
      

  return single


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))



# Problem 2. Write a function that takes a string and returns True if all characters are unique, False if any character repeats.

def all_unique(str):

  count = {}

  for char in str:
    if char in count:
      return False
    
    else:
      count[char]=1
  return True
    
print(all_unique("hello"))
print(all_unique("world") )
print(all_unique("code")  )

  

# Problem 3. Write a function that takes two lists and returns a list of items that appear in both.

def common(lst1,lst2):

  common =[]

  for i in lst1:

    for j in lst2:
      if i == j:
        common.append(i)

  return common







print(common([1, 2, 3, 4], [3, 4, 5, 6]))



 


# Problem 4. Write a function that takes a sentence and returns the longest word in it.

def longest_word(str):
 words = str.split()

 longest_word = words[0]
 

 for l in words:

   if len(l)>len(longest_word):
     longest_word = l

 return longest_word

print(longest_word("I love programming in Python"))

 
# Problem 5. Write a function that takes a list of numbers and returns two lists — one with even numbers and one with odd numbers.


def split_even_odd(lst):
  even =[]
  odd =[]

  for item in lst:
    if item % 2  ==0:
      even.append(item)
    else:
      odd.append(item)
  return even,odd




print(split_even_odd([1,2,3,4,5,6]) )


# Problem 6. Write a function that takes a string and returns a dictionary of character frequencies, but only for letters — ignore spaces and punctuation.


def char_freq(str):
  freq = {}

  for char in str:

    if char.isalpha():
       if char in freq:
        freq[char] += 1
       else:
        freq[char] = 1
    
   
 
  return freq
    


print(char_freq("hello world"))   


# Problem 7. Write a function that takes a list of strings and returns the list sorted by the last character of each string.

def sort_by_last(lst):

  sort_words = sorted(lst, key=lambda x: x[-1])



  return sort_words

  

print(sort_by_last(["banana", "apple", "cherry"]) )


# Problem 8. Write a function that flattens a nested list — turns a list of lists into a single list.
# flatten([[1,2], [3,4], [5,6]]) → [1, 2, 3, 4, 5, 6]

def flatten(lst):

  nw = []

  for item in lst:

    for elm in item:
      nw.append(elm)

  return nw
    


print(flatten([[1,2], [3,4], [5,6]]))



# Problem 9. Write a function that takes a list of dictionaries representing students and returns the name of the student with the highest grade.




def top_student(lst):

    highest_student = lst[0]

    for student in lst:
       
        if student["grade"] > highest_student["grade"]:
           
            highest_student = student

    return highest_student["name"]

students = [
    {"name": "Ahmed", "grade": 88},
    {"name": "Sara",  "grade": 95},
    {"name": "Ali",   "grade": 72}
]

print(top_student(students)) 




# Problem 10. Write a function that takes a string and returns True if it is an anagram of another string — meaning both strings have exactly the same characters, just in different order.


anagram = False

def is_anagram(str1,str2):
     

    

  
  
  
     return sorted(str1) == sorted(str2)



print(is_anagram("listen", "silent"))


print(is_anagram("hello", "world"))