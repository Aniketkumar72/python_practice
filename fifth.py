# Q1. create a new file "practice.txt" using python. add the following data?
        #"hi everyone
        # we are learning file i/o
        # using java 
        # i like programming in java"

with open("practice.txt","w") as f:
    f.write("hi everyone\nwe are learning file i/o\n")
    f.write("using java\ni like programming in java")

# Q2. W.A.F that replce all the occurences of "java" with python in above file?
    
def replace():
    with open("practice.txt","r") as f:
        data = f.read()

    new_data = data.replace("java","python")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

replace()

# Q3. search if the word "learning" exists in the file or not?

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

# Q4. W.A.F  to find in which line of the files does nthe word "learning" occur first print -1 if word not found?

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    
    return -1

check_for_line()
    
# Q5. from a file containig  numbers seperated by comma, print the count of even numbers?

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    print(num)
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
        
print(count)