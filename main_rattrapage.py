"""
CHARPENAY Arthur CADET Esteban
21/12/20

CS-DEV: SPACE INVADERS
Ce programme respecte les règles de base du jeu 'Space Invader' indiquées dans le sujet.

CONTROLES: 
   JOUEUR: [GAUCHE/DROITE/TIR]: flèche gauche / flèche droite / barre d'espace
   ENNEMI SPECIAL: [HAUT/BAS/GAUCHE/DROITE/TIR]: z / s / q / d / w

MENU: 
   - GAME: Restart(Relance une partie) / Quit(Ferme le jeu)
   - CREDITS: A propos(Affiche les credits)

BUTTONS:
   - Start Game: Démarre un jeu ou redémarre un autre si aucun jeu n'est en cours
   - Quit: Ferme le jeu

RATTRAPAGES:
   Esteban Cadet: Rattrapage du vendredi 18 décembre. Tapez "Rattrapage" pour voir les lignes de code

STRUCTURE PROGRAMME:
   IMPORTS / CLASSE / FONCTIONS / TKINTER

Git: https://github.com/EstebanCdt/Space_Invader.git
Codé en Anglais
"""


# -- IMPORTS --
import random as rd
import tkinter as TK
import winsound  #Sous windows uniquement (Rattrapage)

another = 0      #indicator of a game reloading
start = 0        #start trigger
info = 0         #indicator of shown info



# -- CLASS --
class interact:

    #Sound
    def __init__(self):
        self.sounds = {
            'shot': mixer
        }
    def play(self, name):
        self.sound[name].play()

    #Initialization
    def __init__(self, id, coords):
        self.coords = coords
        self.id = id

    #Create and display instance chosen by [indicator] (str)
    def create(self, indicator):
        if (indicator == "enemy_boss"):
            self.id = C1.create_image(10,10, anchor = NW, image = enemy_boss_ship)
            C1.coords(self.id, self.coords[0], self.coords[1])

        if (indicator == "enemy_solo"):                                                         #(Rattrapage)
            self.id = C1.create_image(10,10, anchor = NW, image = enemy_solo_ship)              #(Rattrapage)
            C1.coords(self.id, self.coords[0], self.coords[1])                                  #(Rattrapage)

        if (indicator == "bullet"):
            self.id = C1.create_image(10, 10, anchor = NW, image = player_shot)
            C1.coords(self.id, self.coords[0], self.coords[1])

        if (indicator == "player"):
            self.id = C1.create_image(10, 10, anchor = NW, image = player_ship)
            C1.coords(self.id, self.coords[0], self.coords[1])

        if (indicator == "enemy"):
            self.id = C1.create_image(10, 10, anchor = NW, image = enemy_ship)
            C1.coords(self.id, self.coords[0], self.coords[1])
        
        if (indicator == "enemy_s"):
            self.id = C1.create_image(10, 10, anchor = NW, image = enemy_s_ship)
            C1.coords(self.id, self.coords[0], self.coords[1])

        if (indicator == "laser"):
            self.id = C1.create_image(10, 10, anchor = NW, image = enemy_shot)
            C1.coords(self.id, self.coords[0], self.coords[1])

        if (indicator == "block"):
            self.id = C1.create_image(10, 10, anchor = NW, image = block)
            C1.coords(self.id, self.coords[0], self.coords[1])

    #Delete input instance
    def delete(self):
        C1.delete(self.id)

    #Refresh instance coords dashing them by inputs x and y (int)
    def refresh(self, x, y):
            self.coords = (self.coords[0] + x, self.coords[1] + y) 
            C1.coords(self.id, self.coords[0], self.coords[1])

    #Set instance to the coords input x and y (int)
    def set(self, x, y):
            self.coords = (x, y)
            C1.coords(self.id, self.coords[0], self.coords[1])



