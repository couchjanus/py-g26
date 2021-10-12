plus = lambda x: x + 1

print(plus(1))


print((lambda x: x*x)(9))


full_name = lambda fn, ln: f'Full name: {fn.title()} {ln.title()}'

print(full_name('tom', 'cat'))

import math

sqrt = lambda x: math.sqrt(x)

print(sqrt(7))

print((lambda x:
    (
        x%2 and 'odd' or 'even'
    ) 
)(72))

def inc(n):return lambda x:x+n

f = inc(99)
g = inc(4)

print(f(77), g(99))

print(inc(77)(99))