"""
This is a two body problem simulation

To see the bodies orbital path comment out line 101

This comes with a rubber band function 
to remove it comment out lines 101,111,112
otherwise use these values in lines 111,112 to get good results

Bodies.append(rubberband(800,275,0,0,0,1,pow(10,2.5)*1/2,100,10))
Bodies.append(rubberband(340,175,0,0,0,0,pow(10,2.5)*1/2,200,10))

if you do remove the rubberband these definitions for bodies work well and capy this code in to replace lines 79 and 80

Bodies.append(rubberband(800,275,0,0,-0.7,-0.7,pow(10,7)*1/2,100,10))
Bodies.append(rubberband(340,175,0,0,1,0.8,pow(10,7.25)*1/2,200,10))

have fun
*there are even ways to show a gravity assist
"""

import pygame
import numpy as np


pygame.init() # Initialize all imported Pygame modules

screen = pygame.display.set_mode((900, 700))
screen.fill((255, 255, 255))
pygame.display.set_caption("Two Body Problem")


class planet():
    def __init__(self,x,y,Fx,Fy,Vx,Vy,m,COLOR,r):
        self.x=x
        self.y=y
        self.Fx=Fx
        self.Fy=Fy
        self.Vx=Vx
        self.Vy=Vy
        self.m=m
        self.COLOR=COLOR
        self.r=r
        
    def add_force(self,FAX,FAY): #DUH adds a force in x,y compoents
        self.Fx=self.Fx+FAX
        self.Fy=self.Fy+FAY
        
    def update(self,dt): #Updates position velocity and force
        self.Vx=self.Vx+self.Fx*dt
        self.Vy=self.Vy+self.Fy*dt
        self.x=self.x+self.Vx*dt
        self.y=self.y+self.Vy*dt
        
        
        
        self.Fx=0
        self.Fy=0
        

    def Draw(self):
        pygame.draw.circle(screen, (0, 255, self.COLOR), [self.x, self.y], self.r, 0)
class rubberband(planet):
    
    def rubber_band_F(self,k,r,dx,dy):
        self.dx=dx
        self.dy=dy
        self.rad=r
        self.k=k
        self.F=-self.k*self.rad #using weird variables so I do not redifine existing ones
        self.new_Fx=self.F*self.dx/self.rad
        self.new_Fy=self.F*self.dy/self.rad
        super().add_force(self.new_Fx,self.new_Fy) #call add force from main function
        self.F=0
        
def collision(B1,B2):
    R=B1+B2
    return R
Bodies=[] #list of planets

Bodies.append(rubberband(800,275,0,0,-0.7,-0.7,pow(10,7)*1/2,100,10))
Bodies.append(rubberband(340,175,0,0,1,0.8,pow(10,7.25)*1/2,200,10))
  

G=6.674*pow(10,-11)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

# Fill the screen with white color
    pygame.display.update()
    screen.fill((255,255,255)) # uncomment to see body orbits
    pygame.draw.rect(screen, (0, 0, 0), (0, 350, 900, 1), width=1)
    pygame.draw.rect(screen, (0, 0, 0), (450, 0, 1,700), width=1)
    
    
    if len(Bodies) > 1:
        #pygame.draw.line(screen,(255,0,0),(Bodies[0].x,Bodies[0].y),(Bodies[1].x,Bodies[1].y),width=2)
        for i in range(1,2000): # loop 1 defining forces and other stuff
            DX=Bodies[0].x-Bodies[1].x
    
            DY=Bodies[0].y-Bodies[1].y
            r=pow(pow(DX,2)+pow(DY,2),0.5)
            F=(G*Bodies[0].m*Bodies[1].m)/pow(r,2)
            Fx,Fy=F*DX/r,F*DY/r
            Bodies[0].add_force(-Fx,-Fy)
            Bodies[1].add_force(Fx,Fy)
           # Bodies[0].rubber_band_F(0.0008, r, DX, DY)
           # Bodies[1].rubber_band_F(-0.0008, r, DX, DY)
            if r <= 20:
                print(Bodies[0].Vx,Bodies[0].Vy,Bodies[1].Vx,Bodies[1].Vy)
                Sign=[(Bodies[1].Vy-Bodies[0].Vy),(Bodies[1].Vx-Bodies[0].Vx)]
                Bodies[0].r=collision(Bodies[0].r,Bodies[1].r)
                Bodies[0].Vx=(abs(Bodies[1].Vx)-abs(Bodies[0].Vx))*np.sign(Sign[1])
                Bodies[0].Vy=(abs(Bodies[1].Vy)-abs(Bodies[0].Vy))*np.sign(Sign[0])
                Bodies.pop(1)
                print(Bodies[0].Vx,Bodies[0].Vy)
                break
        
            
    for i in range(1,1000):
        for j in range(len(Bodies)):
            Bodies[j].update(0.001)
            Bodies[j].Draw()

        
        

pygame.quit()