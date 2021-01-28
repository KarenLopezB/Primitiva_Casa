from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPasto():
    glColor3f(0.1,0.7,0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarNube1():
    glColor3f(0.9,1,0.9)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 -0.17, sin(angulo) * 0.05 + 0.68, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.05, sin(angulo) * 0.05 + 0.7, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 -0.06, sin(angulo) * 0.05 + 0.64, 0.0)
    glEnd()

def dibujarNube2():
    glColor3f(0.9,1,0.9)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.57, sin(angulo) * 0.05 + 0.68, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.75, sin(angulo) * 0.05 + 0.7, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.66, sin(angulo) * 0.05 + 0.64, 0.0)
    glEnd()

def dibujarNube3():
    glColor3f(0.9,1,0.9)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.35, sin(angulo) * 0.07 + 0.40, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.1 + 0.25, sin(angulo) * 0.07 + 0.44, 0.0)
    glEnd()

def dibujarArbol():
    glColor3f(0.1,0.4,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 -0.75, sin(angulo) * 0.15 + -0.0, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 -0.7, sin(angulo) * 0.15 + 0.1, 0.0)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 -0.75, sin(angulo) * 0.15 + 0.2, 0.0)
    glEnd()

def dibujarArbolpalo():
    glColor3f(0.3,0.1,0)
    glBegin(GL_QUADS)
    glVertex3f(-0.8,0.0,0.0)
    glVertex3f(-0.7,0.0,0.0)
    glVertex3f(-0.7,-0.5,0.0)
    glVertex3f(-0.8,-0.5,0.0)
    glEnd()

def dibujarVentana1():   
    glColor3f(1,0.9,1)
    glBegin(GL_QUADS)
    glVertex3f(-0.35,-0.3,0.0)
    glVertex3f(0.05,-0.3,0.0)
    glVertex3f(0.05,-0.1,0.0)
    glVertex3f(-0.35,-0.1,0.0)
    glEnd()

def dibujarVentana2():   
    glColor3f(1,0.9,1)
    glBegin(GL_QUADS)
    glVertex3f(0.85,-0.3,0.0)
    glVertex3f(0.45,-0.3,0.0)
    glVertex3f(0.45,-0.1,0.0)
    glVertex3f(0.85,-0.1,0.0)
    glEnd()

def dibujarTecho1():   
    glBegin(GL_TRIANGLES)
    glColor3f(1,0.3,0.5)
    glVertex3f(-0.3,0.25, 0.0)
    glVertex3f(-0.5,0.0, 0.0)
    glVertex3f(-0.3,0.0, 0.0)
    glEnd()

def dibujarTecho2():   
    glBegin(GL_TRIANGLES)
    glColor3f(1,0.3,0.5)
    glVertex3f(0.8,0.25, 0.0)
    glVertex3f(1.0,0.0, 0.0)
    glVertex3f(0.8,0.0, 0.0)
    glEnd()

def dibujarTecho3():
    glColor3f(1,0.3,0.5)
    glBegin(GL_QUADS)
    glVertex3f(-0.3,0.0,0.0)
    glVertex3f(0.8,0.0,0.0)
    glVertex3f(0.8,0.25,0.0)
    glVertex3f(-0.3,0.25,0.0)
    glEnd()

def dibujarPerilla():
    glColor3f(0.2,0,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.2, sin(angulo) * 0.02 + -0.35, 0.0)
    glEnd()

def dibujarPuerta():
    glColor3f(0.4,0.1,0)
    glBegin(GL_QUADS)
    glVertex3f(0.17,-0.5,0.0)
    glVertex3f(0.33,-0.5,0.0)
    glVertex3f(0.33,-0.2,0.0)
    glVertex3f(0.17,-0.2,0.0)
    glEnd()

def dibujarPuertaarriba():
    glColor3f(0.4,0.1,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.08 + 0.25, sin(angulo) * 0.08 + -0.2, 0.0)
    glEnd()   

def dibujarParedcasa1():
    glColor3f(1,0.7,0.7)
    glBegin(GL_QUADS)
    glVertex3f(0.4,-0.5,0.0)
    glVertex3f(0.9,-0.5,0.0)
    glVertex3f(0.9,0.0,0.0)
    glVertex3f(0.4,0.0,0.0)
    glEnd()

def dibujarParedcasa2():
    glColor3f(1,0.7,0.7)
    glBegin(GL_QUADS)
    glVertex3f(-0.4,-0.5,0.0)
    glVertex3f(0.1,-0.5,0.0)
    glVertex3f(0.1,0.0,0.0)
    glVertex3f(-0.4,0.0,0.0)
    glEnd()

def dibujarParedpuerta():
    glColor3f(1,0.8,0.9)
    glBegin(GL_QUADS)
    glVertex3f(0.1,-0.5,0.0)
    glVertex3f(0.4,-0.5,0.0)
    glVertex3f(0.4,0.05,0.0)
    glVertex3f(0.1,0.05,0.0)
    glEnd()

def dibujarRayos():
    glColor(1,0.6,0.1)
    glBegin(GL_LINES)
    glVertex3f(-0.85,0.4,0.0)
    glVertex3f(-0.96,0.3,0.0)

    glVertex3f(-1.0,0.55,0.0)
    glVertex3f(-0.9,0.55,0.0)

    glVertex3f(-0.35,0.55,0.0)
    glVertex3f(-0.5,0.55,0.0)

    glVertex3f(-0.7,0.9,0.0)
    glVertex3f(-0.7,0.75,0.0)

    glVertex3f(-0.85,0.7,0.0)
    glVertex3f(-0.95,0.8,0.0)

    glVertex3f(-0.45,0.8,0.0)
    glVertex3f(-0.55,0.7,0.0)

    glVertex3f(-0.45,0.3,0.0)
    glVertex3f(-0.55,0.4,0.0)
    glEnd()

def dibujarSol():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 -0.7, sin(angulo) * 0.15 + 0.55, 0.0)
    glEnd()

def dibujar():
    #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    
    glEnd()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.1,0.8,0.9,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujarPasto()
        dibujar()
        dibujarSol()
        dibujarRayos()
        dibujarParedcasa1()
        dibujarParedcasa2()
        dibujarParedpuerta()
        dibujarPuerta()
        dibujarPuertaarriba()
        dibujarTecho1()
        dibujarTecho2()
        dibujarTecho3()
        dibujarPerilla()
        dibujarVentana1()
        dibujarVentana2()
        dibujarArbolpalo()
        dibujarArbol()
        dibujarNube1()
        dibujarNube2()
        dibujarNube3()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()