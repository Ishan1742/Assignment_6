class Dog:
  def __init__(self,name=None,age=0,coat=None):
    self.name = name
    self.age = age
    self.coat = coat

  # Instance method
  def description(self):
    print(f"{self.name} is {self.age} years old")

  def get_info(self):
    print(f"{self.name} has {self.coat} Coat")
  
class JackRussellTerrier(Dog):
  def __init__(self,name=None,age=0,coat=None):
    super().__init__(name,age,coat)
    
  def run(self):
    super().description()
    super().get_info()
    print(f"{self.name} likes to Run a lot")
    
  def jump(self):
    print(f"{self.name} jumps a lot")  

class Bulldog(Dog):
  def __init__(self,name=None,age=0,coat=None):
    super().__init__(name,age,coat)
  
  def drool(self):
    super().description()
    super().get_info()
    print(f"{self.name} Drools a lot ")
  
  def bark(self):
    print(f"{self.name} Barks a lot ")


#object

a = JackRussellTerrier("Mike" , 4 , "Brown")
a.run()
a.jump()


b = Bulldog("Spike" , 6 , "Grey")
b.drool()
b.bark()


  