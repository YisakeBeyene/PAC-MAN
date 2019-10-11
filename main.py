from pacman import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Ghost import *
from Keyboard import *
a=1
b=2
def Pac():
    #Draw Pacman
    glColor3f(0,1,1)
    glPushMatrix()
    glTranslatef(a,-b,0)
    glTranslatef(0.5,0.6,0)
    glTranslatef(31/-2.0,28/2.0,0.5)
    glutSolidSphere(0.5,15,10)
    glPopMatrix()
def create_list_lib():
    #Set Up Maze Using Lists
    list1 = glGenLists(1)
    glNewList(list1, GL_COMPILE)

    #North Wall
    glBegin(GL_QUADS)
    glColor3f(0,0,1)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 1.0)
    glEnd()
    glEndList()

    list2 = glGenLists(1)
    glNewList(list2, GL_COMPILE)
    glBegin(GL_QUADS)
    #North Wall
    glColor3f(0,0,1)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 1.0)
    #South Wall
    glColor3f(0,0,1)
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glEndList()

    list3 = glGenLists(1)

    glNewList(list3, GL_COMPILE)
    glBegin(GL_QUADS)
    #North Wall
    glColor3f(0,0,1)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 1.0)
    #East Wall
    glColor3f(0,0,1)
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()
    glEndList()


    list4 = glGenLists(1)

    glNewList(list4, GL_COMPILE)
    glBegin(GL_QUADS)
    #Top Wall
    glColor3f(-1,0.3,0)
    glNormal3f(1.0, 0.0, 1.0)
    glVertex3f(1, 1, 1.0)
    glVertex3f(0, 1, 1.0)
    glVertex3f(0, 0, 1.0)
    glVertex3f(1, 0, 1.0)
    glEnd()
    glEndList()
    
def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    


def init():
    glEnable(GL_NORMALIZE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1.33,0.005,100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(-1.5, 0, 40, -1.5, 0, 0, 0.0,1.0,0.0)
    
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
    glutInitWindowSize(1200, 780)
    glutInitWindowPosition(0,0)
    glutCreateWindow(bytes("Pac","ascii"))
    init()
    glutDisplayFunc(RenderScene)
    create_list_lib()
    Pac()

    #glutKeyboardFunc(mykey)

    #glutSpecialFunc(specialDown)
    #glutSpecialUpFunc(specialUp)

    glEnable(GL_DEPTH_TEST)

    '''for the ghosts'''
    start_x=[11,12,15,16]
    ghost=[]
    for i in range(0,4): #for all gohsts
        ghost.append(Ghost(start_x[i],14))
    ghost_color=[(255/255,0,0),(120/255,240/255,120/255),(255/255,200/255,200/255),(255/255,125/255,0)]
    for i in range(0,4):
        ghost[i].x=start_x[i]
        ghost[i].y=14
        ghost[i].eaten=False
        ghost[i].max_speed=0.1-0.01*i
        ghost[i].speed=ghost[i].max_speed
    #colorize ghosts
        for j in range(0,3):
            ghost[i].color[j]=ghost_color[i][j]
    tp_array=[]
    for k in range(0,31):
        for l in range(0,28):
            tp_array[k][l]=pebbele_array[k][l]
    pebbeles_left=244
    glShadeModel(GL_SMOOTH)
    glMainLoop()
    
    
main()
