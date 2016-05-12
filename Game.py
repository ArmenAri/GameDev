#Author: Armen Aristakesyan
from tkinter import *
import winsound
import random
import time
import sys

#Implementing sounds
walk_sound_list = ["sounds/grass1.wav","sounds/grass2.wav","sounds/grass3.wav","sounds/grass4.wav","sounds/grass5.wav","sounds/grass6.wav"]
sound_rand = random.randint(0, 5)
chest_sound = "sounds/chestopen.wav"
wood2_sound = "sounds/wood2.wav"
wood1_sound = "sounds/wood1.wav"
wood5_sound = "sounds/wood5.wav"
wood_break_sound = "sounds/woodbreak.wav"
travel_sound = "sounds/travel.wav"
main_theme = "sounds/maintheme.wav"

#Window Size
width = 1600
height = 900

#Get Window Width
def getWindowWidth():
    global width
    return width

#Get Window Height
def getWindowHeight():
    global height
    return height

WIDTH = 2 * getWindowWidth()//2
HEIGHT = 2 * getWindowHeight()//2

#Scale of blocks
scale = 34

#World
World = []
world_size_x = WIDTH // scale
world_size_y = HEIGHT // scale



#Booleans
gameOver = False
savana_biome = False
forest_biome = False
start = True
solidBlockPresence = False

#Player
player_face = 'player_face'
player_left_side = 'player_left_side'
player_right_side = 'player_right_side'
player_back_side = 'player_back_side'
Player_HP = 20
Player_FOOD = 20
Player_XP = 0
Level = 0
heart_by_level = 0

#Blocks
grass = 'grass'
savana_grass = "savana_grass"
flower = 'flower'

#Chests
wooden_chest = "wooden_chest"
dark_wooden_chest = "dark_wooden_chest"
silver_chest = "silver_chest"
golden_chest = "golden_chest"

#Chest list
wooden_chestList = []
dark_wooden_chestList = []
silver_chestList = []
golden_chestList = []

#Decorations
stone = 'stone'
grave_stone = "grave_stone"
axe_in_the_log = 'axe_in_the_log'
barrel = "barrel"

#SolidBlocks
tree = 'tree'
water = 'water'
savana_tree = "savana_tree"
savana_water = "savana_water"
volcano_sleep = "volcano_sleep"
volcano_awaken = "volcano_awaken"
tower_top = "tower_top"
tower_bottom = "tower_bottom"
forest_dense = "forest_dense"
forest_medium = "forest_medium"

#Solid Block List
solidBlocks = []

#Items
apple = "apple"
axe = "axe"
key = "key"
wood_log = "wood_log"

#Inventory
inventory = [apple, apple, apple, key, wood_log, wood_log, wood_log, wood_log, wood_log]
itemList = []

#Check if the block is solid or not
def isSolidBlock(block, isSolidBlock):
    global solidBlocks
    if isSolidBlock == True:
        solidBlocks = solidBlocks + [block]

#Setting solid status to blocks
isSolidBlock(water, True)
isSolidBlock(tree, True)
isSolidBlock(savana_tree, True)
isSolidBlock(savana_water, True)
isSolidBlock(volcano_sleep, True)
isSolidBlock(volcano_awaken, True)
isSolidBlock(tower_top, True)
isSolidBlock(tower_bottom, True)
isSolidBlock(wooden_chest, True)
isSolidBlock(dark_wooden_chest, True)
isSolidBlock(silver_chest, True)
isSolidBlock(golden_chest, True)
isSolidBlock(stone, True)
isSolidBlock(grave_stone, True)
isSolidBlock(axe_in_the_log, True)
isSolidBlock(barrel, True)

#Add new item with rarity (common, uncommon, rare, epic, legendary)
def addNewItem(item, rarity):
    global itemList
    if rarity == "legendary":
        itemList = itemList + 1*[item]
    elif rarity == "epic":
        itemList = itemList + 3*[item]
    elif rarity == "rare":
        itemList = itemList + 4*[item]
    elif rarity == "uncommon":
        itemList = itemList + 10*[item]
    elif rarity == "common":
        itemList = itemList + 15*[item]

