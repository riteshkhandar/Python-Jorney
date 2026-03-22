# Find duplicate characters in a string.


string = "programming"


dupicate ={}

for char in string:
  if char in dupicate:
      dupicate[char]+=1
  
  else:
     dupicate[char]=1


for keys in dupicate:
   if dupicate[keys]>1:
      print(keys)
