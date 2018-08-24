#Question 1
class circle:
    def __init__(self):
        self.radius=10
    def getArea(self):
        self.area=3.14*(self.radius**2)
        print(self.area)
    def getCircumference(self):
        print(2*3.14*self.radius)
a=circle()
a.getArea()
a.getCircumference()


#Question 2
class student:
    def __init__(self):
        self.name=input("Enter Name: ")
        self.rollno=int(input("Enter Rollno: "))
        self.age=0
        self.marks=0
    def display(self):
        print("Student Info: ")
        print(self.name,self.rollno,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter Age: "))
    def setMarks(self):
        self.marks=int(input("Enter Marks: "))
s=student()
s.setAge()
s.setMarks()
s.display()


#Question 3


class temperature:
    def __init__(self):
        self.ctemp=0
        self.ftemp=0
    def convertFahrenheit(self):
        self.ctemp=float(input("Enter temperature in celsius: "))
        self.ftemp=(self.ctemp*1.8)+32
        print(self.ctemp,"celsius=",self.ftemp,"Fahrenheit")
    def convertCelsius(self):
        self.ftemp=float(input("Enter temperature in celsius: "))
        self.ctemp=(self.ftemp - 32) * 0.5556
        print(self.ftemp,"Fahrenheit=",self.ctemp,"celsius")
t=temperature()
t.convertFahrenheit()
t.convertCelsius()


#Question 4

class MovieDetails:
    def Display(self):
        print("Movie Details:")
        print("Artist Name: ",self.artistname,"\nYear Of Release: ",self.year,"\nRating: ",self.rating)
    def Add(self):
        self.artistname=input("Enter Artist Name: ")
        self.year=int(input("Enter year Of release:  "))
        self.rating=float(input("Enter The Rating: "))
m=MovieDetails()
m.Add()
m.Display()


#Question 5

class Animal:
    def animaL(self):
        print("Animal Class")
class animal_attribute():
    def animal(self):
        print("animal_attributes Class")
class Tiger(Animal,animal_attribute):
    def tiger(self):
        print("Tiger Class")
a=Animal()
b=animal_attribute()
c=Tiger()
c.animaL()
c.animal()


#Question 6

output= A B
	A B


#Question 7


class Shape:
    def area(self):
        self.length=int(input("Enter length: "))
        self.breadth=int(input("Enter breadth: "))
class rectangle(Shape):
    super().area()      
class square(Shape):
    super().area()
s=Shape()
r=rectangle()
sq=square()
r.area()
sq.area()
