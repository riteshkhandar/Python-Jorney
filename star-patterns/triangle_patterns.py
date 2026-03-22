
#     *
#    ***
#   *****
#  *******

for i in range(1, 6):
    
 
    for j in range(5-i):
        print(" ", end="")
    
   
    for k in range(2*i-1):
        print("*", end="")
 
    print()




# *
# **
# * *
# *  *
# *****

for i in range(1,6):
    for j in range(1,i+1):

        if (i==3 or i==4) and (j!=1 and j!=i): 
            print(" ", end="")

        else:
            print("*", end="")
    print()





# *********
#  *******
#   *****
#    ***
#     *


for i in range(1, 6):
    
 
    for j in range(i-1):
        print(" ", end="")
   
    for k in range(2*(5-i)+1):
        print("*", end="")
    
    print()