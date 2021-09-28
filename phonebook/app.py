from datetime import datetime, time

choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')

contacts = []

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
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    return contact

def findContact():
    if len(contacts) < 1:
        return
    name = input(f'Enter {fields[0]} for search: ')
    for item in contacts:
        if name in item:
            return item
        else: return None

def editContact(x):
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    contacts[x] = contact

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
            result = findContact()
            contact = result if result else 'Nothing found'
            print(contact)
        elif choice == 4:
            result = findContact()
            if result:
                index = contacts.index(result)
                editContact(index)
            
        elif choice == 5:
            result = findContact()
            if result:
                index = contacts.index(result)
                del contacts[index]
            
        elif choice == 6:
            print('Thanks for using PhoneBook!')
            break
        else:
            print('Incorrect Choice!')


if __name__ == '__main__':
    main()
    