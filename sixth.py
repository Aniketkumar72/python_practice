# Q1. create student class that takes name and marks of three subjects as arguments in constructor. then create a method to print the average ?

class student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "the avg score is:", sum/3)

s1 = student("aniket", [97,86,92])
s1.get_avg()

# Q2. create account class with 2 attributes balance and account no. create methods for debit, credit and printing the balance.

class account:

    def  __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("rs", amount ,"was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("rs", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)

#abstraction

# Q3. write a program the vehicle problem to show abstraction without using the abstract keyword ?
    # scenario: you are building a gracing game. you have a car and bike
    # the task: create a way to "start" all vehicles at the  begining of a race.

class vehicle: 

    def start_engine(self):
        print("start the vehicle engine")
    
class car(vehicle):
    def start_engine(self):
        print("car: turning the key and ignition started..")

class bike(vehicle):
    def start_engine(self):
        print("bike: kickstarting the engine")

def begin_race(veh):
    veh.start_engine()

c1 = car()
b1 = bike()

begin_race(c1)
begin_race(b1)

# Q4. write a program the "remote control" problem 
    #the problem: think of Tv remote. it has a button labelled "volume up."
    #abstraction task: does the user need to know about circuit boards, or binary code to increase the volume?

class RemoteControl():

    def __init__(self):
        self.brand = "samsung"
    
    def check_battery(self):
        print("check battery voltage")
        return True
    
    def connect_infrared(self):
        print("setting frequency")

    def send_signal(self):
        print("power on")

    def press_power_button(self):
        print(f"---{self.brand}--- remote")

        if self.check_battery():
            self.connect_infrared()
            self.send_signal()
            print("action: tv is on")
    
R1 = RemoteControl()
R1.press_power_button
R1.send_signal()

# Q5. write a program the "pet" problem?
    #the details :golden retriever named buddy who likes tennis ball:
    # a siamese cat named luna who hates vaccum cleaners.
    # the abstraction: both are "pets". both have a name.

class pet():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass

class dog(pet):
    def speak(self):
        return "woof"
    
class cat(pet):
    def speak(self):
        return "meow"
    
pets = [dog("buddy"),cat("luna")]

for p in  pets:
    print(f"{p.name} says: {p.speak()}")