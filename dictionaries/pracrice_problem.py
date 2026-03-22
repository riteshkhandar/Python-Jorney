
student = {

  "name":"tony",
  "age":23,
  "marks":85
}
print(student["marks"])



print(student)


product = {
  "name":"laptop",
  "price":50000,
  "quantity":2
}

print(product["name"])
print("total price =",product["price"]*product["quantity"])



car = {
  "name":"tesla",
  "price":5000000

}

car["color"] = "red"

print(car)



student = {
"name": "Ravi",
"marks": 75
}

student["city"] = "pune"

student["marks"] = 85

print(student)




student = {
"name": "Amit",
"marks": [78, 82, 90]
}

print("amit scored",student["marks"][1])


student = {
  "name":"Ravi",
  "marks":[70,85,90]
}
print(student["name"],"total marks =",student["marks"][0]+student["marks"][1]+student["marks"][2])


student = {
"name": "Ankit",
"marks": [70, 85, 90]
}

average = student["marks"]

average_marks=(average[0]+average[1]+average[2])/(len(average))

print(f"Avrage marks = {average_marks}")



student = {
"name": "Rahul",
"marks": [65, 80, 72]
}

marks = student["marks"]

largest = marks[0]

if marks[1] > largest:
    largest = marks[1]

if marks[2] > largest:
    largest = marks[2]

print("Highest marks =", largest)


lowest = marks[0]

if marks[1] > largest:
    lowest = marks[1]

if marks[2] > largest:
    lowest = marks[2]

print("Lowes marks =", lowest)