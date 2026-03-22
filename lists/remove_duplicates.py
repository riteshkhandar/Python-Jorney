
# Remove duplicates from a list using loops.

# Example

# Input
# [1,2,2,3,4,4,5]

# [1,2,3,4,5]


numbers = [1,2,2,3,4,4,5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)



