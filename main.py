from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip #For copy something on clipboard
import pandas as pd

#Password generator
def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '*', '(', ')', '_', '+', '[', ']', '{', '}', '.', '?', '`', '~']


        password_letters = [choice(letters) for _ in range(randint(8,10))]
        password_symbols = [choice(symbols) for _ in range(randint(2,4))]
        password_numbers = [choice(numbers) for _ in range(randint(2,4))]
            
        password_list = password_letters + password_numbers + password_symbols     
        shuffle(password_list)

        password ="".join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(message='Password copied to clipboard')

#Save data to file
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0  or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                           f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            
            new_data = pd.DataFrame({
                'Website': [website],
                'Email': [email],
                'Password':[password]
            })
            try:
                existing_data = pd.read_excel("data.xlsx")
                new_data = pd.concat([existing_data, new_data], ignore_index = True)
            except FileNotFoundError:
                pass
             
            new_data.to_excel("data.xlsx", index = False)
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)

#UI setup

window = Tk()

window.title("LockIt - Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200 , width=300)
logo_img = PhotoImage(file="lockit.png")
canvas.create_image(150, 80, image=logo_img)
# canvas.pack()
canvas.grid(row=0,column=1)

#Labels
# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
# email_entry.insert(0,"tusharharyana@gmail.com")
email_entry.grid(row=2, column=1)
password_entry = Entry(width=35) 
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save) 
add_button.grid(row=4, column=1)

window.mainloop()