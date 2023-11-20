# testing to see what happens on test-branch

# TODO:
# conceivably two entities can have same name. But this doesn't matter

import random
from wordlists import first_names, last_names, make_name

MIN_REPRO_AGE = 3
DEATH_AGE = 50
DNA_RANGE_UPPER = 99
MAX_KIDS = 5
all_entities = []
year = 0
perfect_dnas_produced = 0

class Entity():

    def __init__(self):
        self.id = len(all_entities) + 1
        self.name = make_name()
        self.age = 0
        self.dna = []
        self.effectiveness = 1000
        self.parents = [make_name(), make_name()]
        self.children = []
        self.alive = True

        for i in range(0,5):
            self.dna.append(random.randint(0,DNA_RANGE_UPPER))

        all_entities.append(self)
        
    def __repr__(self):
        return self.name
    
    def can_reproduce(self,other):

        if other in self.parents or self in other.parents:
            print(f"{self.name} and {other.name} can't reproduce: parent and child")
            return False
        elif other.parents[0] in self.parents or other.parents[1] in self.parents:
            print(f"{self.name} and {other.name} can't reproduce: siblings")
            return False
        elif self.age < MIN_REPRO_AGE:
            print(f"{self.name} can't reproduce: too young")
            return False
        elif other.age < MIN_REPRO_AGE:
            print(f"{other.name} can't reproduce: too young")
            return False
        elif self == other:
            print(f"{self.name} can't reproduce with self")
            return False
        elif len(self.children) > MAX_KIDS:
            print(f"{self.name} can't reproduce: too many kids")
            return False
        elif len(other.children) > MAX_KIDS:
            print(f"{other.name} can't reproduce: too many kids")
            return False
        else:
            return True
        

    def reproduce(self, other):

        child = Entity()
        child.dna = [0,0,0,0,0]
        child.parents = [self, other]

        for i in range(0,5):
            if random.randint(0,5) == 0:
                # child.dna[i] = self.dna[i] + random.randint(0,19) - 10
                child.dna[i] = random.randint(0,DNA_RANGE_UPPER)
            else:
                if self.dna[i] == other.dna[i]:
                    child.dna[i] = self.dna[i] 
                else:
                    child.dna[i] = random.choice([self.dna[i],other.dna[i]])
        
        self.children.append(child)
        other.children.append(child)
    
        print(f"{self.name} (e{self.effectiveness}) and {other.name} (e{other.effectiveness}) produced: {child.name}, DNA: {child.dna}")


target = []
for i in range(5):
    target.append(random.randint(0,DNA_RANGE_UPPER))

print(f"TARGET: {target}")

for i in range(0,20):
    temp = Entity()

print(f"Community originally consists of: {all_entities}\n\n")



def time_cycle():
    global all_entities
    global year
    global perfect_dnas_produced

    year += 1
    print(f"YEAR {year}")

    for entity in all_entities:
        entity.age += 1

    # death comes knocking
    for entity in all_entities:
        if entity.age > DEATH_AGE:
            if random.randint(0,9) > 8:
                print(f"{entity.name} has died aged {entity.age}")
                entity.alive = False
    all_entities = list(filter(lambda x: x.alive, all_entities))

    # select entities of breeding age
    adults = list(filter(lambda x: x.age >= MIN_REPRO_AGE, all_entities))
    
    # if no two people are old enough to reproduce, nothing happens!
    if len(adults) < 2:
        print("No two people old enough to reproduce")
        return None

    # calculate effectiveness of every adult. Closer to 0 is better    
    for entity in adults:
        entity.effectiveness = sum([abs(val-target[i]) for i, val in enumerate(entity.dna)])

        if entity.effectiveness == 0:
            print(f"{entity.name} achieved target DNA!")
            perfect_dnas_produced += 1

    # sort by effectiveness
    adults.sort(key = lambda x: x.effectiveness)

    # MATING SEASON! ############################
    # two couples randomly generated from most successful 8 adults

    breeders = adults[:8]
    p1 = breeders.pop(random.randrange(0, len(breeders)))
    p2 = breeders.pop(random.randrange(0, len(breeders)))
    p3 = breeders.pop(random.randrange(0, len(breeders)))
    p4 = breeders.pop(random.randrange(0, len(breeders)))
    if p1.can_reproduce(p2):
        p1.reproduce(p2)
    if p3.can_reproduce(p4):
        p3.reproduce(p4)

############### END OF TIME CYCLE ################

for i in range(1000):
    time_cycle()

print(f"TARGET WAS: {target}")
for entity in all_entities:
    print(f"{entity.name}, {entity.age} years old, DNA: {entity.dna}. EFFECTIVENESS: {entity.effectiveness}")
print(f"Perfect DNA count: {perfect_dnas_produced}")

# new_var = True
# while new_var:
#     char = input("Enter name: ")
#     for entity in all_entities:
#         if entity.name == char:
#             print(entity.children)





