# find second largest element in the list 

numbers = [10, 5, 20, 8, 100, 101, 2, 3, 4]

largest = float('-inf')
second_largest = float('-inf')

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print(largest)
print(second_largest)