#Addin new items in list of items
addNewItem(key, "rare")
addNewItem(apple, "common")


#Called when the prog. choose a random item
def chooseAnItem():
    global itemList, item
    rand = random.randint(0, (len(itemList)-1))
    item = itemList[rand]
    return item
    
#World MAP Creation
for x in range(world_size_x):
    L1 = []
    for y in range(world_size_y):
            L1 = L1 + [grass]
    World = World + [L1]
           
#Get player positions
def getPlayerPos():
    global player_pos_x, player_pos_y, world_size_x, world_size_y, World, player
    for x in range(world_size_x):
        for y in range(world_size_y):
            if World[x][y] == player_face:
                player_pos_x = x
                player_pos_y = y
            if World[x][y] == player_left_side:
                player_pos_x = x
                player_pos_y = y
            if World[x][y] == player_right_side:
                player_pos_x = x
                player_pos_y = y
            if World[x][y] == player_back_side:
                player_pos_x = x
                player_pos_y = y
                
#Get tower positions
def getTowerPos():
    global tower_pos_x, tower_pos_y, world_size_x, world_size_y, World, player
    for x in range(world_size_x):
        for y in range(world_size_y):
            if World[x][y] == tower_bottom:
                tower_pos_x = x
                tower_pos_y = y
    
#Get chests positions
def getChestsPos():
    global wooden_chest_pos_x, wooden_chest_pos_y, silver_chest_pos_x, silver_chest_pos_y, dark_wooden_chest_pos_x, dark_wooden_chest_pos_y, golden_chest_pos_x, golden_chest_pos_y, world_size_x, world_size_y, World, player
    for x in range(world_size_x):
        for y in range(world_size_y):
            if World[x][y] == wooden_chest:
                wooden_chest_pos_x = x
                wooden_chest_pos_y = y
                
#Get axe positions
def getAxePos():
    global world_size_x, world_size_y, World, player, axe_pos_x, axe_pos_y
    for x in range(world_size_x):
        for y in range(world_size_y):
            if World[x][y] == axe_in_the_log:
                axe_pos_x = x
                axe_pos_y = y
                
#Set player positions
def setPlayerPos(x, y):
    getPlayerPos()
    World[player_pos_x][player_pos_y] = grass
    World[x][y] = player_face
    window_creation()
    LoadGraphics()

#Called when creating random x and y positions
def createRandomPosition(start, end_x, end_y, block):
    pos_x = random.randint(start, end_x)
    pos_y = random.randint(start, end_y)
    while World[pos_x][pos_y] != grass:
        pos_x = random.randint(start, end_x)
        pos_y = random.randint(start, end_y)
    World[pos_x][pos_y] = block

#Called when creating 'number' blocks
def create(min_number, max_number, block):
    global world_size_y
    for i in range(random.randint(min_number, max_number)):
        createRandomPosition(2, world_size_x-2, world_size_y-2, block)
        
#Called when creating 'number' tower blocks
def createTower(min_number, max_number, block):
    for i in range(random.randint(min_number, max_number)):
        createRandomPosition(5, world_size_x-5, world_size_y-5, block)

#Called when creating 'number' axe blocks
def createAxe(min_number, max_number, block):
    for i in range(random.randint(min_number, max_number)):
        createRandomPosition(0, world_size_x-(world_size_x-5), world_size_y-(world_size_y-3), block)
        
#Object Creation
#create(min_number, max_number, object)
create(10, 20, tree)
create(5, 10, water)
create(2, 5, volcano_sleep)
create(1, 1, volcano_awaken)
create(2, 5, stone)
create(1, 3, grave_stone)
create(1, 1, axe_in_the_log)
create(1, 5, barrel)
createTower(1, 1, tower_top)
create(1, 1, wooden_chest)
create(1, 1, player_face)
                                  
