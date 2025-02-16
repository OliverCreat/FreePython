class MyClass:
    variable = "blah"
    other = "red"

    def function(self):
        if self.variable == "blah":
            print("This is a message inside the class. \n")
        elif self.variable == "yackity":
            print("This is not Blah!!!\n")
        else:
            print("This is a number\n")
            
myobjectx = MyClass()
myobjecty = MyClass()
myobjectz = MyClass()

print(myobjectx.variable)

myobjectx.function()

myobjecty.variable = "yackity"

print(myobjecty.variable)
myobjecty.function()


myobjectz.variable = "1000"

print(myobjectz.variable)
myobjectz.function()


#new construction
#A função __init__(), é uma função especial que é chamada quando a classe está sendo iniciada. É usada para atribuir valores em uma classe.


class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
    
var = NumberHolder(8)
print(var.returnNumber())




# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# 
car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
