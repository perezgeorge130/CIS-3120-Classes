class Animal:
    def __init__(self, name, animal, weight = 10, lifespan = 5): 
        self.__name = name
        self.__animal = animal
        self.__weight = weight
        self.__lifespan = lifespan
        print(f"Hello, my name is {self.__name} and I am a {self.__animal.lower()}! I weigh {self.__weight} pounds and have {self.__lifespan} years left to live")

    def vet(self):
        '''A visit to the vet adds one year to the lifespan of the pet'''
        self.__lifespan+=1
        print(f"Thank you for bringing your {self.__animal.lower()} to the vet. You have just increaed their lifespan by 1 year.")
    
    def feed(self):
        '''Feeding once adds 5 pounds to the pet's weight'''
        self.__weight +=5
        print(f"Your {self.__animal.lower()} has gained 5 pounds. The current weight is {self.__weight}")
    
    def pet(self):
        '''When you call this function, your pet gets 2 years added to lifespan'''
        self.__lifespan+=2
        print(f"Your {self.__animal.lower()} was loved. They have gained 2 years in lifespan. Thank you for loving them.")

    def run(self,time):
        '''time: Time you are letting your pet run for. Time must be less than weight'''
        if time>=self.__weight:
            print("Less time to run please.")
        elif self.__weight - time <=5:
            print(f"Your {self.__animal.lower()} cannot be less than or equal to 5 pounds after a run. It will die")
        else:
            self.__weight-=time
            print(f"Your {self.__animal.lower()} is now {self.__weight} pounds.")
    
    def speak(self):
        '''Your pet will speak'''
        print("RAHH")
