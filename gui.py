import tkinter
import os
from datetime import date
from tkinter import messagebox
import tkinter.simpledialog

# Making sure 'journals' folder exists
if not os.path.exists("journals"):

    messagebox.showerror("Error", "Journals folder not found. Please create it manually.")

else:
    
    def save_entry():
        entry_text = text_box.get("1.0", tkinter.END).strip()

        if entry_text:
            today = date.today()

            with open("journals/entries.txt", "a") as file:
                file.write(f"{today} ~ {entry_text}\n")

            messagebox.showinfo("Saved", "Journal entry saved successfully!")
            text_box.delete("1.0" , tkinter.END)

        else:
            messagebox.showwarning("Empty Entry", "Please write something before saving.")

    def view_entries():
        try:
            with open("journals/entries.txt", "r") as file:
                entries = file.readlines()

                # Create a new window
                top = tkinter.Toplevel(window)
                top.title("Journal Entries")
                
                # create a Text widget
                text = tkinter.Text(top, height=10, width=50)
                text.pack()

                for num, entry in enumerate(entries, start=1):
                    text.insert(tkinter.END, f"{num}. {entry}")
                
                # make the text box interactable
                text.config(state="disabled")
                
                # create a scrollbar
                scrollbar = tkinter.Scrollbar(top, command=text.yview)
                scrollbar.pack(side="right", fill="y")

                #Link the text to scrollbar
                text.config(yscrollcommand=scrollbar.set)

        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found. Try adding some first.")

    def filter_by_date():
        try:
            with open("journals/entries.txt", "r") as file:
                entries = file.readlines()
                
                # Asking for required Date
                user_date = tkinter.simpledialog.askstring("Date filter", "Enter the date to want to check YYYY-MM-DD :")
                
                # new window
                top = tkinter.Toplevel(window)
                top.title("Date Filter")
                
                # Add text box
                text = tkinter.Text(top, height=10, width=50)
                text.pack()

                matching = []
                for entry in entries:
                    journal_date, journal = entry.strip().split("~")
                    if user_date.strip() == journal_date.strip():
                        matching.append(journal.strip())
                
                if matching:
                    for item in matching:
                        text.insert(tkinter.END, f"{item}\n")
                else:
                    text.insert(tkinter.END, "No entries found for that date.")
                text.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found. Try adding some first.")

    # Gui Setup
    window = tkinter.Tk()
    window.title("Journal Tracker")
    window.geometry("400x500")

    # Label
    label = tkinter.Label(window, text="Write your journal entry below:")
    label.pack(pady=10)

    # Text Box
    text_box = tkinter.Text(window, height=10, width=40)
    text_box.pack()

    # Save Button     
    save_button = tkinter.Button(window, text="Save Entry", command=save_entry)
    save_button.pack(pady=4)

    # View entries Button
    view_button = tkinter.Button(window, text= "View entries", command=view_entries)
    view_button.pack(pady=4)

    # Filter by Date Button
    filter_button = tkinter.Button(window, text= "Filter by Date", command=filter_by_date)
    filter_button.pack(pady= 4)

    # Run the app
    window.mainloop()



