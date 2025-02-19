class Animal:
    def __init__(self, name, animal, weight = 10, lifespan = 5): 
        self.__name = name
        self.__animal = animal
        self.__weight = weight
        self.__lifespan = lifespan
        print(f"hello, my name is {self.__name} and I am a {self.__animal}!")

    def vet(self):
        self.__lifespan+=1
        print(f"Thank you for bringing your {self.__animal} to the vet. You have just increaed their lifespan by 1.")
    
    def feed(self):
        self.__weight +=5
        print(f"Your pet has gained 5 pounds")
    
    def pet(self):
        self.__lifespan+=2
        print(f"Your{self.__animal} was petted. They have gained 2 years in lifespan")

    def run(self,time):
        if time>self.__weight:
            print("Less time to run please")
        else:
            self.__weight-=time
            print(f"Your pet is now {self.__weight}")
    
    def speak(self):
        print("RAHH")
