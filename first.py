# Q1. write a program to input two numbers and print their sum?

a = int(input("enter first no.:"))
b = int(input("enter second no.:"))

print("sum:",a + b)

# Q2. W.A.P to input side of square and print its area?

side = int(input("enter square side:"))
print("area:",side**2)

# Q3. W.A.P to input two floating point no. and print their avg?

a = float(input("enter first no.:"))
b = float(input("enter second no.:"))

print("avg:",(a + b)/2)

# Q4. W.A.P to input two numbers a and b. print true if a is greater than equal to b. if not print false?

a = int(input("enter first no.:"))
b = int(input("enter second no.:"))

print(a>=b)

# Q5. W.A.P to input user's first name and print its length?

name = input("enter name:")
print(len(name))

# Q6. W.A.P to find the occurrence of $ in a string?

str = "hi i am the $ symbol $99"
print(str.count("$"))

# Q7. grade students based on marks
    # marks >= 90, grade = "A"
    # 90 > marks >= 80, grade = "B"
    # 80 > marks >= 70, grade = "C"
    # 70 > marks >= 60, grade = "D"
    
marks = int(input("enter marks:"))
if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
elif(marks >= 60 and marks <70):
    print("grade D")
else:
    print("fail")

# Q8. W.A.P to check if a number entecred by the user is odd or even?

a = int(input("enter a number:"))
if(a%2 == 0):
    print("even")
else:
    print("odd")

# Q9. W.A.P to find the greater of three no. enterd by the user?

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))   

if(a >= b and a >= c):
    print("a is greater")
elif(b >= c):
    print("b is greater")
else:
    print("c is greater")

# Q10. W.A.P to check if a number is a multiple of 7 or not?
a = int(input("enter a number:"))
if(a % 7 == 0):
    print("multiple of 7")
else:
    print("not")

# Q11. W.A.P to check the eligible for vote or not?
age = int(input("enter age :"))
if(age >= 18):
    print("eligible for vote")
else:
    print("not")