import tkinter
import os
from datetime import date
from tkinter import messagebox

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
                text.config(state="disabled")
                
                # create a scrollbar
                scrollbar = tkinter.Scrollbar(top, command=text.yview)
                scrollbar.pack(side="right", fill="y")

                #Link the text to scrollbar
                text.config(yscrollcommand=scrollbar.set)

        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found. Try adding some first.")

    # Gui Setup
    window = tkinter.Tk()
    window.title("Journal Tracker")
    window.geometry("400x300")

    # Label
    label = tkinter.Label(window, text="Write your journal entry below:")
    label.pack(pady=10)

    # Text Box
    text_box = tkinter.Text(window, height=10, width=40)
    text_box.pack()

    # Save Button     
    save_button = tkinter.Button(window, text="Save Entry", command=save_entry)
    save_button.pack(pady=10)

    # View entries Button
    view_button = tkinter.Button(window, text= "View entries", command=view_entries)
    view_button.pack(pady=4)

    # Run the app
    window.mainloop()



