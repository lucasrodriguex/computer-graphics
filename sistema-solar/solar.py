from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

def renderScene():
    glPushMatrix()
    #To rotate around drawn object
    gluLookAt(0.0,0.0,-4.0,0.0,0.0,1.0,0.0,-3.0,0.0)
    glColor3f(1.0,1.0,0.0)
    glutSolidSphere(SunSize,50,50)   # Display Sun as solid object
    glRotatef(year,0.0,1.0,0.0)   # Rotation of Earth around Sun
    glTranslatef(EarthOrbitRadius,0.0,0.0)
    glPushMatrix()
    glRotatef(day,0.25,1.0,0.0)
      
    glColor3f(0.0,0.0,1.0)
    glutSolidSphere(EarthSize,10,10)    #Display Earth as a solid object
    glPopMatrix()

    # Rotation of Moon around Earth
    glRotatef(moonAroundEarth,0.0,1.0,0.0)                                                                            
    glTranslatef(MoonOrbitRadius,0.0,0.0)
    glRotatef(moonItsSelf,0.0,1.0,0.0)
                         
    glColor3f(1.0,1.0,1.0)
    glutSolidSphere(MoonSize,8,8)   #Display Moon as a solid object
    glPopMatrix()                    

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    renderScene()
    glFlush()
    glutSwapBuffers()
      
def myWireSphere(radius, slices, stacks):
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  glutWireSphere(radius, slices, stacks)
  glPopMatrix()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(x,y):
    if (y == 0): 
        return
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0,x/y,0.5,20.0)
    glMatrixMode(GL_MODELVIEW)
    glViewport(0,0,x,y)
    display()

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glClearDepth(10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def idle():
    global day
    global year
    global moonItsSelf
    global moonAroundEarth

    day += daySpeed
    year += yearSpeed
    moonItsSelf += moonItsSelfSpeed
    moonAroundEarth += moonAroundEarthSpeed
    display()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow("PRACTICAL4")
    init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutMainLoop()

SpeedMultiplicator = 1.0
DaysPerYear = 10.0
year = 0.0   #degrees
day = 0.0
moonAroundEarth = 0.0
moonItsSelf = 0.0

EarthOrbitRadius = 1.25
MoonOrbitRadius = 0.20
daySpeed = 5.0 * SpeedMultiplicator
yearSpeed = DaysPerYear / 360.0 * daySpeed * SpeedMultiplicator
moonAroundEarthSpeed = 1.25 * SpeedMultiplicator
moonItsSelfSpeed = 1 * SpeedMultiplicator
SunSize = 0.5
EarthSize = 0.10
MoonSize = 0.05
main()


