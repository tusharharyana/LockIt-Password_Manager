from tkinter import *
from tkinter import messagebox



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
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save) 
add_button.grid(row=4, column=1)

window.mainloop()