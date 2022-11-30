class mammal:
    def walk(self):
        print("walk")


class Dog(mammal):
    def bark(self):
        print("bark")


class Cat(mammal):
    def be_annooying(self):
        print("annoying")

dog1 = Dog()
dog1.bark()
dog1.walk()

cat1 = Cat()
cat1.walk()
cat1.be_annooying()