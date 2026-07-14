
from turtle import update


profile = {"name": "John Doe", 
           "age": 30, 
           "email": "john.doe@example.com"}

'''
print (profile)

print ("Name:", profile["name"])

profile["age"] += 1 
print ("Updated age:", profile["age"])

profile = {"skills": "Python"}

print (profile["skills"])

'''

rank={"rank": "Beginner",
      "level": 1}

merged_profile = {**profile, **rank}
print (merged_profile)

rank["Exam"] = "Python Basics"
print (rank)

merged_profile = {**profile, **rank}
print (merged_profile)