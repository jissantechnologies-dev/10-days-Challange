#Conditional Statements

score = int(input("Enter your exam score: "))



if score >100:
    print("Invalid score. Please enter a score between 0 and 100.")
elif 90 <= score <= 100:
    print("You got an A!")
elif 80 <= score < 90:
    print("You got a B!")
elif 70 <= score < 80:
    print("You got a C!")   
else:
    print("You got a C or lower.")



#Nested if-else statements

age=int(input("Enter your age: "))
Channel=input("Enter your channel Name: ")

if age>=18: 
    if Channel=="Geevee":
        print("You are eligible to watch Geevee content.")
    else:
        print("You are not eligible to watch this content.")    


#Ternary Operator

age = int(input("Enter your age: "))

is_eligible = True if age >= 18 else False



