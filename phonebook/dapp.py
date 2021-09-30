from datetime import datetime, time

choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')

contacts = [
    {
        'name': 'Mary Ann', 
        'phone': '1234567', 
        'address': '1, Marry st., Kiev city'
    },
    {
        'name': 'Tom Cat', 
        'phone': '222222', 
        'address': '1, Cats st., Kiev city'
    },
    {
        'name': 'Angry Dog', 
        'phone': '666666', 
        'address': '1, Dogs st., Kiev city'
    },
]

def welcome():
    prompt = '''
        Welcome to PhoneBook!
            At hand:\n'''
    for (i, item) in enumerate(choices):
        if i == 0: continue
        prompt += f"{' '*8} {i}: {item}\n"
    
    return input(prompt + f"{' '*8} Your choce(1,2,3,4,5 or 6): ")

fields = ('name', 'phone', 'address') 

def addContact():
    contact = {}
    for key in fields:
        value = input(f'Enter {key}: ')
        contact[key] = value
    contact['added'] = datetime.today().strftime("%Y-%m-%d")
    return contact

def findContact(contacts, name):
    if len(contacts) < 1:
        return
    for item in contacts:
        if item['name'].lower() == name.lower():
            return item
        else: return None

def editContact(contact):
    # contact = []
    for key in contact:
        value = input(f'Enter {key} please: ') or contact[key]
        contact[key] = value
    contact['added'] = datetime.today().strftime("%Y-%m-%d")
    contact.update()

def main():
    
    while True:
        choice = welcome()
        choice = int(choice if choice.isdigit() else 0)
        
        if choice == 0:
            continue
        elif choice == 1:
            print(contacts)
        elif choice == 2:
            contacts.append(addContact())
        elif choice == 3:
            name = input(f'Enter name for search please: ')
            result = findContact(contacts, name)
            if(result):
                for item in result.items(): print(item)
            else: print('Nothing found')

        elif choice == 4:
            name = input(f'Enter name for edit please: ')
            result = findContact(contacts, name)
            if result:
                index = contacts.index(result)     
                editContact(contacts[index])
            else: print('Nothing found for edit')
            
        elif choice == 5:
            name = input(f'Enter name for remove please: ')
            result = findContact(contacts, name)
            if result:
                index = contacts.index(result)
                contacts.remove(contacts[index])
            else: print('Nothing found for remove')
            
        elif choice == 6:
            print('Thanks for using PhoneBook!')
            break
        else:
            print('Incorrect Choice!')


if __name__ == '__main__':
    main()
    