import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Bank_GUI")

# List of login

Login = {"Nosent": "Nosent678",
         "Filip": "Filip102$",
         "Icaca": "Icacas67",
         "Adik": "Niggets",
         "Adrian": "Zawisze"}

Code = {"Nosent": "58349",
        "Filip": "738660",
        "Icaca": "396850",
        "Adrian": "485920"}

Balance = {"Nosent": 1000,
           "Filip": 1267,
           "Icaca": 7910,
           "Adik": 3019,
           "Adrian": 1082}



# Check

def check_login():
    user = Login_Usernamentry.get()
    pwd = Login_Passwordentry.get()
    code = Login_Codentry.get()

    if user in Login:
        print("Username Correct")
        if Login[user] == pwd:
            print("Password Correct")
            if Code[user] == code:
                print("Code correct")
                Login_frame.pack_forget()
                Menu_frame.pack(fill='both', expand=True)
                Menu_Hello.config(text=f"Hello {user}")
                Menu_Balance.config(text=f"Your balance is {Balance[user]}$")
            else:
                print("Wrong Code")
                Login_page.config(text="Wrong code", fg='red')
        else:
            Login_page.config(text="Wrong Username, Password or Code", fg='red')
    else:
        print("The account does not exist")
        Login_page.config(text="The account doesn't exist", fg='orange')


# Register function

def register():
    user = Register_Usernamentry.get()
    pwd = Register_Passwordentry.get()
    code = Register_CreateCodeEntry.get()

    if user in Login:
        print("Account already exist!")
        Register_page.config(text="Account already exist!", fg='red')
    else:
        Login[user] = pwd
        Code[user] = code
        Balance[user] = 0

        Register_page.config(text="Account Created", fg='green')
        
        print(Login)
        print(Code)
        print(Balance)

# Open Function

def open_login():
    Choose_frame.pack_forget()
    Login_frame.pack(fill='both', expand=True)

def open_register():
    Choose_frame.pack_forget()
    Register_frame.pack(fill='both', expand=True)

def open_admin():
    Choose_frame.pack_forget()
    Admin_frame.pack(fill='both', expand=True)

def open_deposit():
    Menu_frame.pack_forget()
    Deposit_frame.pack(fill='both', expand=True)

def open_withdraw():
    Menu_frame.pack_forget()
    Withdraw_frame.pack(fill='both', expand=True)

# Back to Menu Function

def back_login():
    Login_frame.pack_forget()
    Choose_frame.pack(fill='both', expand=True)

def back_register():
    Register_frame.pack_forget()
    Choose_frame.pack(fill='both', expand=True)

def back_admin():
    Admin_frame.pack_forget()
    Choose_frame.pack(fill='both', expand=True)

# Logout function

def logout():
    Menu_frame.pack_forget()
    Choose_frame.pack(fill='both', expand=True)

def back_deposit():
    Deposit_frame.pack_forget()
    Menu_frame.pack(fill='both', expand=True)

def back_withdraw():
    Withdraw_frame.pack_forget()
    Menu_frame.pack(fill='both', expand=True)

# Deposit function

def Deposit():
    user = Login_Usernamentry.get()
    Bal = Balance[user]
    Dep = Deposit_Entry.get()

    Dep = int(Deposit_Entry.get())

    if Dep <= 0:
        Deposit_page.config(text="Enter the a positive number", fg='red')
    else:
        Bal += Dep
        Deposit_frame.pack_forget()
        Menu_frame.pack(fill='both', expand=True)
        Menu_Balance.config(text=f"Deposited {Dep}$ You have: {Bal}")
    

# Withdraw function

def Withdraw():
    user = Login_Usernamentry.get()
    Bal = Balance[user]
    Wit = Withdraw_Entry.get()

    Wit = int(Withdraw_Entry.get())

    if Wit > Bal:
        Deposit_page.config(text=f"Enter the a number under {Bal}", fg='red')
    else:
        Bal -= Wit
        Withdraw_frame.pack_forget()
        Menu_frame.pack(fill='both', expand=True)
        Menu_Balance.config(text=f"Withdrawed {Wit}$ You have: {Bal}$", fg='green')

# Choose page
Choose_frame = tk.Frame(root)

Choose_page = tk.Label(Choose_frame, text="Choose a option", font=('Arial', 18))
Choose_page.pack(pady=10)

Choose_option1 = tk.Button(Choose_frame, text="Login", font=('Arial', 16), command=open_login)
Choose_option1.pack(pady=10)

Choose_option2 = tk.Button(Choose_frame, text="Register", font=('Arial', 16), command=open_register)
Choose_option2.pack(pady=10)

Choose_option3 = tk.Button(Choose_frame, text="Admin Mode Coming Soon", font=('Arial', 16), fg='red', command=open_admin)
Choose_option3.pack(pady=10)

Note_Label = tk.Label(Choose_frame, text="Note: More updates coming soon", font=('Arial', 14))
Note_Label.pack(pady=45)
Version_Label = tk.Label(Choose_frame, text="Version: 1.0v", font=('Arial'))
Version_Label.pack(pady=50)

# Login page
Login_frame = tk.Frame(root)

Login_page = tk.Label(Login_frame, text="Login", font=('Arial', 18))
Login_page.pack(pady=10)

Login_Username = tk.Label(Login_frame, text="Username", font=('Arial', 16))
Login_Username.pack(pady=10)

Login_Usernamentry = tk.Entry(Login_frame)
Login_Usernamentry.pack()

Login_Password = tk.Label(Login_frame, text="Password", font=('Arial', 16))
Login_Password.pack(pady=10)

Login_Passwordentry = tk.Entry(Login_frame, show=("*"))
Login_Passwordentry.pack()

