# comment
title = 'Smart Calculator'

running = True

def hello(name):
    print("It's me, ", name)
    h = input("Can I help You? (y,n): ")
    return h

while running:
    if hello(title) == 'n':
        print("THANK YOU FOR USING " + title )
        break
    op = input('Enter operation: ')
    if op == 'q':
        print("Programm done")
        running = False
    else:  
        a = input('Enter a = ')
        if a.isdigit():
            a = float(a)
        else:
            print("a shuold be digit")
            running = False
            break
        b = input('Enter b = ')
        if b.isdigit():
            b = float(b)
        else:
            print("b shuold be digit")
            running = False
            break
        # if op == 'q':
        #     print("Programm done")
        #     running = False
        if op == '+':
            print('a + b = ', a + b )
        elif op == '-':
            print('a - b = ', a - b )
        elif op == '*':
            print('a * b = ', a * b )
        elif op == '/':
            if b != 0:
                print('a / b = ', a / b )
            else:
                print('Oops, float division by zero')
        else:
            print("I don't know what You want")