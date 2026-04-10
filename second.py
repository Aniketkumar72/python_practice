# Q1. W.A.P to ask the user to enter name of their 3 favorite movies and store them in a list?

movies = []
mov1 = input("enter first movie:")
mov2 = input("enter second movie:")
mov3 = input("enter third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# Q2. W.A.P to check if a list contains a palindrome of elements or not?

list = [1,2,1]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("not")

# Q3. W.A.P to count the number of students with the "A" grade in the following tuple.
    # ["C","D","A","A","B","B","A"]

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

# Q4. store the above values in a list and sort them from "A" to "D"

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

# Q5. store following word meanings in a python dictionary:
    # table : "a piece of furniture", "list of facts & figures"
    # cat : "a small animal"

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]  
}
print(dict)

# Q6. you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students
    # "python","java","c++","python","javascript",
    # "java","python","java","c++","c"

subjects = {
    "python","java","c++","python","javascript",
     "java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

# Q7. W.A.P to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary &add one by one. use subject name as key 7 marks as value.

marks = {}
x = int(input("enter phy:"))
marks.update({"phy" : x})

x = int(input("enter math:"))
marks.update({"math" : x})

x = int(input("enter chem:"))
marks.update({"chem" : x})

print(marks)

# Q8. figure out a way to store 9 & 9.0 as seperate a values in the set.

values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)

# Q9. W.A.P to swap two variables?

a = int(input ("enter first no.:"))
b = int(input("enter second no.:"))

a,b = b,a
print("the value of a is:", a)
print("the value of b is:", b)

# Q10. W.A.p to cancatenate two list ?

a = [1,2,3,4]
b = [3,4,5.6]

res = list(set(a).union(set(b)))

print(res)

