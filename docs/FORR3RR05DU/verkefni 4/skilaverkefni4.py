from math import *

class Vigur:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def prenta( self ):
        print( 'A = [ %s %s ]' %( self.x,self.y ) )

    def lengd( self ):
        return sqrt( self.x**2 + self.y**2 )
    
    def stefnuhorn( self ):
        if self.y < 0:
            return -degrees( acos( self.x / self.lengd() ) )
        else:
            return degrees( acos( self.x / self.lengd() ) )

    # Fall sem skilar þvervigri
    def þvervigur( self ):
        return Vigur( -self.y, self.x )

    # Fall sem skilar hallatölu
    def halli( self ):
        if self.y == 0 or self.x == 0:
            print( 'Þú getur ekki deild 0' )
        else:
            return self.y / self.x

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn( self,v ):
        innfelldi = self.x * v.x + self.y * v.y
        return round( degrees( acos( (innfelldi / ( self.lengd() * v.lengd() ) ) ) ), 1 )

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return self.x + v.x * self.y + v.y


inpx = int( input( 'hvað er x fyrir fyrsta vigur ' ) )
inpy = int( input( 'hvað er y fyrir fyrsta vigur ' ) )

inpx1 = int( input( 'hvað er x fyrir seinni vigur ' ) )
inpy1 = int( input( 'hvað er y fyrir seinni vigur ' ) )

# a = Vigur(inpx,inpy)
v1 = Vigur( inpx, inpy ) # breyta í input option
v1.prenta()
print( 'Lengd: ', v1.lengd() )
print( 'Halli: ', v1.halli() )
vþ = v1.þvervigur()
print( 'þvervigur: ', end=' ' )
vþ.prenta()
print( 'stefnuhorn: ', v1.stefnuhorn() )
v2 = Vigur( inpx1, inpy1 )
print( 'Horn milli vigra: ', v2.horn( v1 ) )
v3 = v1.summa( v2 )
print( 'Summa: ', end = ' ' )
v3.prenta()
