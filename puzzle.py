import pyglet
import pyglet.shapes

window = pyglet.window.Window(width=500, height=500)
batch = pyglet.graphics.Batch()

bg = pyglet.shapes.Rectangle(x=0, y=0, height=window.height, width=window.width, batch=batch)
protagonist = pyglet.shapes.Rectangle(0, 0, 50, 50, color=(255, 22, 255), batch=batch)


def block(x, y):
    kjl = pyglet.shapes.Rectangle(x*50, y*50, 50, 50, color=(0, 0, 0), batch=batch)
    if protagonist.x == x*50 and protagonist.y == y*50:
        protagonist.x, protagonist.y = 0, 0
        print("respawned")


def wall(x1, y1, width, height):
    kjld = pyglet.shapes.Rectangle(x1*50, y1*50, width=width*50, height=height*50, color=(0, 0, 0), batch=batch)
    for i in range(x1, x1+width):
        for b in range(y1, y1+height):
            block(i, b)

global won
won = False

@window.event
def on_draw():
    global won

    winplate = pyglet.shapes.Rectangle(5 * 50, 0 * 50, 50, 50, (0, 255, 0), batch)
    if protagonist.x == winplate.x and protagonist.y == winplate.y:
        won = True

    if not won:
        block(0, 1)
        block(1, 1)
        block(2, 1)
        block(2, 2)
        block(2, 3)
        block(1, 3)

        wall(4, 0, 1, 8)
        wall(1, 5, 3, 1)
        wall(1, 7, 3, 1)
        wall(0, 9, 6, 1)
        wall(6, 6, 1, 4)
        block(7, 6)
        wall(5, 4, 4, 1)
        wall(8, 6, 1, 3)
        wall(6, 0, 1, 3)
        wall(7, 2, 2, 1)
        block(8, 1)

        batch.draw()

    else:
        window.clear()
        vic = pyglet.text.Label(text="Victory!", font_name="Minecraft", font_size=24, x=window.width/2 - 75, y=window.height/2 - 24)
        vic.draw()


@window.event
def on_key_press(symbol, modifiers):
    # print(symbol)

    # D
    if symbol == 100:
        if protagonist.x == window.width - 50:
            pass
        else:
            protagonist.x += 50
    # W
    if symbol == 119:
        if protagonist.y == window.height - 50:
            pass
        else:
            protagonist.y += 50
    # A
    if symbol == 97:
        if protagonist.x == 0:
            pass
        else:
            protagonist.x -= 50
    # S
    if symbol == 115:
        if protagonist.y == 0:
            pass
        else:
            protagonist.y -= 50
    # R
    if symbol == 114:
        protagonist.x = 0
        protagonist.y = 0

    if symbol == 65307:
        window.close()


pyglet.app.run()