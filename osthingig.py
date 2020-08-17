import pyglet
from pyglet.window import key, mouse
from pyglet import shapes

window = pyglet.window.Window(width=500, height=500)
batch = pyglet.graphics.Batch()
global paint
paint = False
global txt
txt = False


class application():
    def __init__(self, name, x, y, size_x, size_y, color):
        shapemaker = name + "= shapes.Rectangle(x=" + x + ", y=" + y + ", width=" + size_x + ", height=" + size_y + ", color=" + color + \
                     ", batch=batch) "
        titleadder = pyglet.text.Label(name, "Arial", 12, y=y - size_y)
        exec(shapemaker)


doc = shapes.Rectangle(
    x=0, y=0, width=window.width, height=window.height / 16, color=(255, 0, 255), batch=batch)

q = shapes.Rectangle(
    x=40, y=40, width=40, height=40, color=(255, 0, 0), batch=batch)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    """print(x, y, dx, dy)
    doc.x = x
    doc.y = y"""


@window.event
def on_draw():
    window.clear()
    if not paint or not txt:
        batch.draw()

    if paint:
        window.clear()
        back = shapes.Rectangle(
            x=0, y=0, width=window.width, height=window.height, color=(255, 255, 255), batch=batch)


def on_mouse_press(x, y, button, modifiers):
    if x in range(q.x, q.x + q.width) and y in range(q.y, q.y + q.width) and button == mouse.LEFT:
        global paint
        paint = True


pyglet.app.run()
