# Define a class, which have a class parameter and have a same instance parameter.

class human:
    age = 10

    def getAge(self):
        return self.age

lulu = human()
lulu.age = 8
mama = human()
mama.age =9
print(mama.getAge())
print(lulu.age)


 