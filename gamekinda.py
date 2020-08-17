import pyglet
from pyglet import shapes
from random import randint
from time import sleep

window = pyglet.window.Window(width=500, height=500, visible=True)
window.set_caption("Blocky")
batch = pyglet.graphics.Batch()

coin = shapes.Circle(325, 25, 25, color=(255, 255, 22), batch=batch)
protagonist = shapes.Rectangle(0, 0, 50, 50, color=(255, 22, 255), batch=batch)

global scorenum
scorenum = 0
score = pyglet.text.Label(str(scorenum),
                          font_name="Arial",
                          font_size=36,
                          x=window.width / 2,
                          y=window.height - 20,
                          anchor_x='center',
                          anchor_y='center',
                          color=(255, 255, 255, 255),
                          batch=batch)


@window.event
def on_draw():
    if (protagonist.x + 25, protagonist.y + 25) == (coin.x, coin.y):
        global scorenum
        scorenum += 1
        score.text = str(scorenum)
        coinx = randint(1,10)
        coin.x = (coinx * 50) - 25

        coiny = randint(1, 10)
        coin.y = (coiny * 50) - 25

    if scorenum / 10 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        score.color = (0, 255, 0, 255)

    if scorenum / 10 not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        score.color = (255, 255, 255, 255)

    if scorenum == 0:
        score.color = (0, 0, 0, 0)

    window.clear()
    score.draw()
    batch.draw()


# window.on_key_press(pyglet.window.key.D)
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
