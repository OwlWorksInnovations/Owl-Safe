from tkinter import *
from tkinter import ttk
from owlsafe_conosle import generate_random_password, validate_input, save_password
import hashlib
import os

# Global variables
CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+="
PASSWORD_LENGTH = 12
PASSWORD_FILE = "storage/password.txt"
HASH_FILE = "storage/db.txt"

def copy_to_clipboard(password_var):
    text = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(text) 
    root.update()

def hide_label_after_delay(label):
    label.grid_forget()

class OwlSafeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Owl Safe")
        self.root.geometry("800x350")
        
        self.notebook = ttk.Notebook(self.root)

        self.generate = ttk.Frame(self.notebook)
        self.search = ttk.Frame(self.notebook)

        self.notebook.add(self.generate, text="Generate")
        self.notebook.add(self.search, text="Search")
        
        self.notebook.pack(fill='both', expand=True)

        self.name_var = StringVar()
        self.password_var = StringVar()

        ttk.Label(self.generate, text="Name:").grid(column=1, row=1, sticky=W)
        self.name_entry = ttk.Entry(self.generate, textvariable=self.name_var)
        self.name_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.generate, text="Generated Password:").grid(column=1, row=2, sticky=W)
        self.password_label_generate = ttk.Label(self.generate, textvariable=self.password_var)
        self.password_label_generate.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.generate, text="Copy", command=lambda: copy_to_clipboard(self.password_var)).grid(column=2, row=3, sticky=W)
        ttk.Button(self.generate, text="Generate", command=self.generate_and_save).grid(column=2, row=4, sticky=W)

        for child in self.generate.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.name_var_search = StringVar()
        self.password_var_search = StringVar()

        ttk.Label(self.search, text="Name:").grid(column=1, row=1, sticky=W)
        self.name_entry_search = ttk.Entry(self.search, textvariable=self.name_var_search)
        self.name_entry_search.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.search, text="Password:").grid(column=1, row=2, sticky=W)
        self.password_label_search = ttk.Label(self.search, textvariable=self.password_var_search)
        self.password_label_search.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self.search, text="Copy", command=lambda: copy_to_clipboard(self.password_var_search)).grid(column=2, row=3, sticky=W)
        ttk.Button(self.search, text="Search", command=lambda: self.search_identifier_password(self.name_var_search)).grid(column=2, row=4, sticky=W)

        for child in self.search.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def generate_and_save(self):
        if not os.path.exists(PASSWORD_FILE):
            open(PASSWORD_FILE, 'w').close()
        if not os.path.exists(HASH_FILE):
            open(HASH_FILE, 'w').close()

        identifier = validate_input(self.name_var.get())

        with open(PASSWORD_FILE, 'r') as file:
            lines = file.readlines()

        identifier_exists = False
        for line in lines:
            if identifier in line.strip():
                identifier_exists = True
                break

        if identifier_exists:
            self.identifier_label_generate = ttk.Label(self.generate, text="Identifier already exists")
            self.identifier_label_generate.grid(column=1, row=4, sticky=(W, E))
            self.root.after(3000, hide_label_after_delay, self.identifier_label_generate)
        else:
            password = generate_random_password()
            self.password_var.set(password)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            save_password(identifier, password, hashed_password)
            self.password_label_generate = ttk.Label(self.generate, text="Password Generated!")
            self.password_label_generate.grid(column=1, row=4, sticky=(W, E))
            self.root.after(3000, hide_label_after_delay, self.password_label_generate)

    def search_identifier_password(self, identifier):
        identifier = validate_input(self.name_var_search.get())
        with open(PASSWORD_FILE, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if identifier in line:
                    if i + 1 < len(lines):
                        password = lines[i + 1].strip()
                        print(f"The password under the name {identifier} is: {password}")
                        self.password_var_search.set(password)
                        break
            else:
                self.identifier_label_search = ttk.Label(self.search, text="Identifier does not exist")
                self.identifier_label_search.grid(column=1, row=5, sticky=(W, E))
                self.root.after(3000, hide_label_after_delay, self.identifier_label_search)

if __name__ == "__main__":
    root = Tk()
    app = OwlSafeApp(root)
    root.mainloop()
