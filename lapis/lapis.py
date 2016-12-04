from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
 
 
#dropbox -> https://www.dropbox.com/sh/sgy5d7spqtu4oca/AABWbwj05d270xbPqJJawoyxa?dl=0
 
vertices = (
    ( 1,-1,-1), #0
    ( 1, 1,-1), #1
    (-1, 1,-1), #2
    (-1,-1,-1), #3
    ( 1,-1, 1), #4
    ( 1, 1, 1), #5
    (-1,-1, 1), #6
    (-1, 1, 1),#7
    (0,2,0),    #8 teto
    (0.7 ,   0,  1), #9  porta
    (0   ,   0,  1), #10 porta
    (0   ,  -1,  1), #11 porta
    (0.7 ,  -1,  1), #12 porta
    (-0.8 ,   0,  1), #13 janela
    (-0.5   ,   0,  1), #14 janela
    (-0.5   ,  -0.5,  1), #15 janela
    (-0.8 ,  -0.5,  1), #16 janela
 
     
    )
 
linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    (5,8),
    (7,8),
    (2,8),
    (1,8),
    (9,10),
    (9,12),
    (10,11),
    (13,14),
    (14,15),
    (13,16),
    (15,16),
    )
 
faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    (7,2,8,1),
    (2,1,8,5),
    (1,5,8,7),
    (5,7,8,2),
    )
 
def Cubo():
    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv((0,1,0))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
 
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()
 
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    Cubo()
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
 
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glClearColor(0.,0.,0.,1.)
glutDisplayFunc(display)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()