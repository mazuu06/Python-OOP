# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = Person("Mazhar", 28)         # Instantiate an Object
# print(obj)                         # This will return a memory location where this object is stored

###############################################################################################################################

# class Person:
   
#     city = "Lahore"          # Class attribute

#     def __init__(self, name, age):
#         self.name = name            # Instance attribute
#         self.age = age              # Instance attribute
#         print(f"Name is : {self.name}\nAge is : ",self.age)

# obj = Person("Mazhar", 28)
# print(obj.city)

###############################################################################################################################

# class Person:
#     city = "Lahore"

#     def __init__(self, name, age):          # This will run at first
#         self.name = name
#         self.age = age

#     def detail(self):                        # Instance method
#         return f"{self.name} is {self.age} years old"

#     def F_Name(self, fname):                 # Another instance method
#         return f"{self.name} is son of {fname}"

# obj_1 = Person("Mazhar", 21)

# var_1 = obj_1.detail()
# print(var_1)

# var_2 = obj_1.F_Name("Naseer")
# print(var_2)

###############################################################################################################################
# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#         print(f"The {self.color} Car has {self.mileage} miles")

# car1 = Car("Blue", 20000)
# car2 = Car("Red", 30000)

###############################################################################################################################

# class animal:
#     def eating(self):
#         print("eating")

# class dog(animal):
#     def bark(self):
#         print("bark")

# d = dog()
# d.eating()
# d.bark

###############################################################################################################################

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# class GoldenRetriever(Dog):
#     def speak(self, sound="Bark"):
#         self.sound = sound
#         return super().speak(sound)


# obj = GoldenRetriever
# obj.speak








