# def call_this(f):
#     f()
#     print("Colled This")
    
# def call_foo(f):
#     f("Hello ")
    
# def bar(hello = ''):
#     print(hello + "Colled bar function")
    
# call_this(bar)
# call_foo(bar)


# def lawercase(f):
#     def wrapper():
#         return f().lower()
#     return wrapper
# def test_f():
#     return "HELLO SIMOLE DECORATOR"

# decor = lawercase(test_f)

# print(type(decor))
# print(decor())


def transpass(f):
    def new_f(x):
        return f(float(x))
    return new_f

@transpass
def foo(x):
    return x**2

@transpass
def bar(x):
    return x**0.5

print(foo('3'))
print(bar('7'))
