from fileinput import close
from multiprocessing.resource_sharer import stop
from secondary import * 
import keyboard

while True:
    generate()
    input('Press ENTER to generate a new password, or ESC to close the program.')
    
    if keyboard.is_pressed('escape'):
        exit()