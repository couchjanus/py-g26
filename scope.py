# x = 2 
# y = 2
# print(x)

def counter():
    x = 0
    def f1():
        nonlocal x
        x += 1
        return x
    return f1

c = counter()

print(type(c))

print(c())
print(c())
print(c())
print(c())
print(c())

cc = counter()

print(type(cc))

print(cc())
print(cc())
print(cc())
print(cc())


print(c())
print(c())
print(c())
print(cc())

