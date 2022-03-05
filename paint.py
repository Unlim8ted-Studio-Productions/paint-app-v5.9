from os import write
from tkinter import W
import pygame as pig
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_i, K_s,RESIZABLE
import subprocess
from pygame import gfxdraw
from pygame.draw import rect
from pygame.gfxdraw import filled_circle as circle
#import downloader.downloader as info
#p_t_1 = "C:\ "
#os.listdir()

info = open("info.TXT","r")
p_a_p = info.readline(64)
s_i_p = info.readline(2)
d_p = info.readline(3)

pig.init()
  
print("r = red,o = orange,y = yellow,g = green,b = blue,p = purple,p + i = pink,t + u = turquoise,s + b = sky blue,l = lime,z = screen black,x = screen white,m = magenta,d + b = dark blue,s + c = skin color,e = black,w + h = white,s + f1 = save slot1,s + f2 = save") 
print('slot2,s + f3 = save slot3,s + f4 = save slot4,s + f5 = save slot5,s + f6 = save slot6,s + f7 = save slot7,s + f8 = save slot8,s + f9 = save slot9,s + end = save slot0, l + 0 = load image 0,hold equale key = rainbow')
print('c + i = circle mode, s + q = square mode, c + h = christmas mode, n + c = not christmas mode, while hold equale key rainbow mode = True, if speed 9 pattern apears,shift + 8 = pattern appears while moving diagnale')


  
icon = pig.image.load(p_a_p + r'paint app gus v5\icon.ico')
win_size = (1920,1025)
win = pig.display.set_mode(win_size,RESIZABLE)
pig.display.set_caption("paint")
pig.display.set_icon(icon)  
# object current co-ordinates 
x = 200
y = 200
a = 207 
b = 207

color = (255,255,255)



# dimensions of the object 
rainbow_mode = False
width = 20
height = 20
width1 = 5
height1 = 5  
width_hight = 5
width_hight1 = 3

# maocity / speed of movement
ma = 1
christmas = False
        

for event in pig.event.get() :
    print('Loading')
    
       