# -- FUNCTIONS --
#Fonction initializing the game, launching the heart
def initialising():

    #If a game isn't on already (Rattrapage)
    global start, results, another, lives, step, boss_step, solo_step, way, fire, bullet_trigger, laser_shot, score, L, info, fire_s
    if ((another == 1) | (start == 0)):

        #Set variables
        fire = 0           #indicator of an ongoing fire
        step = 3           #enemy horizontal dash value
        boss_step = -6     #boss enemy horizontal dash value
        solo_step = -2     #solo enemy horizontal dash value (Rattrapage)
        way = 0            #indicator of a complete round-trip
        bullet_trigger= 0  #indicator of a bullet trigger
        laser_shot = 0     #indicator of a laser on canvas
        start = 1          #start trigger
        fire_s = 0         #special enemy shot trigger

        #Set menu variables
        score = 0         #score
        lives = 3         #number of remaining lives
        l2.configure(text = "Score: "+str(score))
        l3.configure(text = "Lives: "+str(lives))

        #Delete credits if displayed
        if (info == 1):
            info = 0
            C1.delete(results)

        #List of remaining enemies initialisation
        L = []
        for i in range (0, 50):
            L.append(i)

        #If this a game reloading
        if (another == 1):
            
            #Delete previous results
            C1.delete(results)
            another = 0
        
            #Set every element position on canvas
            for i in range (0, 5):
                #Player set
                player.set(0 ,473)
                
                #Enemy set
                for j in range (0,10):
                    eval("enemy_"+str(j+i*10)).set(100+j*50, 50+i*50)
            
            #Boss enemy set
            enemy_boss.set(2000,10)

            #Solo enemy set (Rattrapage)
            enemy_solo.set(1500,70)

            #Special enemy set
            enemy_s.set(30, 30)

            #Bullet set
            bullet.set(-10,10)

            #Laser set
            laser.set(-40, -40)

            #Block set
            for i in range(0,3):
                for k in range(0,3):
                    for j in range(0,5):
                        eval("block"+str(j+k*5+i*15)).set(100+i*230+j*25, 350+k*25)

        #Start the heart
        heart()

#Function that destroys the window to exit
def quit():
    w.destroy()

#Function that displays the credits
def info():

    #If a game isn't on already
    if ((another == 1) | (start == 0)):
        global results, info

        #If this is a reload, delete previous results
        if (start == 1):
            C1.delete(results)
        
        #Show the credits
        results = C1.create_text(390, 460, fill = "Orange", text = "Credits: Charpenay Arthur Cadet Esteban - CPE Lyon", font = ('Arial', '20'))
        info = 1 

#Function that sets the controls over the player and special enemy
def control(event):

    #If the game started
    if (start == 1):
        global fire, fire_s
        touche = event.keysym

        #PLAYER
        #Right dash
        if ((touche == "Right") and (player.coords[0]<730)):
            player.refresh(30, 0)

        #Left dash 
        if ((touche == "Left") and (player.coords[0]>0)):
            player.refresh(-30, 0)

        #Fire
        if touche == "space":
            bullet.set(player.coords[0]+10, player.coords[1]-25)
            fire = 1  #Trigger indicating a shot ongoing
            winsound.PlaySound("laser.wav",winsound.SND_ASYNC)                                #(Rattrapage)

        #SPECIAL
        #Left dash 
        if ((touche == "q") and (enemy_s.coords[0]>0)):
            enemy_s.refresh(-30, 0)
            
        #Right dash 
        if ((touche == "d") and (enemy_s.coords[0]<730)):
            enemy_s.refresh(30, 0)
        
        #Up dash 
        if ((touche == "z") and (enemy_s.coords[1]>0)):
            enemy_s.refresh(0, -30)
        
        #Down dash
        if ((touche == "s") and (enemy_s.coords[1]<400)):
            enemy_s.refresh(0, 30)

        #Fire
        if touche == "w":
            laser_s.set(enemy_s.coords[0]+10, enemy_s.coords[1]+25)
            fire_s = 1  #Trigger indicating a special shot ongoing

