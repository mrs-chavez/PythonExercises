# This is a simple Python program that simulates having a pet
# This is inspired from the game Tamagotchi (also known as Virtual Pet)

from enum import Enum
from threading import Timer, Thread, Event

class Species(Enum):
    CAT = 'Cat'
    DOG = 'Dog'
    FISH = 'Fish'


class Pet():

    def __init__(self, name: str, species: Species):
        self.name = name
        self.species = species
        self.fullness = 50
        self.happiness = 50
        self.health = 99

    def change_name(self, new_name):
        self.name = new_name

        return self.name
    
    def feed(self):
        self.fullness = min(self.fullness + 10, 100)
        print(f"{self.name} says 'YUM!' and is now {self.fullness}% full.")
        

    def play(self):
        self.happiness = min(self.happiness + 5, 100)
        print(f"{self.name} says 'WEEE!' and is now {self.happiness}% happier.")

    def check(self):
        print(f"{self.name} is {self.fullness}% full and {self.happiness}% happy. Current health: {self.health} / 100")

    def is_pet_okay(self):
        is_alive = True

        # Gradually decrease fullness and happiness
        self.fullness = max(self.fullness - 2, 0)
        self.happiness = max(self.happiness - 1, 0)

        if self.health < 5:
            is_alive = False
        
        if self.fullness < 5:
            self.health = max(self.health - 10, 0)
        
        if self.happiness < 5:
            self.health = max(self.health - 5, 0)

        return is_alive


# Simulates having a pet; Uses the concept of threading to update the status of the pet
# https://en.wikipedia.org/wiki/Thread_(computing) 
class PetSimulator(Thread):

    def __init__(self, event, pet_name, pet_species):
        self.pet_name = pet_name
        self.pet_species = pet_species
        Thread.__init__(self)
        self.stopped = event
        self.pet = Pet(self.pet_name, self.pet_species)
        
    # When start() is called, this is automatically run.
    def run(self):
        # Every 5 seconds, we check if pet is okay. 
        while not self.stopped.wait(5):
            if not(self.pet.is_pet_okay()):
                 print(f"{self.pet_name} the {self.pet_species} is dying...")

        



game = PetSimulator(Event(), "Fifi", Species.CAT)
game.start()

is_playing = True

while is_playing:
    user_action = input("You may choose to FEED or PLAY or CHECK your pet: ")
    
    if user_action.lower() == "feed":
        game.pet.feed()
    elif user_action.lower() == "play":
        game.pet.play()
    elif user_action.lower() == "check":
        game.pet.check()
    else:
        user_action = input("Invalid input. Choose between FEED, PLAY, or CHECK.\nPress Enter to continue...")

    