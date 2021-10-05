# fh = open('foo.text', 'w')
# fh = open('foo.text', 'a')

# try:
#     fh.write('\nAnd Bye world')
# except Exception as e:
#     print('Exception ', e)
# finally:
#     fh.close()
    
# print(f'File name: {fh.name}')
# print(f'File {fh.name} closed: {fh.closed}')
# fh.close()
# print(f'File {fh.name} closed: {fh.closed}')


with open('foo.text', 'a') as fh:
    fh.write('\nAdded some content with operator with')
    
with open('foo.text', 'r') as fh:
    content = fh.read()

print(content)
