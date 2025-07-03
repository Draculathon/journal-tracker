import tkinter
import os
from datetime import date
from tkinter import messagebox
import tkinter.font
import tkinter.simpledialog

def read_entries():
        with open("journals/entries.txt", "r") as file:
            return file.readlines()

def write_entries(entries):
    with open("journals/entries.txt", "w") as file:
        file.writelines(entries)

# Making sure 'journals' folder exists
if not os.path.exists("journals"):

    messagebox.showerror("Error", "Journals folder not found. Please create it manually.")

else:
    
    def save_entry():
        """
        This function takes the entry, mood and weather and stores them into a file with the time it was activated.

        Parameters:
        entry (string): user's journal.
        date(YYYY-MM-DD): the moment the user activates the function.
        mood (string): user's mood or default value 'Unknown'.
        weather (string): user's weather's state or default value 'Unknown'.

        Returns:
        Entry saved into the file, with success message or Error if the Entry had problems.
        """
        entry_text = text_box.get("1.0", tkinter.END).strip()
        mood = mood_slot.get("1.0", tkinter.END).strip() or "Unknown"
        weather = weather_slot.get("1.0", tkinter.END).strip() or "Unknown"
        today = date.today()
        
        # The condition wont work 100% because mood/weather = "Unknown" by default which is > 2.

        if not entry_text:
            messagebox.showwarning("Empty Entry","Please write something before saving.")
        elif "~" in entry_text or "~" in mood or "~" in weather:
            messagebox.showwarning("Warning", "Please do not use ~ Symbol.")
        else:
            with open("journals/entries.txt", "a") as file:
                file.write(f"{entry_text} ~ {today} ~ {mood} ~ {weather}\n")

            messagebox.showinfo("Saved", "Journal entry saved successfully!")
            text_box.delete("1.0" , tkinter.END)
            mood_slot.delete("1.0", tkinter.END)
            weather_slot.delete("1.0", tkinter.END)
        
    def view_metadata():
        """
        This function view all the entries in the file, Entry / date / mood / weather.

        Parameters:
        entry (string): user's journal.
        date(YYYY-MM-DD): the moment the user activates the function.
        mood (string): user's mood or default value 'Unknown'.
        weather (string): user's weather's state or default value 'Unknown'.

        """
        try:
                entries = read_entries()
                
                top = tkinter.Toplevel(window)
                top.title("Metadata")

                scrollbar = tkinter.Scrollbar(top)
                scrollbar.pack(side="right", fill="y")

                text = tkinter.Text(top , wrap="word", yscrollcommand=scrollbar.set)
                text.pack(expand=True, fill="both")
                scrollbar.config(command=text.yview)

                for intry in entries:
                    try:
                        entry, date, mood, weather = intry.strip().split("~")
                        text.insert(tkinter.END, f"{entry.strip()}\nDate: {date.strip()}\nMood: {mood.strip()}\nWeather: {weather.strip()}\n{"-"*40}\n\n")
                    except ValueError:
                        print("Skipping malformed entry:", intry)
                text.config(state="disabled")

        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found, please try adding some first.")
    
    def filter_by_date():
        """
        This function view the entries within a specific day, entry / entry_date / mood / weather.

        Parameters:
        date (YYYY-MM-DD): the required day date. 
        entry (string): user's journal.
        entry_date(YYYY-MM-DD): the moment the user activates the function.
        mood (string): user's mood or default value 'Unknown'.
        weather (string): user's weather's state or default value 'Unknown'.

        """
        try:
                entries = read_entries()
                
                # Asking for required Date
                user_date = tkinter.simpledialog.askstring("Date filter", "Enter the date to want to check YYYY-MM-DD :")
                if not user_date or not user_date.strip():
                    return
                
                # new window
                top = tkinter.Toplevel(window)
                top.title("Date Filter")
                
                # Add text box
                text = tkinter.Text(top, height=10, width=50)
                text.pack()
                
                found = False
                for entry in entries:
                    journal, journal_date, mood, weather = entry.strip().split("~")

                    if user_date.strip() == journal_date.strip():
                        text.insert(tkinter.END, f"{journal.strip()}\nMood: {mood}\nWeather: {weather}\n{"-"*40}\n")
                        found = True
                
                if not found:
                    text.insert(tkinter.END, "No entries found for that date.")
                text.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found. Try adding some first.")

    def delete_entry():
        """
        This function takes the wanted user entry and deletes it from the entries file.

        Parameters:
        Entry_number(int): The number of the wanted entry.

        Returns:
        Deleting the Entry from the file.

        """
        try:
            entries = read_entries()

            # Adding new window top

            top = tkinter.Toplevel(window)
            top.title("Entries")
            top.resizable()

            # Adding Text Box in top

            text = tkinter.Text(top)
            text.pack(fill="both", expand=True)

            # Showing the number of each entry

            for num, entry in enumerate(entries, start=1):
                journal,journal_date,mood,weather = entry.strip().split("~")
                text.insert(tkinter.END, f"{num}. {journal.strip()}\nDate: {journal_date.strip()}\nMood: {mood.strip()}\nWeather: {weather.strip()}\n{"-"*40}\n")
            text.config(state="disabled")

            # Asking for Entry Number
            label = tkinter.Label(top, text="Enter the number of the entry you would like to delete: ")
            label.pack()
            blog = tkinter.Entry(top)
            blog.pack()

            # Deleting the entry if the number is valid

            def confirm_delete():
                number = blog.get()
                if number.isdigit():
                    number = int(number)
                    if 1 <= number <= len(entries):
                        del entries[number - 1]
                        write_entries(entries)
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
        """
        This function takes the user wanted entry and edits it, entry / date / mood / weather.

        Parameters:
        entry_number (int): the number of the wanted entry.
        entry (string): user's journal.
        date(YYYY-MM-DD): the moment the user activates the function.
        mood (string): user's mood or default value 'Unknown'.
        weather (string): user's weather's state or default value 'Unknown'.

        Returns:
        Edited entry in the file.

        """
        try:
                entries = read_entries()
                
                top = tkinter.Toplevel(window)
                top.title("Edit Entries")
                top.resizable()

                text = tkinter.Text(top)
                text.pack(fill="both", expand=True)

                for num, entry in enumerate(entries, start=1):
                    journal,journal_date,mood,weather = entry.strip().split("~")
                    text.insert(tkinter.END, f"{num}.{journal.strip()}\nDate: {journal_date.strip()}\nMood: {mood.strip()}\nWeather: {weather.strip()}\n{"-"*40}\n")
                text.config(state="disabled")

                #scrollbar =tkinter.Scrollbar(top)
                #scrollbar.pack(side="right", fill="y")

                #text.config(yscrollcommand=scrollbar.set)
                #scrollbar.config(text.yview)

                label = tkinter.Label(top, text="Enter an entry to edit:")
                label.pack(pady= 3)

                entry = tkinter.Entry(top)
                entry.pack(pady=5)

                def confirm_edit(): # this function first put the desired entry in a text box to be edited
                    number = entry.get()
                    if number.isdigit(): # making sure the entry is a number.
                        number = int(number)
                        if 1 <= number <= len(entries):
                            bottom = tkinter.Toplevel(top)
                            bottom.title("Editing blog")

                            sub_text_label = tkinter.Label(bottom, text="journal:")
                            sub_text_label.pack()
                            sub_text = tkinter.Text(bottom, height=10, width=40)
                            sub_text.pack()

                            date_label = tkinter.Label(bottom,text="Date:")
                            date_label.pack()
                            date_entry =tkinter.Entry(bottom)
                            date_entry.pack()

                            mood_label = tkinter.Label(bottom,text= "Mood:")
                            mood_label.pack()
                            mood_entry = tkinter.Entry(bottom)
                            mood_entry.pack()

                            weather_label = tkinter.Label(bottom,text= "Weather:")
                            weather_label.pack()
                            weather_entry = tkinter.Entry(bottom)
                            weather_entry.pack()

                            old_entry = entries.pop(number - 1).strip()
                            old_entry_list = [old_entry]
                            for intry in old_entry_list:
                                journal,journal_date,mood,weather = intry.strip().split("~")
                                sub_text.insert(tkinter.END, journal)
                                date_entry.insert(tkinter.END, journal_date)
                                mood_entry.insert(tkinter.END, mood)
                                weather_entry.insert(tkinter.END, weather)
                            date_entry.config(state="disabled")

                            def sub_save_entry(): #this function grabs the edited parts and save them into the original file.

                                new_entry = sub_text.get("1.0", tkinter.END).strip()
                                new_date = date_entry.get().strip()
                                new_mood = mood_entry.get().strip()
                                new_weather = weather_entry.get().strip()
                                
                                if not new_entry:
                                    messagebox.showwarning("Empty Entry", "Please write something before saving.")
                                elif len(new_mood) <=2:
                                    messagebox.showwarning("Invalid Mood","Please enter a valid mood.")
                                elif len(new_weather) <=2:
                                    messagebox.showwarning("Invalid Weather","Please enter a valid weather.")
                                else:
                                    entries.insert(number - 1, f"{new_entry} ~ {new_date} ~ {new_mood} ~ {new_weather}\n")

                                    write_entries(entries)
                                
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

    def keyword_search():
        """
        This function takes a keyword and gives all the entries that mood/weather has that keyword,  entry / date / mood / weather.

        Parameters:
        keyword (string): the desired word to be searched for.
        entry (string): user's journal.
        date(YYYY-MM-DD): the moment the user activates the function.
        mood (string): user's mood or default value 'Unknown'.
        weather (string): user's weather's state or default value 'Unknown'.

        Returns:
        view all entries with the same keyword.
        """
        try:
                entries = read_entries()

                user_word = tkinter.simpledialog.askstring("Keyword Search", "Enter Keyword:")
                if not user_word or not user_word.strip():
                    return
                user_word = user_word.lower().strip()

                top = tkinter.Toplevel(window)
                top.title("Search Results")
                top.geometry("500x400")

                scrollbar = tkinter.Scrollbar(top)
                scrollbar.pack(side="right", fill="y"),

                text = tkinter.Text(top, height=10, width=50)
                text.pack(expand=True, fill="both")
                scrollbar.config(command=text.yview)

                found = False
                for entry in entries:
                    journal,journal_date,mood,weather = entry.strip().split("~")
                    
                    if user_word in mood.strip().lower() or user_word in weather.strip().lower():
                        text.insert(tkinter.END, f"Entry: {journal.strip()}\nDate: {journal_date.strip()}\nMood: {mood.strip()}\nWeather: {weather.strip()}\n{"-"*40}\n")
                        found = True

                if not found:
                    text.insert(tkinter.END, "No entries found with that mood/weather.")
                text.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "No entries found, try adding some first!")

    def confirm_close(): # function asks the user to confirm exiting, if ok exit.
        if messagebox.askokcancel("Exit", "Are you sure to exit?"):
            window.destroy()
        else:
            return

    # Gui Setup
    window = tkinter.Tk()
    window.title("Journal Tracker")
    window.config(bg="#E6E6E6")
    window.resizable(True,True)
    
    # Required Fonts
    header_font = tkinter.font.Font(family="Helvetica" , size=14, weight="normal")
    medium_font = tkinter.font.Font(family="Helvatica", size=11, weight="bold")
    medium_font_normal = tkinter.font.Font(family="Helvatica", size=12, weight="normal")
    mid_small_font = tkinter.font.Font(family="Helvatica", size=10, weight="bold")
    small_font = tkinter.font.Font(family="Helvatica", size=8)
    
    # Label
    label = tkinter.Label(window, text="Write your journal entry below:", bg="#E6E6E6")
    label.pack(pady=10)
    label.config(font=header_font)

    # Text Box
    text_box = tkinter.Text(window, height=10, width=50,bg="#F5F5F5", font=small_font)
    text_box.pack(fill="x", padx=10, pady=(10,2))

    # Mood slot
    mood_text = tkinter.Label(window,text="Mood:", bg="#E6E6E6")
    mood_text.config(font=medium_font_normal)
    mood_slot = tkinter.Text(window, height=2, bg="#F5F5F5", font=small_font)
    mood_text.pack(pady=(2,0))
    mood_slot.pack(fill="x", pady=(0,2), padx=10)

    # Weather slot
    weather_text = tkinter.Label(window, text="Weather:", bg="#E6E6E6")
    weather_text.config(font=medium_font_normal)
    weather_slot = tkinter.Text(window,height=2, bg="#F5F5F5", font=small_font)
    weather_text.pack(pady=(2,0))
    weather_slot.pack(fill="x",pady=(0,5), padx=10)

    # Save Button     
    save_button = tkinter.Button(window, text="Save Entry",height=1 , width=20, command=save_entry)
    save_button.config(font=medium_font, bg= "#6174d3", relief="groove", bd=2)
    save_button.pack(pady=(5,20))

    # View entries Button
    view_button = tkinter.Button(window, text= "View Entries", height=1 , width=20, command=view_metadata)
    view_button.config(font=medium_font, bg= "#61d376", relief="groove", bd=2)
    view_button.pack(pady=5)

    # Filter by Date Button
    filter_button = tkinter.Button(window, text= "Filter By Date", height=1 , width=20, command=filter_by_date)
    filter_button.config(font=medium_font, bg="#9d9f38", relief="groove", bd=2)
    filter_button.pack(pady= 5)

    # Keyword Search Button
    search_button = tkinter.Button(window, text="Search", height=1, width=20, command=keyword_search)
    search_button.config(font=medium_font, bg= "#e1e342", relief="groove", bd=2)
    search_button.pack(pady=5)

    # Edit Entry Button
    edit_button = tkinter.Button(window, text= "Edit Entry" , height=1 , width=20, command=edit_entry)
    edit_button.config(font=medium_font, bg="#d38244", relief="groove", bd=2)
    edit_button.pack(pady=5)

    # Delete Entry Button
    delete_button = tkinter.Button(window, text="Delete Entry", height=1 , width=20, command=delete_entry)
    delete_button.config(font=medium_font, bg="#d34444", relief="groove", bd=2)
    delete_button.pack(pady=(5,10))
     
    # Close App confirmation
    window.protocol("WM_DELETE_WINDOW", confirm_close)
    
    # Run the app
    window.mainloop()