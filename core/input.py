from .utils import Dict
import glfw as g

mouse = Dict({'x': 0, 'y': 0, 'dx': 0, 'dy': 0})
keyboard = [False] * 349
keyboard_events = [lambda:None] * 349

def mouse_handler(_, x, y):
    mouse.dx = x - mouse.x
    mouse.dy = y - mouse.y
    mouse.x = x
    mouse.y = y

def keyboard_handler(_, key, scancode, action, mods):
    keyboard[key] = action >= g.PRESS
    if keyboard[key]: keyboard_events[key]()

def set_on_key(key, cb):
    if type(cb).__name__ == 'function':
        keyboard_events[key] = cb

is_key_pressed = lambda key: keyboard[key]

def on_scroll(w, f):
    flag = False
    if flag:
        g.set_scroll_callback(w, f)
