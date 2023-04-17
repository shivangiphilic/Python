import random

class Roler:
    self.roles = ["singer","dancer","rapper"]
    
    @classmethod
    def sort(cls,name):
        role = random.choice(cls.roles)
        print(f"{name} is a {role}")

Roler.sort("Rose")

'''We don't need any obj. We are directly
using the class Roler to access class
methods like sort(cls is always first arg)
Used when you want only one obj. No need
for roler1, roler2...'''
