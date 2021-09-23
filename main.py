my_tuple = (1,2,3,4,6)
hello = "Hello World"
print(hello[4])

char = 'c'
print(char[0])

l1 = [1,2,3]
l2 = [4,3,2,4,5,6,7,7,78]

print(l1 > l2)

for item in hello:
    print(item)

print(len(hello))

print(l1 + l2)
print([1,2, 'Help' ]*80)

newl = [0,0,0,0,0]
for i in [55,88,99,00]:
    newl.append(i)
    
newl.insert(2, 8888)
print(newl)
print(99 in newl)
print(newl.index(99))
print(newl.count(0))

while True:
    i = newl.index(0)
    if newl.count(0)>1:
        del newl[i]
    else:
        break
print(newl)

a, b, c, d, e = my_tuple
print(a, b, c, d, e)
