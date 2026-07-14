#This is a simple Python program that demonstrates the use of loops.

for i in range(2,10):
    print(i)


list = [1,2,3,4,5,6,7,8,9,"Saravanan",10.9]

for i in list:
    print(i)

dict = {"name":"Saravanan", "age":25, "city":"Chennai"}

for key, value in dict.items():
    print(key, ":", value)

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [10,11,12,13,14,15,16,17,18]
list3 = [19,20,21,22,23,24,25,26,27]

for i, j, k in zip(list1, list2, list3):
    print(i, j, k)

