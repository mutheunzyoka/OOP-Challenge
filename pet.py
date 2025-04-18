
import random
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger =6
        self.energy = 3
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # `eat()`: reduces hunger by 3 points
        #  (but not below 0), and 
        # increases happiness by 1.
        self.hunger=max(0,self.hunger-3)# always above 0
        self.happiness=min(10,self.happiness+1)
        return f"{self.name}, hunger levels are at :{self.hunger} and happiness level is as:{self.happiness}" 
    
    def sleep(self):
        #increases energy by 
        # 5 points (but not above 10).
        self.energy=max(10,self.energy+5)
        return f"{self.name} is sleeping and its energy is at :{self.energy} "

    def play(self):
       # decreases energy by 2, i
       # increases happiness by 2, 
       # and increases hunger by 1
        if self.energy >= 2:# only do actions if the pet is atleast 2
            self.happiness += 2
            self.hunger +=1
            print(f"{self.name} plays. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, *tricks):
        for trick in tricks:
            self.tricks.append(trick)
        print(f"{self.name} learned a new trick:{trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"Status of {self.name}: Hunger={self.hunger}, Energy={self.energy}, Happiness={self.happiness}")
