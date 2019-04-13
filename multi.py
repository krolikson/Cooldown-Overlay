import keyboard
import time

def callback(state):
    print(state)

key = "up" 
key1 = "down"
key2 = "left"
key3 = "right"

upObject = keyboard.add_hotkey(key.upper(), callback, args=(),suppress=True,timeout=1,trigger_on_release=False)
downObject = keyboard.add_hotkey(key.lower(), callback, args=(0,),suppress=True,timeout=1,trigger_on_release=False)

upObject = keyboard.add_hotkey(key1.upper(), callback, args=(),suppress=True,timeout=1,trigger_on_release=False)
downObject = keyboard.add_hotkey(key1.lower(), callback, args=(0,),suppress=True,timeout=1,trigger_on_release=False)

upObject = keyboard.add_hotkey(key2.upper(), callback, args=(),suppress=True,timeout=1,trigger_on_release=False)
downObject = keyboard.add_hotkey(key2.lower(), callback, args=(0,),suppress=True,timeout=1,trigger_on_release=False)

upObject = keyboard.add_hotkey(key3.upper(), callback, args=(),suppress=True,timeout=1,trigger_on_release=False)
downObject = keyboard.add_hotkey(key3.lower(), callback, args=(0,),suppress=True,timeout=1,trigger_on_release=False)

upObject = keyboard.add_hotkey(key3.upper(), callback, args=(1,),suppress=True,timeout=1,trigger_on_release=False)
downObject = keyboard.add_hotkey(key3.lower(), callback, args=(0,),suppress=True,timeout=1,trigger_on_release=False)


time.sleep(2)
keyboard.remove_hotkey(upObject)
keyboard.remove_hotkey(downObject)
