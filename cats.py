#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Garfield", 9)
cat2 = Cat("Tom", 8)
cat3 = Cat("Don Gato", 12)

# 2 Create a function that finds the oldest cat

def oldestCat(lista):
    oldie = lista[0]
    for i in lista:
        if i.age > oldie.age:
            oldie = i
    return oldie

oldcat = oldestCat([cat1, cat2, cat3])

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldcat.age}. His name is {oldcat.name}")