###########compute area of circle   #############


class circle(object):
    def __init__(self,r):   # defining constructor in python
        self.radius=r
    def getter(self):
        print "radius of circle define in constructor is",self.radius
    def setter(self,R):
        self.rad=R
        print "radius of circle define by setter func is",self.rad
    def area_circle(self):
        area=3.14*self.radius*self.radius
        print "AREA OF CIRCLE IS",area
obj1=circle(10)
obj1.getter()
obj1.setter(20)
obj1.area_circle() 


############## COMPUTE AREA OF SQUARE ############################

class shape(object):
      def __init__(self):
          pass           # HERE PASS keyword simply come out of the constructor
                         # and do not print anything  
      def area(self):
          print "AREA OF SHAPE IS",0
class square(shape):
      def __init__(self,l):
          shape.__init__(self) #inheritance of constructor of shape class
          self.length=l
      def area(self):  #function overriding
          area_square=self.length*self.length
          print "AREA OF SQUARE IS",area_square
obj=shape()
obj.area()
obj1=square(15)
obj1.area()
