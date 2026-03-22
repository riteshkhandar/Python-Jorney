# # check the enterd number is odd or even
# num = int(input("enter a number :"))

# if num % 2 == 0 :
#   print('even')

# else:
#   print("odd")
  

number1 = int(input("Enter a Number 1 : "))

number2 = int(input("Enter a Number 2 : "))


number3 = int(input("Enter a Number 3 : "))

number4 = int(input("Enter a Number 4 : "))


if number1>number2 and number1>number3 and number1 >number4:

    print(number1, "big")


elif number2>number1 and number2>number3 and number2 >number4:
    print(number2,"big")


elif number3>number1 and number3>number3 and number3>number4:
    print(number2,"big")


else:
    print(number4,"big")