# Sets — unordered collection, no duplicates, fast membership checking


# Key set operations:
# a | b  → union (everything from both)
# a & b  → intersection (only in both)
# a - b  → difference (in a but not in b)
# a ^ b  → symmetric difference (in either but not both)



# Problem 1. Create a list with duplicates, convert it to a set to remove duplicates, then convert it back to a sorted list.

# input:  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# output: [1, 2, 3, 4, 5, 6, 9]



lst =  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


set_list = sorted(set(lst))

print(set_list)

