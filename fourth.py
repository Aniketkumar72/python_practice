# Q1. avg of three numbers using function

def calc_avg(a, b, c):
    avg = (a + b + c)/3
    print(avg)
    return avg

calc_avg(5, 5, 5)

# Q2. W.A.F to print the length of a list.

num = [1,2,3,4,5]
cities = ["delhi", "ranchi"]
def len_list(list):
    print(len(list))

len_list(num)
len_list(cities)

# Q3. W.A.F to print the elements of a list in a single line. 

cities = ["delhi", "ranchi"]
def len_list(list):
    for item in list:
        print(item, end = " ")

len_list(cities)

# Q4. W.A.F to find the factorial of n.

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    print(fact)

calc_fact(5)

# Q5. W.A.F to convert USD TO INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =",inr_val,"INR")

converter(1)

# Q6. W.A.F to print the no. is even or odd?

def num_func(n):
        n = int(input("enter the no.:"))

        if(n%2 == 0):
            print("even")

        else:
            print("odd")
num_func(1)

# Q7. write a recursive function to print a factorial of n?

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# Q8. write a recursive function to calculate the sum of first n natural numbers?

def num(n):
    if(n == 0):
        return 
    return num(n-1) + n

sum = num(10)
print(sum)

# Q9. write a recursive function to print all elements in a list?

def calc_el(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    calc_el(list,idx+1)

cities = ["delhi","ranchi","bihar","bangalore"]
    
calc_el(cities)

# Q10. write a recursive function to print fibonacci number of n element?

def fib(n):
    if(n<=1):
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))