#Function processing the whole game at every heartbeat
def heart():
    global step, boss_step, fire, way, another, results, lives, bullet_trigger, laser_shot, score, fire_s

    #For solo enemy (Rattrapage)
    enemy_solo = eval("enemy_solo")
    
    #Refresh boss enemy position (dash)
    enemy_solo.refresh(solo_step, 0)

    #For boss enemy
    enemy_boss = eval("enemy_boss")

    #Right border collision
    if ((int(enemy_boss.coords[0]) > 730) & (int(enemy_boss.coords[0]) < 760)):
        boss_step = -6
    
    #Left border collision
    if ((int(enemy_boss.coords[0] < 10 ) & (int(enemy_boss.coords[0]) > 0))):
        boss_step = 6
    
    #Refresh boss enemy position (dash)
    enemy_boss.refresh(boss_step, 0)

    #For each enemy
    for i in range (0, 50):
        enemy = eval("enemy_"+str(i))

        #Right border collision
        if ((int(enemy.coords[0]) > 730) & (int(enemy.coords[0]) < 760)):
            step = -3
        
        #Left border collision
        if ((int(enemy.coords[0] < 10 ) & (int(enemy.coords[0]) > 0))):
            step = 3
            way = 1   #Indicator of a completed round-trip
        
        #Refresh enemy position (dash)
        enemy.refresh(step, 0) 

    #If a round-trip is made
    if (way == 1):
        way = 0
        for i in range(0, 50):

            #Dash the enemy down
            enemy = eval("enemy_"+str(i))
            enemy.refresh(0, 25)

            #If an enemy reach the bottom, take a life down
            if ((enemy.coords[1] > 473) & (enemy.coords[1] < 550)):
                lives -= 1
                l3.configure(text = "Lives: " + str(lives))
                enemy.set(2000, 2000)
            
    #Player fire ongoing
    if (fire == 1):

            #Refresh bullet position
            bullet.refresh(0, -15)

            #If the bullet reaches the top, delete it
            if(bullet.coords[1] < 10):
                bullet.set(-10,-10)
                fire = 0

            #For each enemy
            for i in range (0, 50):
                enemy = eval("enemy_"+str(i))

                #If the bullet touches the ennemy, delete both
                if ((abs(bullet.coords[0] - enemy.coords[0]) < 30) & ((abs(bullet.coords[1] - enemy.coords[1]) < 30))):
                    enemy.set(2000, 2000)
                    bullet.set(-10, 10)
                    fire = 0
                    L.remove(i)
                    score += 25
                    l2.configure(text = "Score: "+str(score))
                if ((abs(bullet.coords[0] - enemy_s.coords[0]) < 30) & ((abs(bullet.coords[1] - enemy_s.coords[1]) < 30))):
                    enemy_s.set(2000, 2000)
                    bullet.set(-10, 10)
                    score += 500
                    l2.configure(text = "Score: "+str(score))
                if ((abs(bullet.coords[0] - enemy_boss.coords[0]) < 30) & ((abs(bullet.coords[1] - enemy_boss.coords[1]) < 30))):
                    enemy_boss.set(2000,2000)
                    bullet.set(-10,10)
                    score += 300
                    l2.configure(text = "Score: "+str(score))
                if ((abs(bullet.coords[0] - enemy_solo.coords[0]) < 30) & ((abs(bullet.coords[1] - enemy_solo.coords[1]) < 30))): #(Rattrapage)
                    enemy_solo.set(2000,2000)                                                                                     #(Rattrapage)
                    bullet.set(-10,10)                                                                                            #(Rattrapage)
                    score += 500                                                                                                  #(Rattrapage)
                    l2.configure(text = "Score: "+str(score))                                                                     #(Rattrapage)

                #If every enemy is shot down
                if (len(L) == 0):
                    another = 1
                    results = C1.create_text(430, 250, fill = "green", text = "You won\n"+"Score: "+str(score), font = ('Arial', '35'))
                    
                    return
                
            #If the bullet touches a block, delete both
            for i in range(0, 45):
                block = eval("block"+str(i))
                if ((abs(bullet.coords[0] - block.coords[0]) < 30) & ((abs(bullet.coords[1] - block.coords[1]) < 30))):
                    block.set(2000,2000)
                    bullet.set(-10,10)
                    
    #No enemy laser on
    if (laser_shot == 0):
        laser_shot = 1

        #Take a random available enemy
        n = rd.choice(L) 

        #Create the laser at the available enemy
        enemy = eval("enemy_"+str(n))
        laser.set(enemy.coords[0], enemy.coords[1])
    
    #Enemy laser ongoing
    else:
        #Refresh laser position
        laser.refresh(0, 15)
        if (fire_s == 1):
            laser_s.refresh(0, 15)

        #If the laser touches the player, take a life down
        if ((abs(laser.coords[0] - player.coords[0]) < 30) & (abs(laser.coords[1] - player.coords[1]) < 30)):
            lives -= 1
            laser.set(-40, -40)
            l3.configure(text = "Lives: "+str(lives))
            laser_shot = 0
            winsound.PlaySound("hit.wav",winsound.SND_ASYNC)                                                         #(Rattrapage)
        if ((abs(laser_s.coords[0] - player.coords[0]) < 30) & (abs(laser_s.coords[1] - player.coords[1]) < 30)):
            lives -= 1
            laser_s.set(-40, -40)
            l3.configure(text = "Lives: "+str(lives))
            winsound.PlaySound("hit.wav",winsound.SND_ASYNC)                                                         #(Rattrapage)  

        #If the laser reaches the bottom, delete it
        if(laser.coords[1] > 473):
            laser.set(-40, -40)
            laser_shot = 0
        if (laser_s.coords[1] > 473):
            laser_s.set(-40, -40)
            fire_s = 0
        
        #If a laser touches a block, delete both
        for i in range(0,45):
            block = eval("block"+str(i))
            if ((abs(laser.coords[0] - block.coords[0]) < 30) & (abs(laser.coords[1] - block.coords[1]) < 30)):
                block.set(2000, 2000)
                laser.set(-40,-40)
                laser_shot = 0
            if ((abs(laser_s.coords[0] - block.coords[0]) < 30) & (abs(laser_s.coords[1] - block.coords[1]) < 30)):
                block.set(2000, 2000)
                laser_s.set(-40, -40)
                fire_s = 0

    #If no lives remain, show results and stop the heart
    if (lives <= 0):                                                #(Rattrapage correction bug)
        lives = 0                                                   #(Rattrapage correction bug)
        l3.configure(text = "Lives: "+str(lives))                   #(Rattrapage correction bug)
        
        for i in range(0, 50):
            eval("enemy_"+str(i)).set(1000, 1000)
        another = 1  #Indicates a game has been done
        results = C1.create_text(430, 250, fill = "red", text = "You lost\n"+"Score: "+str(score), font = ('Arial', '35'))
        print("checked")
        return

    #Start another heartbeat
    w.after(50, heart)



