a = []
for i in range(10):
    a.append(i**3)
print(a)

print([x**3 for x in range(10)])

print([s.upper() for s in "Hello world"])

print([w.strip(',') for w in ['nla,', ',bla,', 'world,', ',hello']])

sentens = 'Beautiful is better than ugly'
print([''.join(sorted(word, key = lambda x: x.lower())) for word in sentens.split()])


c = 4
n = c if c % 2 else c - 1
print(n)

user = {'name': 'Mary'}

name = user['name'] if user is not None else 'Guest'


print([x for x in range(10) if x % 2 == 0 ])

print([x if x % 2 == 0 else None for x in range(10)])

print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)])

print([x + y for x in range(5) if x > 2 for y in range(5,10)])

print([x + y for x in range(5) for y in range(5, 10) if x > 2])


print([i for i in sentens if i in 'aeiou'])

sent = '''In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.'''


def is_cons(letter):
    v = 'aeiou'
    return letter.isalpha() and letter.lower() not in v

print([i for i in sent if is_cons(i)])
print()
print([x if x > 2 else '*' for x in range(10) if x % 2 == 0])

print([x if (x > 2 and x % 2 == 0 ) else '*' for x in range(10)])

from string import ascii_letters

letters = 'яжіиєїhello'

is_en = [f'{l}-en' if l in ascii_letters else f'{l}-ua' for l in letters]

print(is_en)

print([i if i > 0 else 0 for i in [1.22, -111, 33.55, -0, -22, 3,14]])


print([x + y for x, y in [(1,2), (3,4), (5,6)]])

print([x + y + z for x, y, z in zip([1,3,5], [2,4,6], [2,4,6])])

print([int(i) for i in ['2', '55', '77']])

print(list(map(float, ['2', '55', '77'])))

print(dict((x, x*x) for x in (3,5,7)))


print({key: value for key, value in {'x':2, 'y':6}.items() if key == 'x'})

my_d = {1: 'a', 2: 'b', 3: 'c'}

swap = {v: k for k, v in my_d.items()}
print(swap)

print(dict(zip(my_d.values(), my_d)))
print(dict(zip(my_d.values(), my_d.keys())))
print(dict(map(reversed, my_d.items())))

dd = {'z': 7, 'b': 8, 'r': 9, 'c': 77}

print({k: v for d in [swap, dd] for k, v in d.items()})