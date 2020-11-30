import requests, colorama, threading, os

from colorama import Fore,init
from threading import Thread

init()
try:
    os.mkdir('Assets')
    os.mkdir('Assets/Skins')
except:
    pass

def get_images():
    response=requests.get(
        'https://benbotfn.tk/api/v1/cosmetics/br?lang=en'
    ).json()
    for image in response:
        if image['icons']['icon'] != None:
            print(image['icons']['icon'])
            image_content = requests.get(image['icons']['icon'])
            with open(f'Assets/Skins/{image["id"]}.png', 'wb') as image_save:
                image_save.write(image_content.content)

def start_up():
    print(f'''{Fore.BLUE}
___________            __         .__  __           _________                              __  .__               
\_   _____/___________/  |_  ____ |__|/  |_  ____   \_   ___ \  ____  ______ _____   _____/  |_|__| ____   ______
 |    __)/  _ \_  __ \   __\/    \|  \   __\/ __ \  /    \  \/ /  _ \/  ___//     \_/ __ \   __\  |/ ___\ /  ___/
 |     \(  <_> )  | \/|  | |   |  \  ||  | \  ___/  \     \___(  <_> )___ \|  Y Y  \  ___/|  | |  \  \___ \___ \ 
 \___  / \____/|__|   |__| |___|  /__||__|  \___  >  \______  /\____/____  >__|_|  /\___  >__| |__|\___  >____  >
     \/                         \/              \/          \/           \/      \/     \/             \/     \/                                                                                                                                                                                                                                                                     
    {Fore.RESET}
    [{Fore.CYAN}1{Fore.RESET}] Download Assets''')
    i = int(input())
    if i == 1:
        threadnum = int(input("[0-500] Threads: "))
        os.system('cls')
        c = 0
        while c < threadnum:
            processThread = Thread(target=get_images)
            processThread.start()
            c += 1


start_up()
