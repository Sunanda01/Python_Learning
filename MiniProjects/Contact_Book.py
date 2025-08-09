print(" ---------- CONTACT BOOK ---------- ")
contact_list={}
flag=True   
while(flag):
    total_contact=len(contact_list)
    choice=int(input('1. Create Contact\n2. View Contact\n3. Update Contact\n4. Delete Contact\n5. Search Contact\n6. View All Contacts\n7. Count Contact\n0. Exit\nEnter your choice = '))
    if choice==1:
        name=input("Enter name = ")
        if name in contact_list:
           print("Contact Name Already Exists!!!!!!")
        else:
            email=input("Enter email = ")
            mob=input("Enter mobile number = ")
            contact_list[name]={'email':email,'mob':mob}
            print(f"Contact {name} created successfully")

    elif choice==2:
        if(total_contact==0):
            print("Contact List is Empty!!!!!!!!")
        else:
            name=input("Enter the name of contact to view = ")
            if name in contact_list:
                contact=contact_list[name]
                print(f"Name = {name}, Email = {contact['email']}, Mobile Number = {contact['mob']}")
            else:
                print("Contact Not Found!!!!!!!")

    elif choice==3:
        if total_contact==0:
            print("Contact List is Empty!!!!!!!!")
        else:
            name=input("Enter the name of contact to update = ")
            if name in contact_list:
                old_email=contact_list[name]['email']
                old_mob=contact_list[name]['mob']
                email=input(f"Updated email = (Old email = {email} Leave Blank to keep ) : ") or old_email
                mob=input(f"Updated mobile number = (Old mobile number = {mob} Leave Blank to keep ) : ") or old_mob
                contact_list[name]={'email':email,'mob':mob}
                print(f'Contact {name} updated successfully')
            else:
                print(f'Contact {name} Not Found!!!!!!!!')

    elif choice==4:
        if(total_contact==0):
            print('Contact List is Empty!!!!!!!!')
        else:
            name=input("Enter the name of contact to delete = ")
            if name in contact_list:
                del contact_list[name]
                print(f'Contact {name} deleted successfully')
            else:
                print(f'Contact {name} Not Found!!!!!!!!')

    elif choice==5:
        if(total_contact==0):
            print("Contact List is Empty!!!!!!!!")
        else:
            search_name=input("Enter the name of contact you are searching for = ")
            found=False
            for name,contact in contact_list.items():
                if search_name.lower() in name.lower():
                    contact=contact_list[name]
                    print(f"Contact Found\nName = {name}, Email = {contact['email']}, Mobile Number = {contact['mob']}")
                    found=True
            if not found:
                print(f"Contact Not Found with name {search_name}!!!!!!!")

    elif choice==6:
        if(total_contact==0):
            print("Contact List is Empty!!!!!!!!")
        else:
            for name,contact in contact_list.items():
                print(f"Name = {name}\nEmail = {contact['email']}\nMobile Number = {contact['mob']}\n\n")

    elif choice==7:
        if total_contact:
            print(f"Total contact in your list is {total_contact}")
        else:
            print("Contact List is Empty!!!!!!!!")

    elif choice==0:
        print("GOOD BYE!!!!!!!!")
        flag=False

    else:
        print('INVALID CHOICE!!!!!!!!!!')
        flag=False