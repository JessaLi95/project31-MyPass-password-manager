import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password
    password = ""
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
    copied_label.grid(column=2, row=6)
    copied_label.config(text="Copied", fg="#9bdeac")
    copied_label.after(1000, lambda: copied_label.grid_forget())
    # copied_label.grid_forget()
    generate_button.config(text="Generate Password", command=generate_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("my_password.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("my_password.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            # Saving updated data
            with open("my_password.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            generate_button.config(text="Generate Password", command=generate_password)


# ---------------------------- Search function ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("my_password.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File does not exist!")
    else:
        if website in data:
            fetched_email = data[website]['email']
            fetched_password = data[website]['password']
            messagebox.showinfo(title=website, message=f"email: {fetched_email}\npassword: {fetched_password}")
        else:
            messagebox.showerror(title="Error", message=f"Detail of {website} does not exist!")


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
# copied_label.grid(column=2, row=6)

# Button
search_button = Button(text="Search", width=13, command=search)
generate_button = Button(text="Generate Password", command=generate_password)
Add_button = Button(text="Add", width=36, command=save_info)
search_button.grid(column=3, row=2)
generate_button.grid(column=3, row=4)
Add_button.grid(column=2, row=5, columnspan=2)

# Entry
website_entry = Entry(width=21)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "jessali9595@gmail.com")
password_entry = Entry(width=21)
website_entry.grid(column=2, row=2)
email_entry.grid(column=2, row=3, columnspan=2)
password_entry.grid(column=2, row=4)

screen.mainloop()
