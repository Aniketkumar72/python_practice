# Q1. print no. from 1 to 100

i = 1
while i <= 100:
    print(i)
    i +=1

# Q2. print no. from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -=1

# Q3. print the multiplication table of number n?

n = int(input("enter the number:"))
i = 1

while i <= 10:
    print(n*i)
    i +=1

# Q4. print the element of the following list using a while loop?
    # [1,4,9,16,25,36,49,64,81,100]

a = [1,4,9,16,25,36,49,64,81,100]
idx = 0

while idx <= len(a)-1:
    print(a[idx])
    idx +=1

# Q5. search for a number x in this tuple using while loop?
    # [1,4,9,16,25,36,49,64,81,100]

a = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter no.:"))
i = 0
while i < len(a):
    if(a[i] == x):
        print("found at idx",i)
    i +=1

# Q6. print the element of the following list using a for loop?
    # [1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

for val in num:
    print(val)

# Q7. search for a number x in this tuple using for loop?
    # [1,4,9,16,25,36,49,64,81,100]

num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number:"))
i = 0

for val in num:
    if(val == x):
        print("found at index",i)
    i +=1

# Q8. print no. from 1 to 100 using for and range()

for i in range(1, 101):
    print(i)

# Q9. print no. from 100 to 1 using for and range()

for i in range(100, 0, -1):
    print(i)

# Q10. print the multiplication table of number n using  for and range()?

n = int(input("enter a number:"))

for i in range(1,11):
    print(n*i)

# Q11. W.A.P to find the sum of n natural numbers using for loop?

n = 5
sum = 0

for i in range(1, n+1):
    sum += i

print("total no. of sum is:",sum)

# Q12. W.A.P to to find the factorial of first n numbers?

n = 5
fact = 1

for i in range(1 , n+1):
    fact *=i

print("total no. of factorial are:", fact)