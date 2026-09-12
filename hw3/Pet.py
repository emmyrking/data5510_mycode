# create the blueprint for pet
class Pet():
    
    # initilize attributes in the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = input("What is the species of your pet?")

    # print out information on converting to human years and average lifespan of the pet
    def __str__(self):
        return f"Your pet {self.name} is {self.convert_humanyears()} in human years. {self.average_lifespan()}"

    # convert each pet age to human years (relative age to humans)
    def convert_humanyears(self):

        # if the species entered matches dog, horse, or bird, return the corresponding calculation
        if self.species == 'dog':
            return self.age * 7

        elif self.species == 'horse':
            return self.age * 4

        elif self.species == 'bird':
            return self.age * 9

    # print out the average lifespan of the specific species entered
    def average_lifespan(self):

        # if input matches dog, horse, or bird, return the corresponding average lifespan
        if self.species == 'dog':
            return "The average lifespan of a dog is 10-13 years."

        elif self.species == 'horse':
            return "The average lifespan of a horse is 25-30 years."

        elif self.species == 'bird':
            return "The average lifespan of a dog is 5-80 years depending on the type."

# Lucky is a dog. Print out information found.
pet1 = Pet("Lucky", 3)
print(pet1)

# Blue is a horse. Print out information found.
pet2 = Pet("Blue", 10)
print(pet2)

# Pete is a bird. Print out information found.
pet3 = Pet("Pete", 7)
print(pet3)

#------ AI session link ------#
# https://chatgpt.com/share/6aa5df5f-bbac-83e8-b3a7-1420b63d66f2
