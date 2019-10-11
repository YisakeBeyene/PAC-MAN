from pacman import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Ghost:
    def __init__(self,a,b):
        self.tx=a
        self.ty=b
        self.angle=90
        self.speed=1
        self.max_speed=1
        self.color=[1,0,0]
        self.eaten=False
        self.transporting=False
    def Move(self):
        self.tx += speed*maths.cos(math.pi/180*angle)
        self.ty += speed*maths.sin(math.pi/180*angle)


    def Draw(self):
        glColor3f(self.color[0],self.color[1],self.color[2])
        if (self.eaten):
            glColor3f(1,1,0)
        glPushMatrix()
        glTranslatef(self.tx,-self.ty,0)
        glTranslatef(0.5,0.6,0)
        glTranslatef(31/-2.0, 28/2.0,0.5)
        glutSolidSphere(.5,10,10)
        glPopMatrix()
    def chase(self,px,py,open_move):
        c=-1
        moved=False
        if (self.angle == 0 or self.angle== 180):
            if(c*py>c*self.ty  and open_move[1]):
                self.angle=90
            elif(c*py<c*self.ty  and open_move[3]):
                self.angle=270
        elif (self.angle == 90 or self.angle== 270):
            if(c*px>c*self.tx  and open_move[0]):
                self.angle=0
            if (c*px<c*self.tx  and open_move[2]):
                self.angle=180
        #random moves
        if (self.angle == 0 and not open_move[0]):
            self.angle = 90

        if (self.angle == 90 and not open_move[1]):
            self.angle = 180

        if (self.angle == 180 and not open_move[2]):
            self.angle = 270
        if (self.angle == 270 and not open_move[3]):
            self.angle = 0

        if (self.angle == 0 and not open_move[0]):
            self.angle = 90
    def catch(self,px,py):
        #collision detection
        if(px - self.tx < 0.2 and px - self.tx > -0.2 and py - self.ty < 0.2 and py - self.ty > -0.2):
            return True
        return False
    def Update(self):
        if(self.tx == 27 and self.ty==14 and not (self.transporting)):
            self.angle=0
        if(self.tx>26.9 and self.ty==14):
            self.tx=0.1
            self.transporting=True
        if(self.tx==2 or self.tx==25):
            self.transporting=False
        if(self.tx<13):
            self.angle=0
        if(self.tx>14):
            self.angle=180
    
        
                
        
        

    
