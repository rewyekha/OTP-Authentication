import tkinter
import customtkinter
import random
from smtplib import SMTP
from tkinter import messagebox

def run():
    # Sending email
    code = str(random.randint(000000, 1000000))
    subject = "Your Verification Code: "
    message = code
    content = "Subject: {0}\n\n{1}".format(subject, message)

    my_email_address = "...@outlook.com"
    password = "pass"
    send_to = "...@outlook.com"

    mail = SMTP("smtp.outlook.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(my_email_address, password)
    mail.sendmail(my_email_address, send_to, content.encode("utf-8"))
    messagebox.showinfo("Successful!", "Verification code sent via email")

    # Verification screen
    customtkinter.set_appearance_mode("white")
    customtkinter.set_default_color_theme("green")
    app = customtkinter.CTk("")
    screen_width = 1920
    screen_height = 1080
    app.geometry(f"300x300+{(screen_width//2)}+{(screen_height//2)-200}")
    app.title("OTP")

    def login():
        if entry.get() == code:
            messagebox.showinfo("Successful!", "Welcome")
            app.destroy()
        else:
            messagebox.showinfo("Error!", "Invalid code")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=40, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Enter the code: ")
    label_1.pack(pady=10, padx=10)

    entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="4CSAQ")
    entry.pack(pady=10, padx=10)

    button_1 = customtkinter.CTkButton(master=frame_1, command=login, text="Login")
    button_1.pack(pady=30, padx=10)

    app.mainloop()

# Run the function
run()
