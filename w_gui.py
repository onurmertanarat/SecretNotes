from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import base64


class Passwords:
    def __init__(self, title, password, key1):
        self.title = title
        self.password = password
        self.key = key1

    def cryption(self):
        password_bytes = self.password.encode("ascii")
        base64_bytes = base64.b64encode(password_bytes)
        base64_str = base64_bytes.decode("ascii")
        with open("my_passwords.txt", "a") as my_passwords:
            my_passwords.write("==="*10 + "\n")
            my_passwords.write(self.title + "\n")
            my_passwords.write(base64_str)


key = str


def crypto():
    if len(inp_title.get()) == 0 or len(inp_password.get()) == 0 or len(inp_master_key.get()) == 0:
        messagebox.showinfo("Info: Check empty place/places", "You can't pass empty place/places!")
    else:
        # Passwords(inp_title.get(), inp_password.get(), inp_master_key.get()).cryption()

        global key
        key = inp_master_key.get()
        title = inp_title.get()
        password_bytes = inp_password.get().encode("ascii")
        base64_bytes = base64.b64encode(password_bytes)
        base64_str = base64_bytes.decode("ascii")

        print(title)
        print(base64_str)
        print(key)

        with open("my_passwords.txt", "a") as my_passwords:
            my_passwords.write("\n" + "===" * 10 + "\n")
            my_passwords.write(title + "\n")
            my_passwords.write(base64_str)

        inp_title.delete(0, END)
        inp_password.delete(0, END)
        inp_master_key.delete(0, END)


def decrypto():
    if inp_master_key.get() == key:
        base64_bytes = inp_password.get().encode("ascii")
        token_bytes = base64.b64decode(base64_bytes)
        token_str = token_bytes.decode("ascii")
        lbl5.config(text=f"Password is: {token_str}")
    else:
        messagebox.showinfo("Error", "Invalid master key!")


frame = Tk()
frame.minsize(width=400, height=600)
frame.title("Encryption Passwords")

img = ImageTk.PhotoImage(Image.open("./key.png"))
lbl_img = Label(frame, image=img)
lbl_img.pack(side="top", padx=20, pady=20)

lbl_title = Label(frame, text="Enter your title")
lbl_title.config(font=('Verdana', 11, 'normal'))
lbl_title.pack(side="top", padx=5, pady=5)

inp_title = Entry(frame)
inp_title.config(font=('Verdana', 11, 'normal'))
inp_title.pack(side="top")

lbl_password = Label(frame, text="Enter your password")
lbl_password.config(font=('Verdana', 11, 'normal'))
lbl_password.pack(side="top", padx=5, pady=5)

inp_password = Entry(frame)
inp_password.config(font=('Verdana', 11, 'normal'))
inp_password.pack(side="top")

lbl_master_key = Label(frame, text="Enter your master key")
lbl_master_key.config(font=('Verdana', 11, 'normal'))
lbl_master_key.pack(side="top", padx=5, pady=5)

inp_master_key = Entry(frame)
inp_master_key.config(font=('Verdana', 11, 'normal'))
inp_master_key.pack(side="top")

btn_encrypt = Button(frame, text="Save and Encrypt Password", command=crypto)
btn_encrypt.config(font=('Verdana', 11, 'bold'))
btn_encrypt.pack(side="top", padx=20, pady=20)

btn_decrypt = Button(frame, text="Decrypt Password", command=decrypto)
btn_decrypt.config(font=('Verdana', 11, 'bold'))
btn_decrypt.pack(side="top")

lbl5 = Label(frame, text="")
lbl5.config(font=('Verdana', 11, 'normal'))
lbl5.config(fg="green")
lbl5.pack(side="top", padx=20, pady=20)

frame.mainloop()
