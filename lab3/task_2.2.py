from graph import *
from abc import abstractmethod

class Picture:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scalex = scale
        self.scaley = scale
        penSize(0)

    def changeSO(self, a, b):
        self.scalex = a*self.scalex
        self.scaley = b*self.scaley

    def changeXYS(self,x,y,scalex,scaley):
        self.x = x
        self.y = y
        self.scalex = scalex
        self.scaley = scaley

    def reverse_X(self):
        self.scalex = -self.scalex

    def reverse_Y(self):
        self.scaley = -self.scaley

    def deform_X(self, k):
        self.scalex = k * self.scalex

    def deform_Y(self, k):
        self.scaley = k * self.scaley

    @abstractmethod
    def print(self):
        pass

class BrightSun(Picture):
    def print(self):
        for i in range(127):
            brushColor(i*2, 255, 254 -i*2)
            circle(self.x,self.y,129-i)

class Tree(Picture):
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scalex = scale
        self.scaley = scale
        penSize(scale * 0.018)
        penColor('#2AF107')

    def __apples(self):
        brushColor('red')
        oval(self.x + self.scalex/4, self.y - self.scaley/1, self.scalex/8, self.scaley/8)
        oval(self.x + self.scalex/1.3, self.y + self.scaley/30, self.scalex/8, self.scaley/8)
        oval(self.x - self.scalex/1.3, self.y - self.scaley/30, self.scalex/8, self.scaley/8)
        oval(self.x + self.scalex/4, self.y + self.scaley/1.2, self.scalex/8, self.scaley/8)

    def __leafage(self):
        brushColor('green')
        oval(self.x, self.y - self.scaley/1.5, self.scalex/1.8, self.scaley/1.4)
        oval(self.x, self.y, self.scalex, self.scaley/2)
        oval(self.x, self.y + self.scaley/1.5, self.scalex/1.8, self.scaley/2.3)

    def __trunk(self):
        brushColor('white')
        rectangle(self.x - self.scalex/7, self.y + self.scaley/0.55,
                  self.x + self.scalex/7, self.y + self.scaley/2)

    def print(self):
        self.__trunk()
        self.__leafage()
        self.__apples()

class Unicorn(Picture):
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scalex = scale
        self.scaley = scale
        self.xh = x
        self.yh = y
        penSize(0)

    def __hair(self, x, y, xs, ys):
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

    def __main(self):
        self.__hair(69, 123, 12, 6)
        self.__hair(62, 115, 13, 6)
        self.__hair(33, 66, 10, 6)
        self.__hair(45, 60, 13, 7)
        self.__hair(55, 70, 12, 6)
        self.__hair(56, 90, 10, 8)
        self.__hair(35, 85, 12, 5)
        self.__hair(45, 80, 13, 6)
        self.__hair(55, 100, 13, 7)
        self.__hair(55, 107, 12, 6)
        self.__hair(43, 91, 11, 5)
        self.__hair(43, 70, 13, 6)
        self.__hair(59, 75, 12, 7)
        self.__hair(30, 75, 12, 7)
        self.__hair(53, 80, 12, 6)

    def __allhair(self):
        self.xh = self.x
        self.yh = self.y
        self.__main()
        self.xh = self.x - 1.5*self.scalex
        self.yh = self.y + 0.9*self.scaley
        self.__main()

    def __body(self):
        brushColor("white")
        penColor('white')
        oval(self.x, self.y, self.scalex, self.scaley / 2)
        rectangle(self.x - self.scalex / 1.1, self.y + self.scaley / 0.9,
                  self.x - self.scalex / 1.3, self.y)
        rectangle(self.x - self.scalex / 2, self.y + self.scaley,
                  self.x - self.scalex / 3, self.y)
        rectangle(self.x + self.scalex / 1.4, self.y + self.scaley / 1.1,
                  self.x + self.scalex / 1.2, self.y)
        rectangle(self.x + self.scalex / 2.38, self.y + self.scaley / 0.8,
                  self.x + self.scalex / 1.8, self.y)
        oval(self.x + self.scalex * 0.81, self.y - self.scaley, self.scalex * 0.25, self.scaley * 0.25)
        polygon([(self.x + self.scalex * 0.1, self.y - self.scaley * 0.27),
                 (self.x + self.scalex * 0.55, self.y - self.scaley),
                 (self.x + self.scalex * 0.9, self.y - self.scaley * 0.9),
                 (self.x + self.scalex * 0.9, self.y)])
        oval(self.x + self.scalex * 1, self.y - self.scaley * 0.89,
             self.scalex * 0.25, self.scaley / 8)

    def __eye(self):
        brushColor("purple")
        oval(self.x + self.scalex * 0.95, self.y - self.scaley * 1.03, self.scalex * 0.07, self.scaley * 0.07)
        brushColor("black")
        oval(self.x + self.scalex * 0.97, self.y - self.scaley * 1.03, self.scalex * 0.03, self.scaley * 0.03)
        brushColor("white")
        oval(self.x + self.scalex * 0.935, self.y - self.scaley * 1.05, self.scalex * 0.04, self.scaley * 0.015)

    def __horn(self):
        brushColor("pink")
        polygon([(self.x + self.scalex * 0.7, self.y - self.scaley * 1.2),
                 (self.x + self.scalex * 0.87, self.y - self.scaley * 1.2),
                 (self.x + self.scalex * 0.83, self.y - self.scaley * 1.7)])

    def print(self):
        self.__body()
        self.__horn()
        self.__eye()
        self.__allhair()

windowSize(794,1123)
canvasSize(794,1123)
brushColor(0,255,255)
rectangle(0,500,794,0)
brushColor('#2AF107')
rectangle(0,1123,794,499)

a = BrightSun(600,200,200)
a.print()

a = Tree(220,280,200)
a.print()
a.changeXYS(80,400,100,200)
a.print()
a.changeXYS(360,500,200,100)
a.print()
a.changeXYS(200,620,150,150)
a.print()
a.changeXYS(120,800,150,150)
a.print()

a = Unicorn(410, 870, 110)
a.print()
a.changeXYS(700, 750, -80, 80)
a.print()
a.changeXYS(550,570,60,60)
a.print()
a.changeXYS(740,500,-30,30)
a.print()

run()