# -- TKINTER --
from tkinter import *


#WINDOW
w = Tk()
w['bg'] = 'gray23'
w.title('Space Invader')
w.geometry('1100x600')


#MENU
menu = Menu(w, tearoff = 0)

menu1 = Menu(menu, tearoff=0)
menu1.add_command(label = "Restart\n (If previous game ended)", command = initialising)
menu1.add_separator()
menu1.add_command(label = "Quit", command = quit)
menu.add_cascade(label = "Game", menu = menu1)

menu2 = Menu(menu, tearoff=0)
menu2.add_command(label = "A propos", command = info)
menu.add_cascade(label = "Credits", menu = menu2)

w.config(menu = menu)


#FRAMES
f1 = LabelFrame(w, bg ='gray34', text = 'Side Menu')
f1.pack(side = 'right', padx = 20, pady = 20)

f1_1 = LabelFrame(f1, bg = 'gray34')
f1_1.pack(side = 'bottom', padx = 20, pady = 20)

f1_1_1 =LabelFrame(f1_1, borderwidth = 1, relief = 'groove', text = 'Commands', bg = 'gray34')
f1_1_1.pack(side = 'bottom', padx = 20, pady = 20)



#CANVAS
#Create
C1 = Canvas(w, width = 800, height = 500)

#Images
P = PhotoImage(file = "Wallpaper.png")
enemy_boss_ship = PhotoImage(file="enemy_boss_ship.png")
enemy_solo_ship = PhotoImage(file="enemy_solo_ship.png") #(Rattrapage)                    
player_ship = PhotoImage(file="player_ship.png")
enemy_ship = PhotoImage(file="enemy_ship.png")
enemy_s_ship = PhotoImage(file="enemy_s_ship.png")
enemy_shot = PhotoImage(file="enemy_shot.png")
player_shot = PhotoImage(file="player_shot.png")
block = PhotoImage(file="block.png")
C1.create_image(400, 250, image = P)

