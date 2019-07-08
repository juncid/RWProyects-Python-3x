
f = open("contacts.txt", 'w')
f.write("Mickey Mouse|mickey.mouse@disney.com|Y\n")
f.close()

f = open("contacts.txt", 'a')
f.write("Donald Duck|donald.duck@disney.com|Y\n")
f.close()

f = open("contacts.txt", 'r')
contacts = f.read()
print(contacts)

def read_contacts(file_name):
    f = open("contacts.txt", 'r')
    data = f.read().split('|')
    contacts = []
    for contact in data:
        if len(contact)> 0:
            contacts.append(contact.split('|'))

    return contacts
