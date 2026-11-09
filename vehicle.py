class Vehicle:
    def move(self):
        print("Vehicle can move different ways !")
        print()
        
class Car(Vehicle):
    def move(self):
        print("Car moves on four wheels !")
        print()
        
class Bike(Vehicle):
     def move(self):
         print("Bike moves on two wheels !")
         print()
         
class  Airplane(Vehicle):
     def move (self):
         print("Airplane flies in the sky !")
         print()
         
class  Boat(Vehicle):
      def move(self):
          print("Boat moves on water !")
          print()
          
class Train(Vehicle):
      def move(self):
          print("Train moves on rainway !")
          print()

vehicle = Vehicle()
car = Car()
bike = Bike()
airplane = Airplane()
boat = Boat()
train = Train()

vehicle.move()
car.move()
bike.move()
boat.move()
train.move()
          
         
               
        