import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return f'{self.name} ({self.phone})'

class PersonalContact(Contact):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email
        
    def __str__(self):
        return f'{super().__str__()} - {self.email}'

class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company
        
    def __str__(self):
        return f'{super().__str__()} - {self.company}'

class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([vars(c) for c in self.contacts], f)
        except Exception as e:
            print(f'Error saving file: {e}')
            
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for d in data:
                    if 'email' in d:
                        contact = PersonalContact(d['name'], d['phone'], d['email'])
                    else:
                        contact = BusinessContact(d['name'], d['phone'], d['company'])
                    self.add_contact(contact)
        except FileNotFoundError as e:
            print(f'Error loading file: {e}: File not found')
        except json.JSONDecodeError as e:
            print(f'Error loading file: {e}: Invalid JSON format')
        except Exception as e:
            print(f'Error loading file: {e}')
                

if __name__ == '__main__':
    book = AddressBook('contacts.json')
    book.add_contact(BusinessContact('Muhammad Haseeb', '+92314-9946492', 'Bytewise'))
    book.add_contact(PersonalContact('Muhammad Haseeb', '+92310-5156334', 'muhammad.haseeb@studentambassador.com'))
    book.save()
    
    book = AddressBook('contacts.json')
    book.load()
    for c in book.contacts:
        print(c)
