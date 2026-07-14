#This is a simple Python program that demonstrates the use of lists and some basic list operations.

task=["eat","code","sleep","repeat"]

print("The value of task is:", task)

task.append("exercise")
print("The value of task after appending 'exercise' is:", task)

for i in task:
    print(i)

task.reverse()
print("The value of task after reversing is:", task)