
#simple contact book for college project

import json

def load_contact():
    try:
        with open('contacts.json','r') as f:
            return json.load(f)
    except:
        return{}

def save_contacts(data):
    with open('contacts.json','w') as f:
        json.dump(data,f,indent=2)

def add_contact(contacts):
    print("\n---add contact---")
    name=input('enter name')
    phone=int(input('enter phone number'))
    email=input('email (optional):')
    contacts[name]={
        "phone":phone,"email":email
        }

    save_contacts(contacts)
    print('contact saved successfully')

def view_contacts(contacts):
    print("\n---all contacts---")
    if len(contacts)==0:
        print('no contacts found')
        return

    for n in contacts:
        print('name:',n)
        print('phone:',contacts[n]['phone'])
        if contacts[n]['email']:
            print('email:',contacts[n]['email'])
            print('----')

def search_contact(contacts):
    print("\n---search contact---")
    name=input('enter name to search')

    if name in contacts:
        print('contact found')
        print('name:',name)
        print('phone:',contacts[name]['phone'])
        print('email:',contacts[name]['email'])
    else:
        print('no such contact.')

def delete_contact(contacts):
    print("\n----delete contact----")
    name=input('enter name to delete:')

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print('contact deleted')
    else:
        print('contact not found')

def main():
    contacts=load_contact()
    while True:
        print("\n===CONTACT BOOK===")
        print("1.add contact")
        print("2.view contact")
        print("3.search contact")
        print("4.delete contact")
        print("5.exit")

        ch=input('choose an option')

        if ch=="1":
            add_contact(contacts)
        elif ch=="2":
            view_contacts(contacts)
        elif ch=="3":
            search_contact(contacts)
        elif ch=="4":
            delete_contact(contacts)
        elif ch=="5":
            print('thank you for using contact book')
            break
        else:
            print('invalid option,try again')

if __name__=="__main__":
    main()
        
    