#Boss set
vars()["enemy_boss"] = interact("enemy_boss", (2000,10))
vars()["enemy_boss"].create("enemy_boss")

#Solo set (Rattrapage)
vars()["enemy_solo"] = interact("enemy_solo", (1500,70))
vars()["enemy_solo"].create("enemy_solo")

#Player set
vars()["player"] = interact("player", (0, 460))
vars()["player"].create("player")

#Bullet set
vars()["bullet"] = interact("bullet", (-10,10))
vars()["bullet"].create("bullet")

#Special enemy set
vars()["enemy_s"] = interact("enemy_s", (30, 30))
vars()["enemy_s"].create("enemy_s")

#Laser set
vars()["laser"] = interact("laser", (-40, 40))
vars()["laser"].create("laser")

#Special laser set
vars()["laser_s"] = interact("laser_s", (-40, 40))
vars()["laser_s"].create("laser")

#Enemy set
for i in range (0, 5):
    for j in range (0,10):
        vars()["enemy_"+str(j+i*10)] = interact("enemy_"+str(j+i*10), (100 + j*50, 50 + i*50))
        vars()["enemy_"+str(i*10+j)].create("enemy")

#Block set
for i in range(0,3):
    for k in range(0,3):
        for j in range(0,5):
            vars()["block"+str(j+k*5+i*15)] = interact("block"+str(j+k*5+i*15), (100+i*230+j*25, 350+ k*25))
            vars()["block"+str(j+k*5+i*15)].create("block")

C1.focus_set()
C1.bind("<Key>", control)
C1.pack(side = 'left', padx = 20, pady = 20)



#Label
l1 = Label(f1, text = "Space Invader", fg = 'white', bg = 'gray34')
l1.pack(side = 'top', padx = 20, pady = 20)
l1.configure(font = ("Comic Sans MS", 18, "bold"), fg = 'white')

l2 = Label(f1_1, text = 'Score: 0', fg = 'white', bg = 'gray34')
l2.pack(side = 'top', padx = 20, pady = 20)
l2.configure(font = ("Arial", 13, "bold"))

l3 = Label(f1_1, text = 'Lives: 3', fg = 'white', bg = 'gray34')
l3.pack(side = 'top', padx = 20, pady = 20)
l3.configure(font = ("Arial", 13, "bold"))


#Button
B1 = Button(f1_1_1, text = "NEW GAME", bg = 'gray52', fg = 'white', pady = 10, padx = 10, activebackground = 'forestgreen', command = initialising)
B1.pack(side = 'top', padx = 30, pady = 20)

B2 = Button(f1_1_1, text = "QUIT", bg = 'gray52', fg = 'white', pady = 10, padx = 10, activebackground = 'firebrick', command = quit)
B2.pack(side = 'bottom', padx = 30, pady = 20)

w.mainloop()