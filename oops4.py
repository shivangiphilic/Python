class Car:
    def __init__(self,model,speed,price):
        self.model = model
        self.speed = speed
        self.price = price

class Firing_Car(Car):
    def __init__(self,model,speed,price,bullets):
        self.model = model
        self.speed = speed
        self.price = price
        self.bullets = bullets
    def fire(self):
        print("Model:",self.model)
        print("Speed:",self.speed,"kmph")
        print("Price: $",self.price)
        print("Bullets:",self.bullets)

model = input("Enter the model of car: ")
speed = int(input("Enter the speed of Car: "))
price = int(input("Enter the price of Car: "))
bullets = int(input("Enter the no. of bullets: "))
car = Firing_Car(model,speed,price,bullets)
car.fire()
