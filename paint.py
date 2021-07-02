import pygame
from pygame.locals import *
import sys
x = pygame.init()
# colors
white = (255, 255, 255)
black =(0,0,0)
# window creating
width, heigth = 1100, 700
win = pygame.display.set_mode((width, heigth))
# Name change
pygame.display.set_caption("Paint")
# Icon change
gameIcon = pygame.image.load('paint_icon.png')
pygame.display.set_icon(gameIcon)
win.fill(white)
font = pygame.font.SysFont('Constantia', 30)
pygame.display.update()
ck =pygame.time.Clock()
clicked = False
class button():
    # colours for button and text
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = white
    width = 100
    height = 60

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def draw_button(self):
        global button_col
        if self.text == "G":
            button_col = (0,255,0)
            self.text_col = black
        if self.text == "R":
            button_col = (255,0,0)
            self.text_col = black
        if self.text == "B":
            button_col = (0,0,0)
        if self.text == "Bl":
            button_col = (0,0,255)
            self.text_col = black
        if self.text == "O":
            button_col = (255,128,0)
            self.text_col = black
        if self.text == "Y":
            button_col = (255,255,0)
            self.text_col = black
        if self.text == "Wh":
            button_col = (255,255,255)
            self.text_col = black
        if self.text == "<":
            button_col = (115,115,115)
        if self.text == ">":
            button_col = (115,115,115)
        if self.text == "Eraser":
            button_col = (10,255,108)
            self.text_col = black
        if self.text == "AC":
            button_col = (40,40,40)
            self.text_col = white
        global clicked
        action = False
        # get mouse position
        m,n = pygame.mouse.get_pos()
        # create pygame Rect object for the button
        if self.text == ">" or self.text == "<" or self.text == "AC":
            button_rect = Rect(self.x, self.y, self.width//2, self.height)
        else:
            button_rect = Rect(self.x, self.y, self.width, self.height)
        # check mouseover and clicked conditions
        if button_rect.collidepoint(m,n):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(win, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(win, self.hover_col, button_rect)
        else:
            pygame.draw.rect(win, button_col, button_rect)

        # add shading to button
        if self.text == ">" or self.text == "<" or self.text == "AC":
            pygame.draw.line(win,black, (self.x, self.y), (self.x + 50, self.y), 2)
            pygame.draw.line(win,black, (self.x, self.y), (self.x, self.y +self.height), 2)
            pygame.draw.line(win, black, (self.x, self.y + self.height), (self.x + 50, self.y + self.height), 2)
            pygame.draw.line(win, black, (self.x + 50, self.y), (self.x + 50, self.y + self.height), 2)
        else:
            pygame.draw.line(win,black, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(win,black, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(win, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pygame.draw.line(win, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        # add text to button
        if(self.text == "AC"):
            font2=pygame.font.Font(None,30)
            dis_size = font2.render("AC",True,white)
        else:
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
        if self.text == ">" or self.text == "<":
            win.blit(text_img, (self.x + int(50 / 2) - int(text_len / 2), self.y-10 + 25))
        elif(self.text == "AC"):
            win.blit(dis_size,(1033,35))
        else:
            win.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return (clicked)
q=[]
xcommonstart = 105
xcommonend = 104
color =[0,0,0]
green = button(5, 5, "G")
red = button(110,5,"R")
yellow = button(215,5,"Y")
blue = button(320,5,"Bl")
orange = button(425,5,"O")
black1 = button(530,5,"B")
white1 = button(635,5,"Wh")
arrowdecrease = button(760,5,"<")
arrowincrease = button(865,5,">")
erase = button(918,5,"Eraser")
clearwindow = button(1022,5,"AC")
def check(z,x,y,col,q,size,eraser,eraser_size):
    if z == 1:
        q.append((x,y))
        for i in range(1,len(q)):
            if(eraser==0):
                pygame.draw.line(win,col,(q[i-1][0],q[i-1][1]),(q[i][0], q[i][1]),size)
            else:
                pygame.draw.line(win,col,(q[i-1][0],q[i-1][1]),(q[i][0], q[i][1]),eraser_size)
        pygame.display.update()
def pen_size(lent):
    pygame.draw.rect(win,white,(814,5,50,62)),
    font2=pygame.font.Font(None,30)
    dis_size = font2.render("Size",True,black)
    length = font2.render(str(lent),True,black)
    win.blit(dis_size,(818,12))
    win.blit(length,(832,35))
size = 2
def main():
    run = True
    z=0
    q=[]
    size_list=[2]
    eraser = 0
    eraser_size = 12
    while run:
        global color
        global size
        
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    z=1
                else:
                    z=0
                    size = size_list[0]
                    q.clear()
            if event.type == pygame.MOUSEBUTTONUP:
                z=0
                size = size_list[0]
                q.clear()
            if(y>76 and y<692 and x>6 and x<1093):
                #print(x,y)
                if(size>1 and size<10):
                    if(eraser==1):
                        check(z,x,y,color,q,size,eraser,eraser_size)
                    else:
                        check(z,x,y,color,q,size,eraser,eraser_size)
                else:
                    if(size>=10):
                        if(eraser!=1):
                            size = 9
                        else:
                            size = 9
                            eraser_size = 12
                    if(size<2):
                        if(eraser!=1):
                            size = 2
                        else:
                            size =2
                            eraser_size = 12
        #pygame.draw.circle(win,(0,255,0),(50,20),15)
        #button("G",80,10,40,40,(0,255,0),(128,255,115),"g")
        #print(x,y)
        if (clearwindow.draw_button() and (x>=1029 and x<=1079) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    win.fill(white)
                    eraser = 0
        if (green.draw_button() and (x>=6 and x<=104) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [0, 255, 0]
                    eraser = 0
        if (red.draw_button() and (x>=6+xcommonstart and x<=104+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [255,0,0]
                    eraser = 0
        if (yellow.draw_button() and  (x>=111+xcommonstart and x<=208+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [255, 255,0]
                    eraser = 0
        if (blue.draw_button() and (x>=216+xcommonstart and x<=312+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [0, 0, 255]
                    eraser = 0
        if (orange.draw_button() and (x>=321+xcommonstart and x<=416+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [255, 128,0]
                    eraser = 0
        if (black1.draw_button() and (x>=426+xcommonstart and x<=520+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [0, 0, 0]
                    eraser = 0
        if (white1.draw_button() and (x>=531+xcommonstart and x<=624+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [255, 255,255]
                    eraser = 0
        if (erase.draw_button() and (x>=920 and x<=920+xcommonend) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    color = [255, 255,255]
                    eraser = 1
        if(arrowdecrease.draw_button()  and (x>=762 and x<=808) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    global s
                    if(size>2):
                        s = size-1
                        size_list.pop(0)
                        while(len(size_list)<1):
                            size_list.append(s)
                    else:
                        size = 2
        if(arrowincrease.draw_button()  and (x>=867 and x<=912) and (y>=6 and y<=60)):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if ((event.button == 1)):
                    if(size<10):
                        s = size+1
                        size_list.pop(0)
                        while(len(size_list)<1):
                            size_list.append(s)
                    else:
                        size = 9
                    #print(size_list)
        #636 728
        if(size<=2):
            ac_s = 2
            eraser_size = 12
        elif(size>=10):
            ac_s = 9
            eraser_size = 12
        else:
            ac_s = size
            eraser_size = 12
        pen_size(ac_s)
        pygame.draw.line(win,(0,0,0),[0,70],[width,70],5)
        pygame.draw.line(win, (0, 0, 0), [(width//2)+200, 0], [(width//2)+200, 70], 5)
        pygame.draw.line(win, (0, 0, 0), [0+2, 0+2], [0+2, width+2], 6)
        pygame.draw.line(win, (0, 0, 0), [width-3,3], [width-3, heigth-3], 6)
        pygame.draw.line(win, (0, 0, 0), [0,heigth-3], [width, heigth-3], 6)
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
