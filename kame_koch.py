from kame import *
# import kame

def koch(length, depth):
  if depth == 0:
    kame.forward(length)
  else:
    koch(length / 3, depth - 1)
    kame.left(60)
    koch(length / 3, depth - 1)
    kame.right(120)
    koch(length / 3, depth - 1)
    kame.left(60)
    koch(length / 3, depth - 1)

kame=Kame()
kame.setup(400,400,"white")

kame.penup()
kame.goto(125,375)
kame.pendown()

length = 150
depth=8
for i in range(0,8):
  koch(length, depth)
  kame.left(45)

kame.kaku()
