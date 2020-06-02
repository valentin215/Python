# Definition 

class GreetingClass: 

    def __init__(self, greet):
        self.greet = greet

    def display_greet(self):
        print(str(self.greet) + " " + "World, Welcome in Python first class")


greeting = GreetingClass('Bonjour').greet
greeting_test = GreetingClass('Hello')
print(greeting_test.display_greet())
print(GreetingClass('Hello').display_greet())

# Classes objects


