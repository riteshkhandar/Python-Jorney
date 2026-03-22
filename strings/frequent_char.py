# Find the most frequent character in a string

string = "banana"

dict = {}

for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

max_count = max(dict.values())

for key in dict:
    if dict[key] == max_count:
        print(key)




string2= "banana"

count = {}

for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1


largest = 0
most_char = ""

for char in count:
    if count[char] > largest:
        largest = count[char]
        most_char = char

print(most_char)


