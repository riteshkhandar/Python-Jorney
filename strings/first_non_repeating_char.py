# Find the first non-repeating character.

string =  "With great power comes great responsibility great great great great Spider-Man is great at swinging but not so great at paying rent"

list = string.split()

dict = {}

max = 0

repeated_word = ""



for word in list:

  if word in dict:
     dict[word]+=1
  else:
     dict[word]=1

print(dict)


for most in dict:
   if  dict[most]>max:
        
    max=dict[most]
    repeated_word = most
      

   print(most)
   
   
   
print(f"repeated word : {repeated_word} {max} times")

