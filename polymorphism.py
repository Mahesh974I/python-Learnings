class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return (f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        return ("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return (f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        return ("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    print(animal.info())
    print(animal.make_sound())





class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()