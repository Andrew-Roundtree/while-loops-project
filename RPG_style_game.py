# andrew Roundtree rpg style world

import random
from tkinter import*
import tkinter.simpledialog
import tkinter. messagebox

#create a window for the game
root = 0
w = Label(root, text="RPG style battle")
w.pack()

#setup
messagebox.showinfo("Salutations recriut.","Hello. i'll try to make this brief. " +
                    "if you want to live, you have to fight, if not, i'll use " +
                    "you as bait so that others in this world will have a higher " +
                    "chance to live, its straight forward. The better your weapon and " +
                    "traight that it scales off of, the more damage you will do. " +
                    "good luck and start training. ")

name = simpledialog.askstring("Heros title","whats your name Recruit?")
hp = 100
equip = 0
strength = random.randint(4,12)
dexterity = random.randint(4,12)




                    
