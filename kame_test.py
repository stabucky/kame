from kame import *

kame=Kame()

kame.setup(400,400,"red")
kaisu=2000
for i in range(kaisu):
  # kame.color(250-i*250/kaisu,i*250/kaisu,0)
  kame.color(250-i*250/kaisu,0,i*250/kaisu)
  kame.pendown()
  kame.forward(10*i)
  # kame.right(173)
  kame.right(179)
  kame.penup()
  kame.forward(5*i)
  kame.left(7*i/kaisu)
kame.kaku()