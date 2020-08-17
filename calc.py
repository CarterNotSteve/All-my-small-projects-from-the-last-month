from appJar import gui

app = gui()

nums = []

global clearon
clearon = 0

def equl():
    nums.append((app.getLabel("inter")))
    equation = "".join(nums)
    nums.clear()
    app.setLabel("inter", eval(equation))
    global clearon
    clearon = 1


def one():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "1")


def two():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "2")


def three():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "3")


def four():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "4")


def five():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "5")


def six():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "6")


def seven():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "7")


def eight():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "8")


def nine():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "9")


def zero():
    global clearon
    if clearon == 1:
        app.setLabel("inter", "")
        clearon = 0
    app.setLabel("inter", app.getLabel("inter") + "0")


def add():
    nums.append((app.getLabel("inter")))
    nums.append("+")
    app.setLabel("inter", "")


def sub():
    nums.append((app.getLabel("inter")))
    nums.append("-")
    app.setLabel("inter", "")


app.addLabel("inter", "", 0, 2)
app.addButton("1", one, 1, 1)
app.addButton("2", two, 1, 2)
app.addButton("3", three, 1, 3)
app.addButton("4", four, 2, 1)
app.addButton("5", five, 2, 2)
app.addButton("6", six, 2, 3)
app.addButton("7", seven, 3, 1)
app.addButton("8", eight, 3, 2)
app.addButton("9", nine, 3, 3)
app.addButton("0", zero, 4, 2)
app.addButton("+", add, 4, 3)
app.addButton("-", sub, 4, 1)
app.addButton("=", equl, 5, 1, 3, 1)








app.go()