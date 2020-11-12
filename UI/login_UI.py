import tkinter as tk
from networking.client import send_message
import json

VERIFICATION_MESSAGE = "!VERIFY"

WIDTH = 640
HEIGHT = 480

tk_login = tk.Tk()
tk_login.geometry(f"{WIDTH}x{HEIGHT}")

# TODO fix the overall horrible layout
# TODO reconfigure so that the position is static in the top left corner
# create the greeting and login labels
frm_greet = tk.Frame(master=tk_login)

lbl_greeting = tk.Label(master=frm_greet, text="Hello!")
lbl_login = tk.Label(master=frm_greet, text="Please login: ")

frm_greet.rowconfigure([0, 1], minsize=150)
frm_greet.columnconfigure(0, minsize=50)

lbl_greeting.grid(row=0, sticky=tk.W)
lbl_login.grid(row=1, sticky=tk.W)

frm_greet.grid(row=0)

# create entries so as to let passwords and usernames to be typed in

frm_login = tk.Frame(master=tk_login)

lbl_username = tk.Label(master=frm_login, text="Username:")
ent_username = tk.Entry(master=frm_login)

lbl_password = tk.Label(master=frm_login, text="Password:")
ent_password = tk.Entry(master=frm_login)

lbl_username.grid(row=0, column=0)
ent_username.grid(row=0, column=1)

lbl_password.grid(row=1, column=0)
ent_password.grid(row=1, column=1)

frm_login.grid(row=1)

# submit button and function

def submit_info():
    info = (ent_username.get(0, tk.END), ent_password.get(0, tk.END))

    # TODO check the database if this exists by sending a message to the server
    # TODO make a verification message sender method

btn_submit = tk.Button()

tk_login.mainloop()