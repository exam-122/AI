class FamilyTree:
    def __init__(self):
        self.parents = {} 
        self.gender = {}   

    def add_parent(self, child, parent):
        if child not in self.parents:
            self.parents[child] = []
        self.parents[child].append(parent)

    def set_gender(self, person, gender):
        self.gender[person] = gender

    def is_sibling(self, person1, person2):
        return (person1 in self.parents and person2 in self.parents and
                any(p in self.parents[person2] for p in self.parents[person1]) and person1 != person2)

    def is_grandparent(self, grandparent, grandchild):
        if grandchild in self.parents:
            for parent in self.parents[grandchild]:
                if parent in self.parents and grandparent in self.parents[parent]:
                    return True
        return False

    def get_siblings(self, person):
        siblings = []
        for other in self.parents.keys():
            if self.is_sibling(person, other):
                siblings.append(other)
        return siblings

    def get_parents(self, person):
        return self.parents.get(person, [])

    def get_grandparents(self, person):
        grandparents = []
        for parent in self.get_parents(person):
            grandparents.extend(self.get_parents(parent))
        return grandparents


family = FamilyTree()


family.set_gender("John", "male")
family.set_gender("Mary", "female")
family.set_gender("Paul", "male")
family.set_gender("Linda", "female")
family.set_gender("James", "male")
family.set_gender("Susan", "female")

family.add_parent("Paul", "John")
family.add_parent("Paul", "Mary")
family.add_parent("Linda", "John")
family.add_parent("Linda", "Mary")
family.add_parent("James", "Paul")
family.add_parent("Susan", "Paul")

print("Is Paul sibling of Linda?", family.is_sibling("Paul", "Linda"))
print("Is John grandparent of James?", family.is_grandparent("John", "James"))
print("Parents of Paul:", family.get_parents("Paul"))
print("Grandparents of Susan:", family.get_grandparents("Susan"))
print("Siblings of Linda:", family.get_siblings("Linda"))
