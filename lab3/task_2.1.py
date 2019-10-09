from graph import *
from abc import abstractmethod



class Picture:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        penSize(0)

    @abstractmethod
    def print(self):
        pass

class Sun(Picture):
    def print(self):
        brushColor("yellow")
        circle(self.x, self.y, self.scale)


class Tree(Picture):
    def print(self):
        brushColor('white')
        rectangle(self.x - self.scale / 7, self.y + self.scale / 0.55,
                  self.x + self.scale / 7, self.y + self.scale / 2)
        brushColor('green')
        oval(self.x, self.y, self.scale, self.scale/2)
        oval(self.x, self.y - self.scale/1.5, self.scale/1.8, self.scale/1.4)
        oval(self.x, self.y + self.scale/1.5, self.scale/1.8, self.scale/2.3)
        brushColor('red')
        circle(self.x + self.scale/4, self.y - self.scale/1, self.scale/8)
        circle(self.x + self.scale/1.3, self.y + self.scale/30, self.scale/8)
        circle(self.x - self.scale/1.3, self.y - self.scale/30, self.scale/8)
        circle(self.x + self.scale / 4, self.y + self.scale/1.2, self.scale/8)

class Unicorn(Picture):
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scalex = scale
        self.scaley = scale
        self.scale = scale
        self.xh = x
        self.yh = y
        penSize(0)

    def reverse_X(self):
        self.scalex = -self.scalex

    def reverse_Y(self):
        self.scaley = -self.scaley

    def hair(self, x, y, xs, ys):
        if xs%2 == 0 and ys%2==0:
            brushColor("#E883E0")
        elif xs%2 != 0 and ys%2==0:
            brushColor("#F7DF74")
        elif xs%2 == 0 and ys%2 != 0:
            brushColor("#77F4ED")
        else:
            brushColor("#9D7ED9")

        a = 0.015
        b = 0.01
        oval(self.xh + x*b*self.scalex , self.yh - y*b*self.scaley,
             xs*a*self.scalex, ys*a*self.scaley)

    def main(self):
        self.hair(69, 123, 12, 6)
        self.hair(62, 115, 13, 6)
        self.hair(33, 66, 10, 6)
        self.hair(45, 60, 13, 7)
        self.hair(55, 70, 12, 6)
        self.hair(56, 90, 10, 8)
        self.hair(35, 85, 12, 5)
        self.hair(45, 80, 13, 6)
        self.hair(55, 100, 13, 7)
        self.hair(55, 107, 12, 6)
        self.hair(43, 91, 11, 5)
        self.hair(43, 70, 13, 6)
        self.hair(59, 75, 12, 7)
        self.hair(30, 75, 12, 7)
        self.hair(53, 80, 12, 6)

    def tail(self):
        self.xh = self.x - 1.5*self.scalex
        self.yh = self.y + 0.9*self.scaley
        self.main()

    def print(self):
        brushColor("white")
        oval(self.x, self.y, self.scale, self.scale/2)
        rectangle(self.x - self.scalex/1.1, self.y+self.scaley/0.9,
                  self.x - self.scalex/1.3, self.y)
        rectangle(self.x - self.scalex / 2, self.y + self.scaley,
                  self.x - self.scalex / 3, self.y)
        rectangle(self.x + self.scalex / 1.4, self.y + self.scaley/1.1,
                  self.x + self.scalex / 1.2, self.y)
        rectangle(self.x + self.scalex / 2.38, self.y + self.scaley/0.8,
                  self.x + self.scalex / 1.8, self.y)
        circle(self.x + self.scalex*0.81, self.y - self.scaley,  self.scale*0.25)
        penColor('white')
        polygon([(self.x + self.scalex*0.1, self.y - self.scaley*0.27),
                (self.x + self.scalex*0.55, self.y - self.scaley),
                (self.x + self.scalex*0.9, self.y - self.scaley*0.9),
                (self.x + self.scalex*0.9, self.y)])
        oval(self.x + self.scalex*1, self.y - self.scaley*0.89,
             self.scale*0.25, self.scale/8)
        brushColor("purple")
        circle(self.x + self.scalex*0.95, self.y - self.scaley*1.03, self.scale*0.07)
        brushColor("black")
        circle(self.x + self.scalex*0.97, self.y - self.scaley*1.03, self.scale*0.03)
        brushColor("white")
        oval(self.x + self.scalex*0.935, self.y - self.scaley*1.05, self.scalex*0.04,self.scaley*0.015)

        brushColor("pink")
        polygon([(self.x + self.scalex * 0.7, self.y - self.scaley * 1.2),
                 (self.x + self.scalex * 0.87, self.y - self.scaley * 1.2),
                 (self.x + self.scalex * 0.83, self.y - self.scaley * 1.7)])

        self.main()
        self.tail()




windowSize(794,1123)
canvasSize(794,1123)
brushColor(0,255,255)
rectangle(0,500,794,0)
brushColor('#7FFF00')
rectangle(0,1123,794,499)

a = Tree(130,400,150)
a.print()

a = Sun(770,100,200)
a.print()

a = Unicorn(500, 700, 150)
a.print()

run()





