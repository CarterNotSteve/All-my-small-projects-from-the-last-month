from appJar import gui

app = gui()


def reml():
    app.removeWidgetType("Label", "fjaasf")


def adden():
    x = app.getEntry("thing")
    tasks = []
    tasks.append(app.addLabel("fjaasf", x, column=1))
    app.addButton("Done", reml)


app.addLabelEntry("thing", 5, 1)
app.addButton("Add", adden)

app.go()
