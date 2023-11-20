# TO DO:
# currently possible (if v unlikely) to generate two people with same name
"""
Lev distances between two 4-letter strings: 85% 4, 14% 3, <1% 2, 1 0
"""
import random
import string
from nltk.metrics import edit_distance
from wordlists import first_names, last_names

all_people = []

def four_letter_string():
    temp = ""
    for i in range(4):
        temp += random.choice(string.ascii_letters).lower()
    return temp

############# PERSON CLASS ############

class Person():

    def __init__(self):
        self.name = random.choice(first_names) + " " + random.choice(last_names)
        self.age = 0
        self.desires = {} # dict of desires (4-letter strings) and strengths (-10 to 10)
        self.esteems = {} # dict of names and overall likings for each person (-10 to 10)

        for i in range(5):
            self.generate_desire()

        all_people.append(self)

    def __repr__(self):
        return f"\nName: {self.name} \n Age: {self.age} \n Desires: {self.desires}"
    
    def generate_desire(self):
        self.desires[four_letter_string()] = random.randint(0,20) - 10
    
    def interact(self, other_person):

        print(f"{self.name} interacted with {other_person.name}!")
        
        effect1 = four_letter_string()
        # effect2 = four_letter_string() # ADD THIS IN LATER

        # if there's a lev distance between effect and desire of less than 4 for any desire then esteem should change by the desire strength
        # and prolly we should print something too 

        for attribute, strength in other_person.desires.items():
            if edit_distance(attribute,effect1) < 4:
                other_person.esteems[self.name] += strength
                print(f"{other_person.name}'s esteem changed by {strength}")





person1 = Person()
person2 = Person()

person2.interact(person1)
print(person1.esteems)
print(person2.esteems)