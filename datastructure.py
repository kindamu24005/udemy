r = [1,2,3,4,5,1,2,3]
print(r.index(3,3))

print(r.count(3))

if 5 in r:
    print("exist")

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = "My name is Mike."
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

i = [1,2,3,4,5]
j = i
j[0] = 100
print(i)
print(j)

x = [1,2,3,4,5]
y = x.copy()
y = x[:]
y[0] = 100
print(x)
print(y)


x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(y)
print(x)

x = ["a", "b"]
y = x
y[0] = "p"
print(id(x))
print(id(y))
print(y)
print(x)



num_tuple = (10,20)
print(num_tuple)
x,y=num_tuple
print(x,y)
x,y=10,20
print(x,y)

min,max=0,100
print(min,max)

a,b,c,d,e,f="Mike","1","1","1","e","f"
a = "Mike"
b = "1"

i=10
j=20
tmp=i
i=j
j=tmp
print(i,j)

a = 100
b = 200
print(a,b)
a,b=b,a
print(a,b)

chose_from_two = ("A","B","C")
answer=[]
answer.append("A")
answer.append("C")

print(chose_from_two)
print(answer)


x = {"a":1}
y=x
y["a"] = 1000
print(x)
print(y)

x = {"a":1}
y=x.copy()
y["a"]=1000
print(y)
print(x)



fruit = {
    "apple":100,
    "banana":200,
    "orange":300,
}
print(fruit["apple"])



my_friends = {"A","C","D"}
A_friends = {"B","D","E","F"}
print(my_friends&A_friends)

f = ["apple","banana","apple","banana"]
kind = set(f)
print(kind)
