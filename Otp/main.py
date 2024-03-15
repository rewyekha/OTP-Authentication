from multiprocessing.sharedctypes import Value
import tkinter
from tkinter import messagebox
import customtkinter

# Set appearance mode and default color theme for customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main application window
app = customtkinter.CTk()

# Set screen width and height
screen_width = 1920
screen_height = 1080

# Set window geometry
app.geometry(f"500x450+{(screen_width//2)-300}+{(screen_height//2)-300}")
app.title("Kamikaze")

# Function for handling login
def login():
    if entry_1.get() == "learningpurpose0316@gmail.com" and entry_2.get() == "3434":
        messagebox.showinfo("Login Successful!")
    else:
        messagebox.showinfo("Error!", "Incorrect email or password")

# Create a frame within the application
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=30, padx=30, fill="both", expand=True)

# Create and pack labels for email and password
label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="E-mail: ")
label_1.pack(pady=10, padx=10)

# Create and pack an entry widget for email
entry_1 = customtkinter.CTkEntry(master=frame_1, width=150, placeholder_text="examples@gmail.com")
entry_1.pack(pady=10, padx=10)

# Create and pack labels for password
label_2 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Password: ")
label_2.pack(pady=10, padx=10)

# Create and pack an entry widget for password
entry_2 = customtkinter.CTkEntry(master=frame_1, width=150, placeholder_text="********", show="*")
entry_2.pack(pady=10, padx=10)

# Create and pack a button for login
button_1 = customtkinter.CTkButton(master=frame_1, command=login, text="Login")
button_1.pack(pady=30, padx=10)

# Create and pack a checkbox for email reminder
checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Remember Email")
checkbox_1.pack(pady=12, padx=10)

# Set the initial value for radiobutton_var
radiobutton_var = tkinter.IntVar(value=1)

# Start the main event loop
app.mainloop()
