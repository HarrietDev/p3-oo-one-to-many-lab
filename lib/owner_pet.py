class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if pet_type not in Pet.PET_TYPES:
            raise Exception (f"{pet_type} is not a valid pet")

class Owner:
    def __init__(self,name):
        self.name = name
        

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
         pet.owner =self
        else:
            raise Exception("Only Pet instances can be added.")
        
    def get_sorted_pets(self):
        sorted_list = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_list

owner = Owner("Harriet")

dog = Pet("Simba", "dog")
cat = Pet("Milo", "cat")
bird = Pet("Zazu", "bird")

owner.add_pet(dog)
owner.add_pet(cat)
owner.add_pet(bird)

for pet in owner.get_sorted_pets():
    print(pet.name)
