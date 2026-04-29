# Q1. Write a program to add to complex number using a dunder function ?

class complex:
    def __init__(self, real, img):
        self.real = real 
        self.img = img 

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return complex(newReal, newImg)


num1 = complex(1, 3)
num1.showNumber()

num2 = complex(2, 4)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

# Q2. define a circle class to create a circle with radius r using the constructor. define an area() method of the class which calculates the
    #area of the circle. define an perimeter() method of the class which calculates the perimeter of the circle?

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = circle(15)
print(c1.area())
print(c1.perimeter())

# Q3. define a employee class with attributes role, department and salary. this class also has a showDetails() method.
    #create an engineer class that inherit properties from employee and use constructor with attributes: name & age?

class employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "60,000")

engg1 = engineer("rahul", 24)
engg1.showDetails()   

# Q4. create a class called order which stores item & its price. use dunder function __gt__() to convey thet:
    # order1 > order2 if the price of order1 > price of order 2?

class order():
    def __init__(self,item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
     
odr1 = order("chips", 20)
odr2 = order("tea", 15)

print(odr1 > odr2)

# Q5. define a class vehicle with attributes speed. this class also has a display_speed() method.
    #create a derived class car that inherit properties from vehicle and adds attributes: brand and display_brand method?

class vehicle:
    def __init__(self, speed):
        self.speed = speed

    def display_speed(self):
        print("speed =", self.speed)

class car(vehicle):
    def __init__(self, speed, brand):
        self.brand = brand
        super().__init__(speed)

    def display_vehicle(self):
        print("speed =", self.speed)
        print("brand =", self.brand)
    
c = car("150 km/h", "toyota")
c.display_vehicle()

# Q5. define a base class person with attributes name. this class also has a display() method.
    #create a derived class student that inherit properties from person and adds attributes: roll_no and display both details?

class person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("name = ", self.name)

class student(person):
    def __init__(self, name, roll_no):
        self.roll_no = roll_no
        super().__init__(name)

    def display_student(self):
        print("name = ", self.name)
        print("roll.no = ", self.roll_no)
        
s = student("aniket",18)
s.display_student()

# Q6. create a class animal with method sound().create a class dog that override the sound() method.(method overriding.)

class animal:
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog barks")

d = dog()
d.sound()

# Q7. create a three class grandparents , parents that inherits properties from grandparents and child that inherit properties from parents
    # each class should have one method.

class grandparents():
    def older(self):
        print("i am grandparent")

class parents(grandparents):
    def adult(self):
        print("i am parent")

class child(parents):
    def young(self):
        print("i am child")

c = child()
c.young()
c.adult()
c.older()

# Q8. create a class employee with attributes name and salary. create a derived class manager that adds bonus and calculated total salary.

class employee():
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

class manager(employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus
    
m = manager("rahul",50000, 10000)
print("total salary: ", m.total_salary())

# Q9. create a class person with attributes name and age. create a class employee that inherits properties from person and adds employee_id and 
    # display_info() method that prints all details.

class person():
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

class employee(person):
    def __init__(self, name, age , employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("employee_id : ", self.employee_id)

e = employee("rahul", 24, 101)
e.display_info()

# Q10. create a base class shape with method area(). create a two derived classes rectangle or circle each class should override area() to 
    # calculates its own area.

class shape():
    def area(self):
        print("area not defined")

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
r = rectangle(12, 6)
c = circle(14)

print("area of reactangle: ", r.area())
print("area of circle: ",c.area())