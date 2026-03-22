# find the first repeating num in a list 


elements = [4, 5, 1, 2, 1, 4, 5]

seen = set()

for e in elements:
    if e in seen:
        print(e)
        break
    seen.add(e)