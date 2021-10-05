# import csv

# FL = 'people.csv'

# people = [
#     {'name':'Tom','phone': 1111111},
#     {'name':'Mary','phone': 2222222},
#     {'name':'Bob','phone': 3333333},
# ]

# # with open('book.csv', 'w', newline='') as fh:
# #     writer = csv.DictWriter(fh, ['name', 'phone'])
# #     writer.writeheader()
# #     writer.writerows(people)
#     # for row in reader:
#     #     print(row[0], '->', row[1] )
    
# with open('book.csv', 'r', newline='') as fh:
#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row['name'], '->', row['phone'] )


import os

print(os.name)
# print(os.environ)
# print(os.getenv('SYSTEMROOT'))

print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())

# dirs = os.listdir(os.getcwd())

# for f in dirs:
#     print(f)
    
# print(os.stat('book.csv'))

# item = './test'

# print(os.path.exists(item))

# if not os.path.exists(item):
#     os.mkdir(item)
    
# print(os.path.exists(item))

# # os.makedirs('./test/dir1/dir2/dir3')

# os.rename('book.csv', './test/dir1/dir2/phonebook.csv')


for dirname, dirnames, filenames in os.walk('phonebook'):
    for name in dirnames:
        print(os.path.join(dirname, name))
        
    for file in filenames:
        print(os.path.join(dirname, file))