Login_Code = tk.Label(Login_frame, text="Code", font=('Arial', 16))
Login_Code.pack(pady=10)

Login_Codentry = tk.Entry(Login_frame)
Login_Codentry.pack()

Login_Button = tk.Button(Login_frame, text="Login", font=('Arial', 16), command=check_login)
Login_Button.pack(pady=10)

Login_codefind = tk.Label(Login_frame, text="You can find the code in files", font=('Arial', 18), fg='green')
Login_codefind.pack(pady=5)

Login_BackChoosePage = tk.Button(Login_frame, text="Back", font=('Arial', 16), command=back_login)
Login_BackChoosePage.pack(pady=10)

# Register Page
Register_frame = tk.Frame(root)

Register_page = tk.Label(Register_frame, text="Register", font=('Arial', 18))
Register_page.pack(pady=10)

Register_Username = tk.Label(Register_frame, text="Username", font=('Arial', 16))
Register_Username.pack(pady=10)

Register_Usernamentry = tk.Entry(Register_frame)
Register_Usernamentry.pack()

Register_Password = tk.Label(Register_frame, text="Password", font=('Arial', 16))
Register_Password.pack(pady=10)

Register_Passwordentry = tk.Entry(Register_frame)
Register_Passwordentry.pack()

Register_CreateCode = tk.Label(Register_frame, text="Create a code", font=('Arial', 16))
Register_CreateCode.pack(pady=10)

Register_CreateCodeEntry = tk.Entry(Register_frame)
Register_CreateCodeEntry.pack()

Register_Codetell = tk.Label(Register_frame, text="You need to create a code then it will save on files", font=('Arial', 16), fg='green')
Register_Codetell.pack()

Register_Button = tk.Button(Register_frame, text="Register", font=('Arial', 16), command=register)
Register_Button.pack(pady=10)

Register_BackToMenu = tk.Button(Register_frame, text="Back", font=('Arial', 16), command=back_register)
Register_BackToMenu.pack()

# Admin Page
Admin_frame = tk.Frame(root)

Admin_page = tk.Label(Admin_frame, text="Admin Mode", font=('Arial', 18), fg='red')
Admin_page.pack(pady=10)

Admin_Code1 = tk.Label(Admin_frame, text="Enter Code 1", font=('Arial', 18))
Admin_Code1.pack(pady=10)

Admin_Code1Entry = tk.Entry(Admin_frame)
Admin_Code1Entry.pack()

Admin_Code2 = tk.Label(Admin_frame, text="Enter Code 2", font=('Arial', 18))
Admin_Code2.pack(pady=10)

Admin_Code2Entry = tk.Entry(Admin_frame)
Admin_Code2Entry.pack()

Admin_Code3 = tk.Label(Admin_frame, text="Enter Code 3", font=('Arial', 18))
Admin_Code3.pack(pady=10)

Admin_Code3Entry = tk.Entry(Admin_frame)
Admin_Code3Entry.pack()

Admin_Enter = tk.Button(Admin_frame, text="Enter", font=('Arial', 18))
Admin_Enter.pack(pady=10)

Admin_BackMenu = tk.Button(Admin_frame, text="Back", font=('Arial', 18), command=back_admin)
Admin_BackMenu.pack(pady=10)

# Menu page
Menu_frame = tk.Frame(root)

Menu_Hello = tk.Label(Menu_frame, text="", font=('Arial', 18))
Menu_Hello.pack()

Menu_Balance = tk.Label(Menu_frame, text="", font=('Arial', 12))
Menu_Balance.pack()

Menu_Deposit = tk.Button(Menu_frame, text="Deposit", font=('Arial', 16), command=open_deposit)
Menu_Deposit.pack(pady=10)

Menu_Withdraw = tk.Button(Menu_frame, text="Withdraw", font=('Arial', 16), command=open_withdraw)
Menu_Withdraw.pack(pady=10)

Menu_Logout = tk.Button(Menu_frame, text="Logout", font=('Arial', 16), command=logout)
Menu_Logout.pack(pady=10)

# Deposit page
Deposit_frame = tk.Frame(root)

Deposit_page = tk.Label(Deposit_frame, text="Deposit", font=('Arial', 18))
Deposit_page.pack()

Deposit_Question = tk.Label(Deposit_frame, text='How much do you want to deposit?', font=('Arial', 16))
Deposit_Question.pack(pady=10)

Deposit_Entry = tk.Entry(Deposit_frame)
Deposit_Entry.pack()

Deposit_Enter = tk.Button(Deposit_frame, text="Enter", font=('Arial', 16), command=Deposit)
Deposit_Enter.pack(pady=10)

Deposit_Back = tk.Button(Deposit_frame, text="Back", font=('Arial', 16), command=back_deposit)
Deposit_Back.pack(pady=10)

# Withdraw page
Withdraw_frame = tk.Frame(root)

Withdraw_page = tk.Label(Withdraw_frame, text="Withdraw", font=('Arial', 18))
Withdraw_page.pack()

Withdraw_Question = tk.Label(Withdraw_frame, text="How much do you want to withdraw?", font=('Arial', 16))
Withdraw_Question.pack(pady=10)

Withdraw_Entry = tk.Entry(Withdraw_frame)
Withdraw_Entry.pack()

Withdraw_Enter = tk.Button(Withdraw_frame, text="Enter", font=('Arial', 16), command=Withdraw)
Withdraw_Enter.pack(pady=10)

Withdraw_Back = tk.Button(Withdraw_frame, text="Back", font=('Arial', 16), command=back_withdraw)
Withdraw_Back.pack(pady=10)

# Show Choose page first
Choose_frame.pack(fill='both', expand=True)

root.mainloop()
