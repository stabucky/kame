from PIL import Image, ImageDraw, ImageFont
import math

class Kame:
  haba = 500
  takasa = 300
  ichi = (haba // 2, takasa // 2)
  muki = 0
  pen_flag = True
  pen_rgb = (0, 0, 0)
  im = Image.new('RGB', (haba, takasa), "silver")
  draw = ImageDraw.Draw(im)

  def setup(self, width, height, color):
    self.im = Image.new('RGB', (width, height), color)
    self.draw = ImageDraw.Draw(self.im)
    self.haba = width
    self.takasa = height
    self.ichi = (self.haba // 2, self.takasa // 2)

  def kaku(self):
    self.im.show()

  def forward(self, nagasa):
    rad = math.radians(-self.muki)
    x0, y0 = self.ichi
    x1 = x0 + math.cos(rad) * nagasa
    y1 = y0 + math.sin(rad) * nagasa
    self.ichi = (x1, y1)
    if self.pen_flag:
      self.draw.line((x0, y0, x1, y1), fill=self.pen_rgb, width=1)

  def goto(self, x, y):
    x0, y0 = self.ichi
    self.ichi = [x, y]
    if self.pen_flag:
      self.draw.line((x0, y0, x, y), fill=self.pen_rgb, width=1)

  def color(self, r, g, b):
    self.pen_rgb = (int(r), int(g), int(b))

  def right(self, kakudo):
    self.muki -= kakudo

  def left(self, kakudo):
    self.muki += kakudo

  def penup(self):
    self.pen_flag = False

  def pendown(self):
    self.pen_flag = True
