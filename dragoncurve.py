import turtle 
import sys


def applyRules(old):
    new = ""
    if old == 'X':
        new = 'X+YF+'   # Rule 1
    elif old == 'Y':
        new = '-FX-Y'  # Rule 2
    else:
        new = old    # no rules apply

    return new


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def generate(n, result='FX'):
    for _ in range(n):
        result = processString(result)

    return result

def draw(cmds, size=10):
    stack = []
    for cmd in cmds:
        if cmd=='F':
            turtle.forward(size)
        elif cmd=='-':
            turtle.left(90)
        elif cmd=='+':
            turtle.right(90)
        elif cmd=='X':
            pass
        elif cmd=='Y':
            pass
        else:
            raise ValueError('Unknown Cmd: {}'.format(ord(cmd)))
    turtle.update()

def setup():
    turtle.hideturtle()
    turtle.speed(1)
    turtle.tracer(1e3,0)
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()

setup()
curve = generate(10)
print(curve)
draw(curve)
turtle.exitonclick()
