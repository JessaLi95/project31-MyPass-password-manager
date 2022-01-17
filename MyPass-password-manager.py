from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password
    ran_letter = [choice(letters) for _ in range(randint(8, 10))]
    ran_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    ran_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = ran_letter + ran_symbol + ran_number
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    generate_button.config(text="Copy password", command=copy_password)
def copy_password():
    global password
    copy(password)
    copied_label.config(text="Copied", fg="#9bdeac")
    copied_label.after(3000, lambda: copied_label.destroy())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username} \n"
                                               f"Password: {password} \nIs this ok to save?")
        if is_ok:
            new_info = f"{website} | {username} | {password}\n"
            with open("my password.txt", mode="a") as file:
                file.write(new_info)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

# Img
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

# Label
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
copied_label = Label(text="")
website_label.grid(column=1, row=2)
username_label.grid(column=1, row=3)
password_label.grid(column=1, row=4)
copied_label.grid(column=2, row=6)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
Add_button = Button(text="Add", width=36, command=save_info)
generate_button.grid(column=3, row=4)
Add_button.grid(column=2, row=5, columnspan=2)

# Entry
website_entry = Entry(width=35)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0, "jessali9595@gmail.com")
password_entry = Entry(width=21)
website_entry.grid(column=2, row=2, columnspan=2)
username_entry.grid(column=2, row=3, columnspan=2)
password_entry.grid(column=2, row=4)

screen.mainloop()
