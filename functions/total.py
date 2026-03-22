#  get the sum of the element of the list using fucntion

lst=[i+i for i in range(1,6)]
def get_sum(l):
    total = 0
    for item in l:
        total += item
    return total