run = True
print('hi Gus')  
# infinite loop 
circle_mode = False
num = 0
while run:
    pig.time.delay(10)
      
    
    for event in pig.event.get():
          
          
        if event.type == pig.QUIT:
              
            
            run = False
    
    keys = pig.key.get_pressed()
      
    #if mouse.get_pressed:
        #x = mouse.get_pos()
        #y = mouse.get_pos()
    
    #if MOUSEBUTTONUP:   
    if keys[pig.K_LEFT] or keys[pig.K_a] and rainbow_mode == False and x>0:
        x -= ma
        a -= ma
        
    
    if keys[pig.K_RIGHT] or keys[pig.K_d]and rainbow_mode == False and x<1920-width:
        x += ma
        a += ma
         
        
    if keys[pig.K_UP] or keys[pig.K_w]and rainbow_mode == False and y>0:
        y -= ma
        b -= ma  
    
    if keys[pig.K_DOWN] or keys[pig.K_s]and rainbow_mode == False and y<1025-height:
        y += ma
        b += ma
   
    
    path = f'{s_i_p}{num + 1}'
    pig.display.update()        
    
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)  
    orange = (255,165,0)
    yellow = (255,255,25)   
    green = (0,128,0)
    blue = (0,0,255)
    purple = (128,0,128)
    pink = (255,20,147)
    turquoise = (64,224,208)
    sky_blue = (0,191,255)
    magenta = (139,0,139)
    dark_blue = (0,0,139)
    skin_color = (250,231,218)
    color1 = (255,255,255)
    lime = (0,255,0)


    #FIXME better rainbow
    
    if keys[pig.K_EQUALS]:
        rainbow_mode = True
    
    if rainbow_mode == True:
        if keys[pig.K_LEFT] or keys[pig.K_a]and x>0:
            x -= ma
            a -= ma
            color = red
          
        if keys[pig.K_RIGHT] or keys[pig.K_d]and x<1920-width:
            x += ma
            a += ma
            color = yellow
         
        if keys[pig.K_UP] or keys[pig.K_w]and y>0:
            y -= ma
            b -= ma  
            color = green
      
        if keys[pig.K_DOWN] or keys[pig.K_s] and y<1025-height:
            y += ma
            b += ma
            color = blue
        
        if keys[pig.K_EQUALS]:
            rainbow_mode = False
          
            
    
    if keys[pig.K_r]:
        color = red
        rainbow_mode = False

    if keys[pig.K_o]:
        color = orange
        rainbow_mode = False

    if keys[pig.K_w] and keys[pig.K_h]:
        color = white
        rainbow_mode = False

    if keys[pig.K_y]:
        color = yellow
        rainbow_mode = False

    if keys[pig.K_g]:
        color = green
        rainbow_mode = False

    if keys[pig.K_b]:
        color = blue
        rainbow_mode = False	
    
    if keys[pig.K_p]:
       color = purple 
       rainbow_mode = False	

    if keys[pig.K_p] and keys[pig.K_i]:
        rainbow_mode = False
        color = pink

    if color == white and christmas == False:
        color1 = black
    
    if color == black and christmas == False:
        color1 = white
   
    if keys[pig.K_1]:
        width = 2
        height = 20
        width1 = 5
        height1 = 5
        width_hight = 5
        width_hight1 = 3

    if keys[pig.K_2]:
        width = 25
        height = 25
        width1 = 10
        height1 = 10
        width_hight = 10
        width_hight1 = 5

    if keys[pig.K_3]:
        width = 10
        height = 30
        width1 = 15
        height1 = 15
        width_hight = 15
        width_hight1 = 10

    if keys[pig.K_4]:
        width = 35
        height = 35
        width1 = 20
        height1 = 20
        width_hight = 20
        width_hight1 = 15

    if keys[pig.K_5]:
        width = 40
        height = 40
        width1 = 25
        height1 = 25
        width_hight = 25
        width_hight1 = 20

    if keys[pig.K_6]:
        width = 45
        height = 45
        width1 = 30
        height1 = 30
        width_hight = 30
        width_hight1 = 25

    if keys[pig.K_7]:
        ma = 2

    if keys[pig.K_8]:
        ma = 3
    
    if keys[pig.K_9]:
        ma = 3

    if keys[pig.K_e]:
        color = black
    
    if keys[pig.K_s] and keys[pig.K_F1]:
        num += 1
        pig.image.save(win, path+"1.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/{num}.png'))
        subprocess.Popen('explorer "C:/desktop"')
        subprocess.CREATE_NEW_CONSOLE

    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_1]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/1.png'),(0,0))
    
    if keys[pig.K_s] and keys[pig.K_F2]:
        color1 = color
        pig.image.save(win, path +"1.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/2.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_2]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/2.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F3]:
        color1 = color
        pig.image.save(win, path+"2.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/3.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_3]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/3.png'),(0,0))

                
    if keys[pig.K_s] and keys[pig.K_F4]:
        color1 = color
        pig.image.save(win, path+"3.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/4.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_4]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/4.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F5]:
        color1 = color
        pig.image.save(win, path+"4.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/5.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_5]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/5.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F6]:
        color1 = color
        pig.image.save(win, path+"5.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/6.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_6]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/6.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F7]:
        color1 = color
        pig.image.save(win, path+"6.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/7.png'))
        subprocess.Popen('explorer "C:/desktop"')
        
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_7]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/7.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F8]:
        color1 = color
        pig.image.save(win, path+"7.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/8.png'))
        subprocess.Popen('explorer "C:/desktop"')
    
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_8]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/8.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_F9]:
        color1 = color
        pig.image.save(win, path+"8.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/9.png'))
        subprocess.Popen('explorer "C:/desktop"')
    
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_9]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/9.png'),(0,0))

    if keys[pig.K_s] and keys[pig.K_END]:
        color1 = color
        pig.image.save(win, path+"9.png")
        pig.image.save(win, (p_a_p + r'paint app gus v5\data/saves/0.png'))
        subprocess.Popen('explorer "C:/desktop"')
    
    if keys[pig.K_s] and keys[pig.K_o] and keys[pig.K_0]:
        win.blit(pig.image.load(p_a_p + r'paint app gus v5\data/saves/0.png'),(0,0))

    
    if keys[pig.K_z]:
        win.fill((black))

    if keys[pig.K_x]:
       win.fill((white))
    
    if keys[pig.K_t] and keys[pig.K_u]:
        rainbow_mode = False
        color = turquoise

    if keys[pig.K_s] and keys[pig.K_b]:
        rainbow_mode = False
        color = sky_blue
    
    if keys[pig.K_m]:
        rainbow_mode = False
        color = magenta

    if keys[pig.K_d] and keys[pig.K_b]:
        rainbow_mode = False
        color = dark_blue

    if keys[pig.K_s] and keys[pig.K_c]:
        rainbow_mode = False
        color = skin_color

    if keys[pig.K_l]:
        rainbow_mode = False
        color = lime
        
    if keys[pig.K_c] and keys[pig.K_i]:
        circle_mode = True
        
    if keys[pig.K_s] and keys[pig.K_q]:
        width = 20
        hight = 20
        circle_mode = False
        
    if keys[pig.K_n] and keys[pig.K_r]:
        width = 0
        height = 0
         
    if keys[pig.K_ASTERISK]:
        christmas = True
         
    if christmas == True:
        circle_mode = True
        width_hight = 5
        color = red
        color1 = green
        ma = 30
        if keys[pig.K_1] and keys[pig.K_c]:
            ma = 3
            christmas = True
    
    if keys[pig.K_n] and keys[pig.K_c]:
        christmas = False
        ma = 1
        circle_mode = False
    
            
    if keys[pig.K_c] and keys[pig.r]:
        crazy = True
    
    if crazy == True:
        width1 + 10
        height1 + 10
        width_hight1 + 10
        cr_co = [
            black,
            red,
            orange,
            yellow,
            lime,
            green,
            turquoise,
            sky_blue,
            blue,
            dark_blue,
            magenta,
            purple,
            pink,
            skin_color,
            white     
        ]
            
            
            
        
        if keys[pig.K_LEFT] or keys[pig.K_a]and x>0:
            x -= ma
            a -= ma
            color1 = blue
          
        if keys[pig.K_RIGHT] or keys[pig.K_d]and x<1920-width:
            x += ma
            a += ma
            color1 = green
         
        if keys[pig.K_UP] or keys[pig.K_w]and y>0:
            y -= ma
            b -= ma  
            color1 = red
      
        if keys[pig.K_DOWN] or keys[pig.K_s] and y<1025-height:
            y += ma
            b += ma
            color1 = yellow
        

    
            
    

    
    if not circle_mode:
        rect(win, (color), (x, y, width, height))    
        rect(win, (color1), (a, b, width1, height1))  
        
    else:
        circle(win, x +10, y+9, width_hight, color)
        circle(win, x +10, y+9, width_hight1,color1)  
        
        
    
        
    
    
    
        
        
    
pig.display.update()        

  

while True :
  

    pig.display.update()       

    pig.quit()