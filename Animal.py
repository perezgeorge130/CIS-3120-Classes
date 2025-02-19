class Animal:
    def __init__(self, name, animal, weight = 10, lifespan = 5): 
        self.__name = name
        self.__animal = animal
        self.__weight = weight
        self.__lifespan = lifespan
        print(f"hello, my name is {self.__name} and I am a {self.__animal}!")

    def vet(self):
        '''A visit to the vet adds one year to the lifespan of the pet'''
        self.__lifespan+=1
        print(f"Thank you for bringing your {self.__animal} to the vet. You have just increaed their lifespan by 1.")
    
    def feed(self):
        '''Feeding once adds 5 pounds to the pet's weight'''
        self.__weight +=5
        print(f"Your pet has gained 5 pounds")
    
    def pet(self):
        '''When you call this function, your pet gets 2 years added to lifespan'''
        self.__lifespan+=2
        print(f"Your{self.__animal} was petted. They have gained 2 years in lifespan")

    def run(self,time):
        '''time: Time you are letting your pet run for. Time must be less than weight'''
        if time>self.__weight:
            print("Less time to run please")
        else:
            self.__weight-=time
            print(f"Your pet is now {self.__weight} pounds.")
    
    def speak(self):
        '''Your pet will speak'''
        print("RAHH")
