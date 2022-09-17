import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from core import input

class Window:
    WIDTH = 480
    HEIGHT = 270
    TITLE = "OPENGL"

    def __init__(self, W, H, TITLE):
        if not glfw.init():
            return
        self.clearColor = [0.15, 0.15, 0.15, 1.0]
        self.create(W, H, TITLE)

    def create(self, W, H, TITLE):
        Window.WIDTH = W
        Window.HEIGHT = H
        Window.TITLE = TITLE
        self.window = glfw.create_window(W, H, TITLE, None, None)

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.SAMPLES, 8)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

        if not self.window:
            glfw.terminate()
            return
        glfw.make_context_current(self.window)
        glViewport(0, 0, Window.WIDTH, Window.HEIGHT)
        glClearColor(*self.clearColor)
        # Callbacks
        self.setup_callbacks()
        return self.window

    def isNotClosed(self):
        return not glfw.window_should_close(self.window)

    def get_window(self):
        return self.window

    def setup_callbacks(self):
        glfw.set_window_size_callback(self.window, self.on_resize)
        glfw.set_cursor_pos_callback(self.window, input.mouse_handler)
        glfw.set_key_callback(self.window, input.keyboard_handler)

    def update(self, mask=GL_COLOR_BUFFER_BIT):
        glfw.swap_buffers(self.window)
        glfw.poll_events()
        glClear(mask)

    def on_resize(self, _, width, height):
        Window.WIDTH = width
        Window.HEIGHT = height
        glViewport(0, 0, Window.WIDTH, Window.HEIGHT)

    def close(self):
        glfw.terminate()
