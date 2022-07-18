# class Person(object):
#     def __init__(self, name):
#         self.name = name

#     def say_something(self):
#         print("I am {}. hello".format(self.name))
#         self.run(10)
    
#     def run(self, num):
#         print("run" * num)

#     def __del__(self):
#         print("good bye")

# person = Person("Mike")
# person.say_something()

# del person

# print("###############")

#######################################################
# import abc

# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age = 1):
#         self.age = age
    
#     @abc.abstractmethod
#     def drive(self):
#         pass

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         raise Exception("No drive")

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
    
#     def drive(self):
#         print("ok")

# baby = Baby()
# adult = Adult()
# adult.drive()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print("run")
#     def ride(self, person):
#         person.drive()


# class ToyotaCar(Car):
#     def run(self):
#         print("fast")


# class TeslaCar(Car):
#     def __init__(self, model="Model S", 
#                 enable_auto_run=False,
#                 passwd="123"):
#         # self.model = model
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#         self.password = passwd

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.password == "456":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print(self.__enable_auto_run)
#         print("super fast")
#     def aut_run(self):
#         print("auto run")

# tesla_car = TeslaCar("Model S", passwd="456")
# tesla_car.__enable_auto_run = "XXXXXXXXXXXXXXXXXX"
# print(tesla_car.__enable_auto_run)


# class T(object):
#     pass

# t = T()
# t.name = "Mike"
# t.age = 20
# print(t.name, t.age)

###############################################

# class Person(object):
#     def talk(self):
#         print("talk")
    
#     def run(self):
#         print("person run")

# class Car(object):
#     def run(self):
#         print("run")

# class PersonCarRobot(Person,Car):
#     def fly(self):
#         print("fly")

# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()

##############################################

# class Person(object):
    
#     kind = "human"

#     def __init__(self, name):
#         self.name = name

#     def who_are_you(self):
#         print(self.name, self.kind)

# a = Person("A")
# a.who_are_you()
# b = Person("B")
# b.who_are_you()

# class T(object):
#     def __init__(self):
#         self.words = []

#     def add_word(self, word):
#         self.words.append(word)

# c = T()
# c.add_word("add 1")
# c.add_word("add 2")
# print(c.words)

# d = T()
# d.add_word("add 3")
# d.add_word("add 4")
# print(d.words)

##############################################

# def about(year):
#     print("about human {}".format(year))

# class Person(object):

#     kind = "human"

#     def __init__(self):
#         self.x = 100

#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind

#     @staticmethod
#     def about(year):
#         print("about human {}".format(year))

# a = Person()
# print(a.what_is_your_kind())
# print(Person.what_is_your_kind())
# print(Person.kind)

# Person.about(1999)

##############################################

class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Word!!!!!!!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    # def __eq__(self, word):
    #     return self.text.lower() == word.text.lower()

w = Word("test")
w2 = Word("test")

print(id(w))
print(id(w2))

print(w == w2)