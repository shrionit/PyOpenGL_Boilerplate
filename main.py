from OpenGL.GL import glDrawElements, GL_TRIANGLES, GL_UNSIGNED_INT
from core.display import Window
from core.shader import Shader
from core.storage import VAO, VBO, IBO
from core.shapes import RECT

WIDTH = 1366
HEIGHT = 768
TITLE = "GL_Window"

def main():
    # Creating Window
    window = Window(WIDTH, HEIGHT, TITLE)
    
    # Creating shaders with basic.frag and basic.vert, no need to specify extension
    shader = Shader(frag="basic", vert="basic")
    
    # Creating Vertex Array Buffer
    vao = VAO()
    vao.loadBufferToAttribLocation(0, VBO(RECT.vertices)) # Binding vertices buffer to attrib number 0
    vao.loadBufferToAttribLocation(1, VBO(RECT.vertexColors)) # Binding colors buffer to attrib number 1
    vao.loadIndices(IBO(RECT.indices)) # Binding indeces buffer
    
    shader.attach() # using shader
    
    while window.isNotClosed():
        vao.bind()
        glDrawElements(GL_TRIANGLES, len(RECT.indices), GL_UNSIGNED_INT, None)
        vao.unbind()
        window.update()
    
    del vao # cleanup
    shader.detach() # unbinding shader
    window.close() # terminating the glfw window

if __name__=='__main__':
    main()