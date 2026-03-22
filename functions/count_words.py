# count the words in a string using function


def word_count(s):
  count = {}

  words = s.split()





  for char in words:
    if char in count:
      count[char]+=1

    else:
      count[char]=1

 
  return count

print(word_count("the cat sat on the mat the cat"))



#  find the most frequent word in a  string



def most_frequent(s):

 count= word_count(s)

 
 frequent=""

 max = 0


 for c in  count:
   if count[c] > max:
     max = count[c]
     frequent=c
     
     
    
 return frequent


print(most_frequent("the cat sat on the mat the cat"))
