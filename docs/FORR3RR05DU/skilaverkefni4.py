from math import *

class Vigur:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def prenta(self):
        print( 'A = [ %s %s ]' %( self.x,self.y ) )

    def lengd(self):
        return sqrt( self.x**2 + self.y**2 )
    
    def stefnuhorn( self ):
        if self.y < 0:
            return -degrees( acos( self.x / self.lengd() ) )
        else:
            return degrees( acos( self.x / self.lengd() ) )

a = Vigur(1,-2) # breyta í input option
a.prenta()

print(a.lengd(), 'lengd \n')

print(a.stefnuhorn(), 'stefnuhorn \n')