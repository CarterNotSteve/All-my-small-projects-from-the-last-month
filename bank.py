from appJar import gui
import json

app = gui()

app.setTitle("Bank")


def submit():
    a = app.getEntry("amount")
    print(a)


def subDep():
    app.removeAllWidgets()
    app.addLabelEntry("amount", 1, 1, 0, 0, False, "Amount: ")
    app.addButton("submit", submit, 2, 1)


def signup():
    json.dumps({
        app.getEntry("accnum"): 0
    })


def login():
    if app.getEntry("accnum") in json.dumps():
        subDep()

    else:
        app.addLabel("warn", "Please enter a valid PIN")


def deposit():
    app.removeAllWidgets()
    app.addLabelEntry("accnum", 1, 1, 0, 0, True, "Account")
    app.addButton("login", login, 2, 1)
    app.addButton("signup", signup, 2, 1)


def withdraw():
    app.removeAllWidgets()


app.addButton("Deposit", deposit)

app.go()
