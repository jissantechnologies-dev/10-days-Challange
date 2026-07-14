#This is a simple Python program that demonstrates the use of different data types.

# Numbers
a=5
#a.append(10)  # This will raise an AttributeError since integers do not have an append method.

#Strings
x="Social Eagle"
#x.append(" is a great platform for learning.")  # This will raise an AttributeError since strings do not have an append method.

#Tuples
Student= ("Saravanan", "SDET", 25, "Chennai")
#Student.append(6)  # This will raise an AttributeError since tuples do not have an append method.

#Lists
fruits=['apple', 'banana', 5, 10.5]
fruits.append(20)

#Dictionaries
Student= {"name": "Saravanan", "age": 25, "city": "Chennai"}
Student["grade"] = "A"
Student["rank"] = "Pass"
#Student.append(5)  # This will raise an AttributeError since dictionaries do not have an append method.

#Sets
numbers={10,5,7,10}
numbers.add(15)
#numbers.append(20)  # This will raise an AttributeError since sets do not have an append method.


#Print data types of the variables
print(type(a))
print(type(x))
print(type(Student))
print(type(fruits))
print(type(numbers))
#print(type(b))
#print(type(k))

#Print the values of the variables
print("The value of Number:", a)
print("The value of String:", x)  
print("The value of Tuple:", Student)
print("The value of List:", fruits)
print("The value of Dictionary:", Student)    
print("The value of Set:", numbers)


