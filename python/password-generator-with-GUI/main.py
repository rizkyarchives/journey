from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, string=password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Manager", message="The generated password has been copied to your clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"Email/Username": username, "Password": password}}
    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty!")
        return
    confirmation = messagebox.askokcancel(title=website, message=f"Email/Username: {username}\nPassword: {password}\nProceed?")
    if confirmation:
        # Before modifying for day 30
        # with open("data.txt", "a") as file:
        #     file.write(f"{website} | {username} | {password}\n")
        # web_entry.delete(first=0, last=END)
        # password_entry.delete(first=0, last=END)

        # After
        try:
            file = open("data.json", "r")
        except FileNotFoundError:
            file = open("data.json", "w")
            json.dump(new_data, file, indent=4)
        else:
            data = json.load(file)
            data.update(new_data)
            file.close()
            file = open("data.json", "w")
            json.dump(data, file, indent=4)
        finally:
            file.close()
            password_entry.delete(first=0, last=END)
            web_entry.delete(first=0, last=END)

# ---------------------------- Password Search ------------------------------- #
def find_password():
    try:
        file = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="Data Not Found!")
    else:
        data_to_search = json.load(file)
        website_to_search = web_entry.get()
        result = data_to_search.get(website_to_search)
        if result == None:
            messagebox.showwarning(title="Error", message="Data Not Found!")
        else:
            messagebox.showinfo(title=website_to_search, message=f"Email/Username: {result['Email/Username']}\nPassword: {result['Password']}")

            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

logo_canvas = Canvas(width=200, height=190)
logo_image = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 95, image=logo_image)
logo_canvas.grid(row=0, column = 1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

web_entry = Entry() #52
web_entry.grid(row=1, column=1, sticky="EW")
web_entry.focus_set()

username_entry = Entry() #52
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(string="rizkymaulanahadi27@gmail.com", index=0)

password_entry = Entry() #33
password_entry.grid(row=3, column=1, sticky="EW")

pass_button = Button(text="Generate Password", command=generate_pass) #15
pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(width=35, text="Add", command=save_password) #44
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()

# Things to improve that I might do later:
# - Adding a way to edit or show warning when we want to input a login data of a website that we have already inputted previously.
# Currently, if we add two login data with the same website, we would have saved two of that data to the json file.
# So, I could add an option to edit, delete, or add the data anyway so that there are two login info with the same website. Those could be
# done for better functionality. (Not gonna do it immediately. Need to continue the course :D)