#Get Object by positions  
def getObjectByPos(x, y):
    global World
    return World[x][y]

#Graphic Map Creator   
def LoadGraphics():
    global inventory, Window, World, world_size, blockPositions, HEIGHT, WIDTH, Player_HP, Level, heart_by_level, Player_FOOD
    
    #Decorations implementation
    axe_in_the_log_ = PhotoImage(file = "env/blocks/decorations/axe_in_the_log.png")
    barrel_ = PhotoImage(file = "env/blocks/decorations/barrel.png")
    stone_ = PhotoImage(file = "env/blocks/decorations/stone.png")
    grave_stone_ = PhotoImage(file = "env/blocks/decorations/grave_stone.png")

    #Player implementation
    player_face_ = PhotoImage(file = "player/player_face.png")
    player_left_side_ = PhotoImage(file = "player/player_left_side.png")
    player_right_side_ = PhotoImage(file = "player/player_right_side.png")
    player_back_side_ = PhotoImage(file = "player/player_back_side.png")
    
    #Texture implementation
    grass_ = PhotoImage(file = "env/biomes/forest/grass.png")
    water_ = PhotoImage(file = "env/biomes/forest/water.png")
    tree_ = PhotoImage(file = "env/biomes/forest/tree.png")

    #Volcano
    volcano_sleep_ = PhotoImage(file = "env/biomes/forest/volcano_sleep.png")
    volcano_awaken_ = PhotoImage(file = "env/biomes/forest/volcano_awaken.png")

    #Volcano
    tower_top_ = PhotoImage(file = "structures/tower_top.png")
    tower_bottom_ = PhotoImage(file = "structures/tower_bottom.png")

    #Chests textures implementation
    wooden_chest_ = PhotoImage(file = "env/blocks/chests/wooden_chest.png")

    #Hearts textures implementation
    heart = PhotoImage(file = "gui/heart.png")
    empty_heart = PhotoImage(file = "gui/empty_heart.png")
    half_heart = PhotoImage(file = "gui/half_heart.png")

    #Food textures implemantation
    food = PhotoImage(file = "gui/ofood.png")
    empty_food = PhotoImage(file = "gui/empty_food.png")
    half_food = PhotoImage(file = "gui/half_food.png")
    hunger_half_food = PhotoImage(file = "gui/hunger_half_food.png")
    hunger_food = PhotoImage(file = "gui/hunger_food.png")

    #Inv Textures
    inv = PhotoImage(file = "gui/inventory/inv.png")

    #Item Textures
    apple = PhotoImage(file = "items/food/apple.png")
    axe = PhotoImage(file = "items/tools/barbarian_axe.png")
    key = PhotoImage(file = "items/tools/key.png")
    wood_log = PhotoImage(file = "items/nature/wood_log.png")
    
    #Getting player positions x and y
    getPlayerPos()

    #HP GUI
    if Player_HP >= 20 :
        Player_HP = 20
    elif Player_HP <= 0:
        Player_HP = 0
    heart_posY = HEIGHT + 3
    heart_posX_init = 14
    heart_posX_value = 20
    
    for i in range(10):
        canvas.create_image(heart_posX_init+i*heart_posX_value, heart_posY, image = empty_heart)
    if Player_HP % 2 == 1:
        for i in range((Player_HP)//2+1):
            canvas.create_image(heart_posX_init+i*heart_posX_value, heart_posY, image = half_heart)
    for i in range(Player_HP//2):
        canvas.create_image(heart_posX_init+i*heart_posX_value, heart_posY, image = heart)

    #Food GUI  
    food_posY = HEIGHT + 3
    food_posX_init = WIDTH - 190
    food_posX_value = 20
    if Player_FOOD >= 20:
        Player_FOOD = 20
    for i in range(10):
        canvas.create_image(food_posX_init+i*food_posX_value, food_posY, image = empty_food)
    if Player_FOOD % 2 == 1:
        for i in range((Player_FOOD)//2+1):
            canvas.create_image(food_posX_init+i*food_posX_value, food_posY, image = half_food)
    for i in range(Player_FOOD//2):
        canvas.create_image(food_posX_init+i*food_posX_value, food_posY, image = food)
    if Player_FOOD <= 4:
        if Player_FOOD % 2 == 1:
            for i in range((Player_FOOD)//2+1):
                canvas.create_image(food_posX_init+i*food_posX_value, food_posY, image = hunger_half_food)
        for i in range(Player_FOOD//2):
            canvas.create_image(food_posX_init+i*food_posX_value, food_posY, image = hunger_food)

    #Checking all blocks to set graphics         
    for x in range(world_size_x):
        for y in range(world_size_y):
            x0 = (x-1)*scale+37
            y0 = (y-1)*scale+37
            x1 = x0+scale
            y1 = y0+scale
            
            #Creating grass in whole world
            canvas.create_image(x0+17, y0+17, image = grass_)
            
            #Player Graphics
            if World[x][y] == player_face:
                canvas.create_image(x0+17, y0+17, image = player_face_)
            if World[x][y] == player_left_side:
                canvas.create_image(x0+17, y0+17, image = player_left_side_)
            if World[x][y] == player_right_side:
                canvas.create_image(x0+17, y0+17, image = player_right_side_)
            if World[x][y] == player_back_side:
                canvas.create_image(x0+17, y0+17, image = player_back_side_)
                
            #Environment Graphics
            if World[x][y] == savana_grass:
                canvas.create_image(x0+17, y0+17, image = savana_grass_)
            if World[x][y] == water:
                canvas.create_image(x0+17, y0+17, image = water_)
            if World[x][y] == tree:
                canvas.create_image(x0+17, y0+17, image = tree_)
            if World[x][y] == savana_tree:
                canvas.create_image(x0+17, y0+17, image = savana_tree_)
            if World[x][y] == savana_water:
                canvas.create_image(x0+17, y0+17, image = savana_water_)
                
            #Volcano Graphics  
            if World[x][y] == volcano_sleep:
                canvas.create_image(x0+17, y0+17, image = volcano_sleep_)
            if World[x][y] == volcano_awaken:
                canvas.create_image(x0+17, y0+17, image = volcano_awaken_)
                
            #Tower graphics
            if World[x][y] == tower_top:
                canvas.create_image(x0+17, y0+17, image = tower_top_)
            if World[x][y] == tower_bottom:
                canvas.create_image(x0+17, y0+17, image = tower_bottom_)
                
            #Chests graphics
            if World[x][y] == wooden_chest:
                canvas.create_image(x0+17, y0+17, image = wooden_chest_)

            #Decoration graphics
            if World[x][y] == stone:
                canvas.create_image(x0+17, y0+17, image = stone_)
            if World[x][y] == grave_stone:
                canvas.create_image(x0+17, y0+17, image = grave_stone_)
            if World[x][y] == barrel:
                canvas.create_image(x0+17, y0+17, image = barrel_)
            if World[x][y] == axe_in_the_log:
                canvas.create_image(x0+17, y0+17, image = axe_in_the_log_)

    
    info()
    towerCollision()
    chestCollision()
    #INV GUI
    inv_posX_init = WIDTH//2
    inv_posY_init = HEIGHT - 10
    item_posX_init = WIDTH//2 - 215
    item_posX_value = 53
    canvas.create_image(inv_posX_init, inv_posY_init, image = inv)
    for i in range(len(inventory)):
        canvas.create_image(item_posX_init + item_posX_value*i, inv_posY_init, image = eval(inventory[i]))
    axeCollision()
    food_action()
    game_over()
    #Main loop for window
    Window.mainloop()

def inv_rezisement():
    if len(inventory) >= 9:
        rand = random.randint(0, len(inventory)-1)
        inventory.remove(inventory[rand])
    
#Try if in inventory there is the item (item)
def inventoryHasItem(item):
    if item in inventory:
        return True
    
##def motion(event):
##    print("Position de la souris %s %s" %(event.x, event.y))
##
##def leftClick(event):
##    print("leftClick")
##    
##def rightClick(event):
##    print("rightClick")

def keyboard(event):
    global world_size_x, player_pos_x, player_pos_y, World, solidBlocks, solidBlockPresence, Player_HP, Player_FOOD, inventory
    getPlayerPos()
    touche = event.keysym
    sound_rand = random.randint(0, 5)
    winsound.PlaySound(walk_sound_list[sound_rand], winsound.SND_ASYNC)
    #Called when player move up
    if touche == "Up":
        canvas.delete('all')
        World[player_pos_x][player_pos_y] = player_back_side
        for i in solidBlocks:
            if World[player_pos_x][player_pos_y - 1] == i:
                solidBlockPresence = True
                for i in range(len(inventory)):
                        if World[player_pos_x][player_pos_y - 1] == tree and inventory[i] == axe:
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood_break_sound, winsound.SND_ALIAS)
                            World[player_pos_x][player_pos_y - 1] = grass
                            inventory.remove(axe)
                            rand = random.randint(1, 3)
                            inventory = inventory + rand*[wood_log]
                            inv_rezisement()
        if player_pos_y != 0 and solidBlockPresence == False:
            World[player_pos_x][player_pos_y] = grass
            player_pos_y -= 1
            World[player_pos_x][player_pos_y] = player_back_side
        else:
            print("*collision*")
        solidBlockPresence = 0
        LoadGraphics()

    #Called when player move down
    elif touche == "Down":
        canvas.delete('all')
        World[player_pos_x][player_pos_y] = player_face
        for i in solidBlocks:
            if player_pos_y != world_size_y - 1:
                if World[player_pos_x][player_pos_y + 1] == i:
                    solidBlockPresence = True
                    for i in range(len(inventory)):
                        if World[player_pos_x][player_pos_y + 1] == tree and inventory[i] == axe:
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood_break_sound, winsound.SND_ALIAS)
                            World[player_pos_x][player_pos_y + 1] = grass
                            inventory.remove(axe)
                            rand = random.randint(1, 3)
                            inventory = inventory + rand*[wood_log]
                            inv_rezisement()
        if player_pos_y != world_size_y - 1 and solidBlockPresence == False:
            World[player_pos_x][player_pos_y] = grass
            player_pos_y += 1
            World[player_pos_x][player_pos_y] = player_face
        else:
            print("*collision*")
        solidBlockPresence = 0
        LoadGraphics()
        
    #Called when player move right    
    elif touche == "Right":
        canvas.delete('all')
        World[player_pos_x][player_pos_y] = player_right_side
        for i in solidBlocks:
            if player_pos_x != world_size_x - 1: 
                if World[player_pos_x + 1][player_pos_y] == i:
                    solidBlockPresence = True
                    for i in range(len(inventory)):
                        if World[player_pos_x + 1][player_pos_y] == tree and inventory[i] == axe:
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood_break_sound, winsound.SND_ALIAS)
                            World[player_pos_x + 1][player_pos_y] = grass
                            inventory.remove(axe)
                            rand = random.randint(1, 3)
                            inventory = inventory + rand*[wood_log]
                            inv_rezisement()
        if player_pos_x != world_size_x - 1 and solidBlockPresence == False:
            World[player_pos_x][player_pos_y] = grass
            player_pos_x += 1
            World[player_pos_x][player_pos_y] = player_right_side
        else:
            print("*collision*")
        solidBlockPresence = 0
        LoadGraphics()
        
    #Called when player move left
    elif touche == "Left":
        canvas.delete('all')
        World[player_pos_x][player_pos_y] = player_left_side
        for i in solidBlocks:
            if World[player_pos_x - 1][player_pos_y] == i:
                solidBlockPresence = True
                for i in range(len(inventory)):
                        if World[player_pos_x - 1][player_pos_y] == tree and inventory[i] == axe:
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood2_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood1_sound, winsound.SND_ALIAS)
                            winsound.PlaySound(wood_break_sound, winsound.SND_ALIAS)
                            World[player_pos_x - 1][player_pos_y] = grass
                            inventory.remove(axe)
                            rand = random.randint(1, 3)
                            inventory = inventory + rand*[wood_log]
                            inv_rezisement()
        if player_pos_x != 0 and solidBlockPresence == False:
            World[player_pos_x][player_pos_y] = grass
            player_pos_x -= 1
            World[player_pos_x][player_pos_y] = player_left_side
        else:
            print("*collision*")
        solidBlockPresence = 0
        LoadGraphics()

#Callde when player food should decrease    
def food_action():
    global Player_FOOD, Player_HP, inventory
    food_Theory = random.randint(0, 10)
    if food_Theory == 2:
        Player_FOOD -= 1
    if food_Theory > 5 and food_Theory < 10:
        if Player_FOOD <= 4:
            Player_HP -= 1
    if Player_FOOD >= 20 and food_Theory == 4:
        Player_HP += 2
    if Player_FOOD <= 0:
        game_over()
    if Player_FOOD <= 18 and inventoryHasItem("apple") == True:
        Player_FOOD += 2
        inventory.remove("apple")
    
#Called when player game over 
def game_over():
    global HEIGHT, WIDTH
    if Player_HP <= 0 or Player_FOOD <= 0:
        canvas.delete('all')
        canvas.create_text(WIDTH // 2, HEIGHT // 2, fill="black", font="Minecraft 80 bold", text= ('Game Over'))
        canvas.create_text(WIDTH // 2, HEIGHT // 2 + 75, fill="black", font="Minecraft 40 bold", text= ('Try Again'))
        canvas.update()

#Print player positions in game        
def info():
    global canvas
    getPlayerPos()
    canvas.create_text(103, 18, fill="white", font="Minecraft 12 bold", text= ('Player Position : '))
    canvas.create_text(240, 18, fill="white", font="Minecraft 12 bold", text= ('X : %s' % (player_pos_x)))
    canvas.create_text(330, 18, fill="white", font="Minecraft 12 bold", text= ('Y : %s' % (player_pos_y)))
    canvas.update
    
#Getting positions by object name
def getPosByObject(objectIn):
    for x in range(world_size_x):
        for y in range(world_size_y):
            if World[x][y] == objectIn:
                objectIn_pos_x = x
                objectIn_pos_y = y

#Tower around creation
for x in range(world_size_x):
    for y in range(world_size_y):
        if World[x][y] == tower_top:
            World[x][y+1] = tower_bottom
        if World[x][y] == tower_bottom: 
            World[x][y+3] = tree
            World[x+1][y+3] = tree
            World[x-1][y+3] = tree
            World[x+2][y+2] = tree
            World[x+3][y] = tree
            World[x+3][y] = tree
            World[x+3][y-1] = tree
            World[x+2][y-2] = tree
            World[x+1][y-3] = tree
            World[x][y-3] = tree
            World[x-1][y-3] = tree
            World[x-3][y] = tree
            World[x-3][y-1] = tree
            World[x-3][y+1] = tree
            World[x+3][y+1] = tree
            World[x-2][y+2] = tree
            World[x-2][y-2] = tree
            

#Called when player is in front of tower
def towerCollision():
    global World, inventory, key
    #Getting player positions x and y
    getPlayerPos()
    #Getting tower positions x and y
    getTowerPos()
    if World[player_pos_x][player_pos_y] == World[tower_pos_x][tower_pos_y + 1] and World[player_pos_x][player_pos_y] == player_back_side:
        for i in range(len(inventory)):
            if inventory[i] == key:
                inventory.remove(key)
                canvas.delete('all')
                canvas.create_text(WIDTH // 2, HEIGHT // 2, fill="black", font="Minecraft 80 bold", text= ('You Win'))
                winsound.PlaySound(travel_sound, winsound.SND_ASYNC)

#Called when player collided with an axe
def axeCollision():
    global World, inventory, axe
    getPlayerPos()
    getAxePos()
    if World[player_pos_x][player_pos_y] == World[axe_pos_x][axe_pos_y + 1] and World[player_pos_x][player_pos_y] == player_back_side or World[player_pos_x][player_pos_y] == World[axe_pos_x][axe_pos_y - 1] and World[player_pos_x][player_pos_y] == player_face or World[player_pos_x][player_pos_y] == World[axe_pos_x + 1][axe_pos_y] and World[player_pos_x][player_pos_y] == player_left_side or World[player_pos_x][player_pos_y] == World[axe_pos_x - 1][axe_pos_y] and World[player_pos_x][player_pos_y] == player_right_side:
        if World[player_pos_x][player_pos_y] == player_back_side:
            World[player_pos_x][player_pos_y - 1] = grass
        elif World[player_pos_x][player_pos_y] == player_left_side:
            World[player_pos_x - 1][player_pos_y] = grass
        elif World[player_pos_x][player_pos_y] == player_right_side:
            World[player_pos_x + 1][player_pos_y] = grass
        elif World[player_pos_x][player_pos_y] == player_face:
            World[player_pos_x][player_pos_y + 1] = grass
        create(1, 1, axe_in_the_log)
        inventory = inventory + [axe]
        inv_rezisement()
        winsound.PlaySound(wood1_sound, winsound.SND_ASYNC)

#Called when player collided with a chest 
def chestCollision():
    global World, itemList, inventory
    #Getting player positions x and y
    getPlayerPos()
    #Getting tower positions x and y
    getChestsPos()
    if World[player_pos_x][player_pos_y] == World[wooden_chest_pos_x][wooden_chest_pos_y + 1] and World[player_pos_x][player_pos_y] == player_back_side or World[player_pos_x][player_pos_y] == World[wooden_chest_pos_x][wooden_chest_pos_y - 1] and World[player_pos_x][player_pos_y] == player_face or World[player_pos_x][player_pos_y] == World[wooden_chest_pos_x + 1][wooden_chest_pos_y] and World[player_pos_x][player_pos_y] == player_left_side or World[player_pos_x][player_pos_y] == World[wooden_chest_pos_x - 1][wooden_chest_pos_y] and World[player_pos_x][player_pos_y] == player_right_side:
        print("*chest*")
        if World[player_pos_x][player_pos_y] == player_back_side:
            World[player_pos_x][player_pos_y - 1] = grass
        elif World[player_pos_x][player_pos_y] == player_left_side:
            World[player_pos_x - 1][player_pos_y] = grass
        elif World[player_pos_x][player_pos_y] == player_right_side:
            World[player_pos_x + 1][player_pos_y] = grass
        elif World[player_pos_x][player_pos_y] == player_face:
            World[player_pos_x][player_pos_y + 1] = grass
        item = itemList[(random.randint(0, len(itemList)-1))]
        winsound.PlaySound(chest_sound, winsound.SND_ASYNC)
        inventory = inventory + [item]
        itemList.remove(item)
        create(1, 1, wooden_chest)
        inv_rezisement()

#Called when is close requested
def close_window(): 
    Window.destroy()
    
#Window creation    
def window_creation():
    global canvas, Window, HEIGHT, WIDTH, main_theme
    sys.setrecursionlimit(1*10**9)
    winsound.PlaySound(main_theme, winsound.SND_ASYNC)
    Window = Tk()
    Window.title("RPG")
    canvas = Canvas(Window, width = WIDTH, height = HEIGHT + 25)
    Window.resizable(width = False, height = False)
    canvas.focus_set()
    canvas.bind("<Key>", keyboard)
##    canvas.bind("<Motion>", motion)
##    canvas.bind("<Button-1>", leftClick)
##    canvas.bind("<Button-3>", rightClick)
    canvas.pack()
    LoadGraphics()

#Main Loop  
window_creation()
