
# Go back to Alex's lesson on Wednesday August 30th as a guide

# 1. Create a class called Wolf. When this class is instantiated it takes in a name and age. 
# the class is also to have a method called back which will print its name and 'Ahhhoooo'

# 2. Instantiate: Create an Object from the Wolf class and use the bark method

class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def howl(self):
        print(f"{self.name} says Ahhhoooo")

wolf1 = Wolf("Freddie", 10)
wolf1.howl()

# 3. Create a class called Dog. This class will Inherit from the class Wolf. 
# Define a method called 'fetch' and have it print "Who is a good boy"

class Dog(Wolf):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def fetch(self):
        print(f"{self.name} is a good boy")

dog1 = Dog("Teddi", 5)
dog1.fetch()

# 4. Instantiate: Create an Object from the Dog class and try the bark method

# 5. Remember the class Fighter from Aug 30th.
# Change the attack method. 
# In the attack method, damage is strength subtracted by defense. 
# This needs change to: Any integer value between zero and strength subtracted by defense.
# Look up how to generate random number python
# Look up how to round to nearest intergy python

# 6. Change ryu and ken to have the same stats. Fight until ken win 2 times
# While the advantage will still be on the first attacker's side the result should be closer to 50/50
# I like an even match

class Fighter:
    def __init__(self, name, hp, strength, defence):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence
        
    def attack(self, opponent):
        damage = self.strength - opponent.defence
        if (damage < 0):
            damage = 0
        opponent.hp -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage")
        
ryu = Fighter("Ryu", 100, 10, 5)
ken = Fighter("Ken", 100, 12, 3)

while(True):
    ryu.attack(ken)
    
    if (ken.hp <= 0):
        print(f"{ryu.name} wins!")
        break
        
    ken.attack(ryu)
    
    if (ryu.hp <= 0):
        print(f"{ken.name} wins!")
        break
