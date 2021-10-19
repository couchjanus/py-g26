# myl = [x*x for x in range(5)]
# print(myl)
# for i in myl:
#     print(i)

# my = (x*x for x in range(5))
# print(my)
# for i in my:
#     print(i)
    
# log = open('access-log.txt')
# byt = (line.rsplit(None,1)[1] for line in log)
# byts = (int(x) for x in byt if x !='-')
# print("Total: ", sum(byts))

# def mygen():
#     ml = range(5)
#     for i in ml:
#         yield i*i
        
# print(mygen())
# tmp = mygen()
# for i in tmp:
#     print(i)
    
# for i in mygen():
#     print(i)
    
def simple_gen(value):
    while value > 0:
        value -= 1
        yield value + 1
        
# gen_iter = simple_gen(7)

# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


# def foofinder():
#     with open('foo.txt') as f:
#         for line in f:
#             if 'foo' in line:
#                 yield line
                
# for i in foofinder():
#     print(i)

def gen():
    i = 0
    while True:
        yield i
        i += 1
        
g = gen()

# for i in range(10000):
#     print(next(g))
    
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def cube(n):
#     cube_list = []
#     for i in n:
#         cube_list.append(i**3)
#     return cube_list

# cubes = cube([5,7,8,2,3,5])

# print(cubes)

# def cube(n):
#     for i in n:
#         yield i**3

# cubes = cube([5,7,8,2,3,5])

# print(next(cubes))
# print(next(cubes))
# print(next(cubes))

# def fibo():
#     prev, cur = 0, 1 
#     while True:
#         yield prev
#         prev, cur = cur, prev + cur
        
# for i, f in enumerate(fibo()):
#     print('{}: {}'.format(i, f))
#     if i > 10000:
#         break

# def crange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
        
# for n in crange(1, 55, 0.5):
#     print(n)


import itertools

# def gen():
#     counter = itertools.count()
#     while True:
#         yield next(counter)
    
# g1 = gen()
# g2 = gen()

# for i in g1:
#     print(i, end=" ")
#     if i == 8:
#         g1.close()
        
# for i in g2:
#     print(i, end=" ")
#     if i == 8:
#         g1.throw(Exception('Everything is bad'))
        

# def gen():
#     counter = itertools.count()
#     while True:
#         y = (yield next(counter))
#         if y:
#             counter = itertools.count(y)
        
    
# g1 = gen()
# # g2 = gen()

# for i in g1:
#     print(i, end=" ")
#     if i == 5:
#         g1.send(5)
#     elif i == 7:
#         g1.close()
 
def gen():
    i = 0 
    while True:
        yield i
        i += 1
        
for i in itertools.islice(gen(), 55):
    print(i)
