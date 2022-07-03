from ast import Num
from turtle import color
from cv2 import bilateralFilter


print("XXXX")
"""
test
test
test
"""
print("XXXXX")
#Apple price
some_value=100


s="aaaaaaaaaaaaaa" \
    + "bbbbbbbbbbbbbbb"
print(s)

x = (1+1+1+1+1+1+1+1+1 
    +1+1+1+1+1+1+1+1+1+1+1+1+1)
print(x)

a=5
b=10
if a > 0:
    print("a is positive")
    if b > 0:
        print("b is positive")

a = 2
b = 2
print(a>=b)

y = [1,2,3]
x = 1
if x in y:
    print("in")
if 100 not in y:
    print("not in")

a = 1
b = 2
if a != b:
    print("Not equal")

#is_ok = True
# False, 0, 0.0, "",[],(),{}
is_ok = [1,2,3,4]
if is_ok:
    print("OK!")
else:
    print("No!")

is_empty = None
#print(help(is_empty))

if is_empty is None:
    print("None!!!")


print(1 == True)
print(1 is True)
print(None is None)


#count = 0
#while count < 5:
#    print(count)
#    count += 1

count = 0
while True:
    if count >=5:
        break
    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


count = 0
while count <5:
    print(count)
    count += 1
else:
    print("done")


"""
while True:
    word = input("Enter:")
    num = int(word)
    if num == 100:
        break
    print("next")
"""

some_list=[1,2,3,4,5]
#i=0
#while i < len(some_list):
#    print(some_list[i])
#   i+=1
for i in some_list:
    print(i)

for word in ["My", "name", "is", "Mike"]:
    if word == "name":
        continue
    print(word)


for fruit in ["apple", "banana", "orange"]:
    if fruit == "banana":
        print("stop eating")
        break
else:
    print("I ate all")


#num_list=[0,1,2,3,4,5,6,7,8,9]
#for i in range(2, 10, 3):
#    print(i)

for _ in range(10):
    print("hello")

#################################################
for i,fruit in enumerate(["apple","banana","orange"]):
    print(i,fruit)

days = ["Mon","Tue","Wed"]
fruits = ["apple","banana","orange"]
drinks = ["coffe","tea","beer"]

#for i in range(len(days)):
    #print(days[i],fruits[i],drinks[i])

for day, fruit, drink in zip(days,fruits,drinks):
    print(day,fruit,drink)


d = {"x":100,"y":200}

print(d.items())
for k,v in d.items():
    print(k,v)


def say_something():
    s = "hi"
    return s
result=say_something()
print(result)

def what_is_this(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green papper"
    else:
        return "I don't know"

result = what_is_this("red")
print(result)


def add_num(a:int,b:int) -> int:
    return a+b
r = add_num(10,20)
print(r)


def menu(entree="beef",drink="wine",dessert="ice"):   
    print("entree=",entree)
    print("drink=",drink)
    print("dessert=",dessert)
menu()
menu(entree="chicken",dessert="ice",drink="beer")


def test_func(x,l=None):
    if l is None:
        l=[]
    l.append(x)
    return l
# y = [1,2,3]
# r=test_func(100,y)
# print(r)

# y = [1,2,3]
# r=test_func(200,y)
# print(r)

r = test_func(100)
print(r)
r = test_func(100)
print(r)


def say_something(word,*args):
    print("word=",word)
    for arg in args:
        print(arg)

say_something("Hi!","Mike","Nance")
# t=("Mike","Nancy")
# say_something("Hi!",*t)

def menu(food,*args,**kwargs):
    #print(kwargs)
    #for k, v in kwargs.items():
        print(food)
        print(args)
        print(kwargs)

# d = {
#     "entree":"beef",
#     "drink":"ice coffee",
#     "dessert":"ice"
# }
menu("banana","apple","orange",entree="beef",drink="coffee")



#############################関数内関数####################################
def outer(a,b):
    def plus(c,d):
        return c+d
    r1 = plus(a,b)
    r2 = plus(b,a)
    print(r1+r2)
outer(1,2)
##########################################################################

# def outer(a,b):
#     def inner():
#         return a+b
#     return inner
# f = outer(1,2)

# print("######")

# r = f()
# print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))


def print_more(func):
    def wrapper(*args,**kwargs):
        print("func:", func.__name__)
        print("args:",args)
        print("kwargs:", kwargs)
        result = func(*args,**kwargs)
        print("resule:",result)

        return result
    return wrapper

def print_info(func):
    def wrapper(*args,**kwargs):
        print("start")
        result = func(*args,**kwargs)
        print("end")
        return result
    return wrapper

@print_info
@print_more
def add_num(a,b):
    return a+b

r = add_num(10,20)
print(r)

# @print_info
# def add_num(a,b):
#     return a-b

# f = print_info(add_num)
# r = f(10,20)
# print(r)

# print("start")
# r = add_num(19,20)
# print("end")

# print(r)


l = ["Mon","tue","Wed","Thu","fri","sat","Sun"]

def change_words(words,func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# sample_func = lambda word: word.capitalize()

change_words(l,lambda word: word.capitalize())
change_words(l,lambda word: word.lower())


# l = ["Good morning", " Good afternoon", "Good night"]

# for i in l:
#     print(i)

# print("##################")

#######################ジェネレーター############################

def counter(num=10):
    for _ in range(num):
        yield "run"

def greeting():
    yield "Good morning"

    yield "Good afternoon"

    yield "Good night"

g = greeting()
c = counter()
print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))


######################################

t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)


r = [i for i in t if i % 2 == 0]

print(r)


r = []
for i in t:
    for j in t2:
        r.append(i*j)
print(r)


r = [i*j for i in t for j in t2]

print(r)


w = ["Mon","Tue","Wed"]
f = ["coffee","molk","water"]

d = {}
for x,y in zip(w,f):
    d[x]=y
print(d)

d={x:y for x,y in zip(w,f)}
print(d)

s = set()
for i in range(10):
    if i % 2 == 0:
        s.add(i)   
print(s)

s={i for i in range(10) if i % 2 == 0}
print(s)




def g():
    for i in range(10):
        yield i
g = g()



g = (i for i in range(10) if i % 2 ==0)
print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for x in g:
    print(x)



animal="cat"
def f():
    """test func doc"""
    # print(f.__name__)
    # print(f.__doc__)

f()
print("gloval:",globals())


l = [1,2,3]
i = 5

try:
    l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other: {}".format(ex))
else:
    print("done")
finally:
    print("clean up")



class UppercaseError(Exception):
    pass

def check():
    words = ["APPLE","banana","orange"]
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as ex:
    print("This is my fault. Go next")













