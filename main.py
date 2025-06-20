from datetime import date, datetime

print("Welcome to Journal Tracker!")
#TODO: implemet delete_entry function

def menu():
    print("1. Add a journal entry")
    print("2. View entries")
    print("3. Filter entries by date")
    print("4. Delete entry")
    print("5. Search entry")
    print("6. Exit")

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
    try:
        with open("journals/entries.txt", "r") as file:
            entries = file.readlines()
            
            year = int(input("Enter the year: "))
            month = int(input("Enter the month 1-12: "))
            day = int(input("Enter the day 1-31: "))

            chosen_date = date(year,month,day)
            
            found = False

            for journal in entries:
                journal = journal.strip()
                journal_date_str, entry = journal.split("~")
                journal_date_str = journal_date_str.strip()
                journal_date = datetime.strptime(journal_date_str, "%Y-%m-%d").date()
                if chosen_date == journal_date:
                    print(f"-{entry}")
                    found = True

            if not found:
                print("No entries found!")
                   
    except FileNotFoundError:
        print("No journal found, Try adding some first!")
    except ValueError:
        print("Invalid input or date. Please enter correct numbers.")

def delete_entry():
    try:
        with open("journals/entries.txt", "r") as file:
            entries = file.readlines()
            
            for num, entry in enumerate(entries, start= 1):
                print(f"{num}. {entry}")
            
            delete_num = int(input("Enter the entry number you want to delete: "))
            
            if delete_num > len(entries):
                print("Invalid choice. Please enter a number from the list.")
            else:
                choice = input(f"Are you sure you want to delete entry {delete_num}: ").lower()
                if choice == "yes":
                    del entries[delete_num - 1]

                    with open("journals/entries.txt", "w") as file:
                        file.writelines(entries)
                        print("Entry deleted successfully!")
                else: 
                    pass
    except FileNotFoundError:
        print("No entries to delete.")
    except ValueError:
        print("Input invalid, try again!")

def search_entry():
    try:
        with open("journals/entries.txt", "r") as file:
            entries = file.readlines()
            keyword = input("Enter keyword to search for: ").strip()
            found = False
            for num, entry in enumerate(entries,start= 1):
                if keyword.lower() in entry.lower():
                    print(f"{num}. {entry.strip()}")
                    found = True
            if not found:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No entries yet, try adding some!")

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
        filter_by_date()
    elif choice == 4:
        delete_entry()
    elif choice == 5:
        search_entry()
    elif choice == 6:
        print("GoodBye!")
        break
    else:
        print("Option unavailable, Try Again")