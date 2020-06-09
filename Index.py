# Importa as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

# Criar nossa janela
jan = Tk()
jan.title("ABC Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#Carregar Imagens
logo= PhotoImage(file="icons/logo3remove.png")

#Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=10, y=80)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=31)
UserEntry.place(x=150, y=112)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=31, show="*")
PassEntry.place(x=150, y=162)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBase.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado. Bem vindo!!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso negado. Verifique se está cadastrado no sistema")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=40)
    NomeEntry.place(x=100, y=16.5)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width = 40)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="RegisterError", message="Não deixe nenhum campo vazio")
        else:
            DataBase.cursor.execute("""
            INSERT INTO Users (Name, Email, User, Password) VALUES (?,?,?,?)
            """, (Name, Email, User, Pass))
            DataBase.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    Register.place(x=125, y=225)

    def BackToLogin():
        #Removendo Widgets de Cadastro
        NomeEntry.place(x=5000)
        NomeLabel.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo novamente os Widgets de Cadastro
        LoginButton.place(x=100)
        RegisterButton.place(x=130)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=265)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=130, y=260)

jan.mainloop()