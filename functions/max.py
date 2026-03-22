# find the max element in list using function




numbers = [-5, -3, -8, -1]
def get_max(l):
    maximum = numbers[0]
    for m in l:
        if maximum < m:
            maximum = m
    return maximum
