from graph import *
from abc import ABC, abstractmethod



class Picture:
    def __init__(self, ref_point_x, ref_point_y, scale):
        self.ref_point_x = ref_point_x
        self.ref_point_y = ref_point_y
        self.scale = scale
        penSize(0)

    @abstractmethod
    def print(self):
        pass

class Sun(Picture):
    def print(self):
        brushColor("yellow")
        circle(self.ref_point_x, self.ref_point_y, self.scale)

class Tree(Picture):
    def print(self):
        brushColor('white')
        rectangle(self.ref_point_x - self.scale / 7, self.ref_point_y + self.scale / 0.55,
                  self.ref_point_x + self.scale / 7, self.ref_point_y + self.scale / 2)
        brushColor('green')
        oval(self.ref_point_x, self.ref_point_y, self.scale, self.scale/2)
        oval(self.ref_point_x, self.ref_point_y - self.scale/1.5, self.scale/1.8, self.scale/1.4)
        oval(self.ref_point_x, self.ref_point_y + self.scale/1.5, self.scale/1.8, self.scale/2.3)
        brushColor('red')
        circle(self.ref_point_x + self.scale/4, self.ref_point_y - self.scale/1, self.scale/8)
        circle(self.ref_point_x + self.scale/1.3, self.ref_point_y + self.scale/30, self.scale/8)
        circle(self.ref_point_x - self.scale/1.3, self.ref_point_y - self.scale/30, self.scale/8)
        circle(self.ref_point_x + self.scale / 4, self.ref_point_y + self.scale/1.2, self.scale/8)

class Unicorn(Picture):
    def hair(self):
        brushColor("black")
        a = 0.75
        b = 1
        x_bias = self.ref_point_x + a*self.scale
        y_bias = self.ref_point_y - b*self.scale
        for i in range(5):
            oval(x_bias,y_bias, self.scale/8, self.scale/10)
            x_bias -= a/5*self.scale
            y_bias += b/5*self.scale


    def print(self):
        brushColor("white")
        oval(self.ref_point_x, self.ref_point_y, self.scale, self.scale/2)
        rectangle(self.ref_point_x - self.scale/1.1, self.ref_point_y+self.scale/0.9,
                  self.ref_point_x - self.scale/1.3, self.ref_point_y)
        rectangle(self.ref_point_x - self.scale / 2, self.ref_point_y + self.scale,
                  self.ref_point_x - self.scale / 3, self.ref_point_y)
        rectangle(self.ref_point_x + self.scale / 1.4, self.ref_point_y + self.scale/1.1,
                  self.ref_point_x + self.scale / 1.2, self.ref_point_y)
        rectangle(self.ref_point_x + self.scale / 2.38, self.ref_point_y + self.scale/0.8,
                  self.ref_point_x + self.scale / 1.8, self.ref_point_y)
        circle(self.ref_point_x + self.scale*0.81, self.ref_point_y - self.scale,  self.scale*0.25)
        penColor('white')
        polygon([(self.ref_point_x + self.scale*0.1, self.ref_point_y - self.scale*0.27),
                (self.ref_point_x + self.scale*0.55, self.ref_point_y - self.scale),
                (self.ref_point_x + self.scale*0.9, self.ref_point_y - self.scale*0.9),
                (self.ref_point_x + self.scale*0.9, self.ref_point_y)])
        oval(self.ref_point_x + self.scale*1, self.ref_point_y - self.scale*0.89,
             self.scale*0.25, self.scale/8)
        self.hair()



windowSize(794,1123)
canvasSize(794,1123)
brushColor('blue')
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





