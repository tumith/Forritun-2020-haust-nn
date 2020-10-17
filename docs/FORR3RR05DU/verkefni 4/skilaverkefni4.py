from math import *
import re

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
        return Vigur( self.x + v.x, self.y + v.y )


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



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2

inpm = str( input( 'Marglida: ' ) )
marglida = inpm

listi = []
lidir = re.split( '[+-]', marglida )

for i in lidir:
    listi.append(i)
    print( i )
    

print(listi)

N = int( input( 'Enter how many times you want to sum (more times = more accurate)' ) )
a = float( input( 'Enter the lower integration bound: ' ) )
b = float( input( 'Enter the upper integration bound: ' ) )

def Integrate( N, a, b ):
    def f(x):
        # type your function after return
        return x^2
    val = 0
    val2 = 0
    for n in range( 1, N + 1 ):
        val += f( a + ( ( n - ( 1 / 2 ) ) * ( ( b - a ) / N ) ) )
    val2 = ( ( b - a ) / N ) * val
    return val2

# Output including  the integration value:
print( '......................................' )
print( 'Here is your answer: ' )
print( Integrate( N, a, b ) )

for i in lidir:
    full_split = re.split( '[x]', i )
    print( full_split )
    x = 0
    while x != 1:
        if listi[ x ] == '':
            print( 'x^' )
        x = x + 1