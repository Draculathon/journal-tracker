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
        mood = mood_slot.get().strip() or "Unknown"
        weather = weather_slot.get().strip() or "Unknown"
        today = date.today()
        
        if entry_text:

            with open("journals/entries.txt", "a") as file:
                file.write(f"{entry_text} ~ {today} ~ {mood} ~ {weather}\n")

            messagebox.showinfo("Saved", "Journal entry saved successfully!")
            text_box.delete("1.0" , tkinter.END)
            mood_slot.delete(0, tkinter.END)
            weather_slot.delete(0, tkinter.END)

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
                    journal, journal_date, mood, weather = entry.strip().split("~")

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

    def delete_entry():
        try:
            with open("journals/entries.txt", "r") as file:
                entries = file.readlines()

                top = tkinter.Toplevel(window)
                top.title("Entries")

                text = tkinter.Text(top, height=10, width=50)
                text.pack()

                for num, entry in enumerate(entries, start=1):
                    text.insert(tkinter.END, f"{num}. {entry}")
                text.config(state="disabled")

                # Asking for Entry Number
                label = tkinter.Label(top, text="Enter the number of the entry you would like to delete: ")
                label.pack()
                blog = tkinter.Entry(top)
                blog.pack()

                def confirm_delete():
                    number = blog.get()
                    if number.isdigit():
                        number = int(number)
                        if 1 <= number <= len(entries):
                            del entries[number - 1]
                            with open("journals/entries.txt", "w") as file:
                                file.writelines(entries)
                            messagebox.showinfo("Deleted", "Entry deleted successfully.")
                            top.destroy()
                        else:
                            messagebox.showerror("Error", "Entry number out of range.")
                    else:
                        messagebox.showerror("Error", "Invalid input, please enter a valid entry number.")

            sub_delete_button = tkinter.Button(top, text="Delete", command=confirm_delete)
            sub_delete_button.pack(pady=5)
            
        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found, Try adding some first!")

    def edit_entry():
        try:
            with open("journals/entries.txt", "r") as file:
                entries = file.readlines()
                
                top = tkinter.Toplevel(window)
                top.title("Edit Entries")
                top.geometry("400x400")

                text = tkinter.Text(top , height=10, width=50)
                text.pack()

                for num, entry in enumerate(entries, start=1):
                    text.insert(tkinter.END, f"{num}. {entry}")
                text.config(state="disabled")

                label = tkinter.Label(top, text="Enter an entry to edit:")
                label.pack(pady= 3)

                entry = tkinter.Entry(top)
                entry.pack(pady=5)

                def confirm_edit():
                    number = entry.get()
                    if number.isdigit():
                        number = int(number)
                        if 1 <= number <= len(entries):
                            bottom = tkinter.Toplevel(top)
                            bottom.title("Editing blog")

                            sub_text = tkinter.Text(bottom, height=10, width=40)
                            sub_text.pack()

                            old_entry = entries[number - 1].strip()
                            sub_text.insert(tkinter.END, old_entry)

                            def sub_save_entry():

                                new_entry = sub_text.get("1.0", tkinter.END).strip()
                                entries.insert(number - 1, new_entry + "\n")
                                global old_entry
                                del old_entry
                                with open("journals/entries.txt", "w") as file:
                                    file.writelines(entries)
                                
                                messagebox.showinfo("Success", "Entry updated successfully!")
                                bottom.destroy()
                                top.destroy()

                            sub_save_button = tkinter.Button(bottom, text="save", command=sub_save_entry)
                            sub_save_button.pack(pady=5)
                            
                        else:
                            messagebox.showerror("Error", "Entry number doesn't exist, try again.")
                    else:
                        messagebox.showerror("Error", "Input must be a number.")                
                
                sub_edit_button = tkinter.Button(top, text="Edit", command=confirm_edit)
                sub_edit_button.pack(pady=5)

        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found, try adding some first.")

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

    # Mood slot
    mood_text = tkinter.Label(window,text="Mood:")
    mood_slot = tkinter.Entry(window)
    mood_text.pack()
    mood_slot.pack(pady= 5)

    # Weather slot
    weather_text = tkinter.Label(window, text="Weather:")
    weather_slot = tkinter.Entry(window)
    weather_text.pack()
    weather_slot.pack(pady=5)

    # Save Button     
    save_button = tkinter.Button(window, text="Save Entry", command=save_entry)
    save_button.pack(pady=4)

    # View entries Button
    view_button = tkinter.Button(window, text= "View Entries", command=view_entries)
    view_button.pack(pady=4)

    # Filter by Date Button
    filter_button = tkinter.Button(window, text= "Filter By Date", command=filter_by_date)
    filter_button.pack(pady= 4)

    # Delete Entry Button
    delete_button = tkinter.Button(window, text="Delete Entry", command=delete_entry)
    delete_button.pack(pady=4)

    # Edit Entry Button
    edit_button = tkinter.Button(window, text= "Edit Entry" , command=edit_entry)
    edit_button.pack(pady=4)

    # Run the app
    window.mainloop()



