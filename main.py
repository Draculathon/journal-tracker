from datetime import date

print("Welcome to Journal Tracker!")
#TODO: implemet delete_entry function

def menu():
    print("1. Add a journal entry")
    print("2. View entries")
    print("3. Filter entries by date")
    print("4. Exit")

def add_entry():
    with open("journals/entries.txt","a") as file:
        entry = input("Enter your entry journal: ").strip()
        today = date.today()
        file.write(f"{today} ~ {entry}\n")
        print("Entry has been added successfully!")

def read_entries():
    try:
        with open("journals/entries.txt","r") as file:
            entries = file.readlines()
            for num, entry in enumerate(entries, start= 1):
                print(f"{num}. {entry.strip()}")
    except FileNotFoundError:
        print("No Entries found yet, try adding some first!")

def filter_by_date():
    pass

while True:
    print()
    menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a number, Try again!")
    
    if choice == 1:
        add_entry()
        print()
    elif choice == 2:
        read_entries()
        print()
    elif choice == 3:
        pass
    elif choice == 4:
        print("GoodBye!")
        break
    else:
        print("Option unavailable, Try Again")