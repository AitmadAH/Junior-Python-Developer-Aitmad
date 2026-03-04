

def start_phonebook():
    my_contacts = {
        "Ahsan": "0300-1234567",
        "Ahmed": "0311-9876543",
    }

    print("MY CONTACT LIST")
    
    while True:
        print("What do you want to do?")
        print("1. Add a new person")
        print("2. Look up a number")
        print("3. Show everyone")
        print("4. Close")
        
        user_choice = input("Pick a Choice: ")

        if user_choice == "1":
            name = input("Enter their name: ")
            phone = input("Enter their number: ")
            my_contacts[name] = phone
            print(f"Got it! Saved {name}.")

        elif user_choice == "2":
            search = input("Who are you looking for? ")
            if search in my_contacts:
                print(f"{search}'s number is: {my_contacts[search]}")
            else:
                print("Sorry, that name isn't in the list.")

        elif user_choice == "3":
            print(" All Contacts ")
            for person, num in my_contacts.items():
                print(f"{person}: {num}")

        elif user_choice == "4":
            print("Closing the app. Bye!")
            break
            
        else:
            print("That's not a valid option, try again.")

start_phonebook()
