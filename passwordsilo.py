import os
import random
import sys
import colorama
from colorama import Back, Style, Fore
colorama.init(autoreset=True)


sin = Fore.LIGHTBLUE_EX+"""

╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋┏┓
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋┃┃
┏━━┳━━┳━━┳━━┳┓┏┓┏┳━━┳━┳━┛┣━━┳┫┃┏━━┓
┃┏┓┃┏┓┃━━┫━━┫┗┛┗┛┃┏┓┃┏┫┏┓┃━━╋┫┃┃┏┓┃
┃┗┛┃┏┓┣━━┣━━┣┓┏┓┏┫┗┛┃┃┃┗┛┣━━┃┃┗┫┗┛┃
┃┏━┻┛┗┻━━┻━━┛┗┛┗┛┗━━┻┛┗━━┻━━┻┻━┻━━┛
┃┃
┗┛
"""


def choos():
    print(Fore.LIGHTWHITE_EX+"-----------------------------------")
    print(Fore.LIGHTWHITE_EX+"[" + Fore.LIGHTRED_EX + "1" +
          Fore.LIGHTWHITE_EX + "]" + Fore.LIGHTBLUE_EX + " Genereat Easy Password")
    print(Fore.LIGHTWHITE_EX+"[" + Fore.LIGHTRED_EX + "2" +
          Fore.LIGHTWHITE_EX + "]" + Fore.LIGHTBLUE_EX + " Genereat Normal Password")
    print(Fore.LIGHTWHITE_EX+"[" + Fore.LIGHTRED_EX + "3" +
          Fore.LIGHTWHITE_EX + "]" + Fore.LIGHTBLUE_EX + " Genereat Hard Password")
    print(Fore.LIGHTWHITE_EX+"[" + Fore.LIGHTRED_EX + "4" +
          Fore.LIGHTWHITE_EX + "]" + Fore.LIGHTBLUE_EX + " Genereat Complicated Password")
    print(Fore.LIGHTWHITE_EX+"-----------------------------------")
    print("")


characters1 = list("0123456789")
characters2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
characters3 = list(
    "abdcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
characters4 = list(
    "!@#$%^&*()abdcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def generate_easy_password():
    try:
        length = int(input(Fore.LIGHTBLUE_EX + "Enter password length: "))
        random.shuffle(characters1)
        password = []
        for i in range(length):
            password.append(random.choice(characters1))
        random.shuffle(password)
        print(Fore.LIGHTBLUE_EX + "Genereatd password: ")
        print("".join(password))
        var = input(Fore.LIGHTBLUE_EX +
                    "Do you want to generate again 'Yes/No' ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                generate_easy_password()
                print("")
    except ValueError:
        print(Fore.LIGHTRED_EX+"Wrong input !!")


def generate_normal_password():
    try:
        length = int(input(Fore.LIGHTBLUE_EX + "Enter password length: "))
        random.shuffle(characters2)
        password = []
        for i in range(length):
            password.append(random.choice(characters2))
        random.shuffle(password)
        print(Fore.LIGHTBLUE_EX + "Genereatd password: ")
        print("".join(password))
        print("")
        var = input(Fore.LIGHTBLUE_EX +
                    "Do you want to generate again 'Yes/No' ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                generate_normal_password()
                print("")
    except ValueError:
        print(Fore.LIGHTRED_EX+"Wrong input !!")


def generate_hard_password():
    try:
        length = int(input(Fore.LIGHTBLUE_EX + "Enter password length: "))
        random.shuffle(characters3)
        password = []
        for i in range(length):
            password.append(random.choice(characters3))
        random.shuffle(password)
        print(Fore.LIGHTBLUE_EX + "Genereatd password: ")
        print("".join(password))
        print("")
        var = input(Fore.LIGHTBLUE_EX +
                    "Do you want to generate again 'Yes/No' ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                generate_hard_password()
                print("")
    except ValueError:
        print(Fore.LIGHTRED_EX+"Wrong input !!")


def generate_complicated_password():
    try:
        length = int(input(Fore.LIGHTBLUE_EX + "Enter password length: "))
        random.shuffle(characters4)
        password = []
        for i in range(length):
            password.append(random.choice(characters4))
        random.shuffle(password)
        print(Fore.LIGHTBLUE_EX + "Genereatd password: ")
        print("".join(password))
        print("")
        var = input(Fore.LIGHTBLUE_EX +
                    "Do you want to generate again 'Yes/No' ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                generate_complicated_password()
                print("")
    except ValueError:
        print(Fore.LIGHTRED_EX+"Wrong input !!")


print(sin)
choos()
a = input(Fore.LIGHTBLUE_EX + "Coose one of the password options : ")


if a == '1':
    generate_easy_password()

if a == '2':
    generate_normal_password()

if a == '3':
    generate_hard_password()

if a == '4':
    generate_complicated_password()

else:
    print(Fore.LIGHTRED_EX+"Worng input !!")
