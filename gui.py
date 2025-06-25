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

    # Run the app
    window.mainloop()



