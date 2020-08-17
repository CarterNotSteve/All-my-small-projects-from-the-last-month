from appJar import gui
from time import sleep

app = gui()

app.setBg("lightBlue")

global pts
pts = 0
auto = 0


global upgrade_level
global base_amt
upgrade_level = 1
base_amt = 1


def ptsadd():
    global pts
    pts = pts + (base_amt * upgrade_level)
    app.setLabel("score", pts)


def purchase():
    global pts
    if pts > 20:
        pts = pts - 20
        global upgrade_level
        upgrade_level += 1

    if pts < 20:
        app.setLabelBg("warn", "red")
        app.setLabel("warn", "You don't have enough for that. You need 20.")
        sleep(2)
        app.setLabelBg("warn", "red")
        app.setLabel("warn", "")


app.addLabel("warn", "", 1, 2)
app.addButton("Click", ptsadd, 3, 2)
app.addButton("Upgrade (20)", purchase, 4, 2)

app.addLabel("score", pts, 2, 2)





app.go()