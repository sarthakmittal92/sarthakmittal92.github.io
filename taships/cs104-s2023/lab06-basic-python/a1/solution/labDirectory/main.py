'''
    Geometry (Complex and Polar)
'''
import math

# import the classes
from complex import Complex
from polar import Polar

def modulus(c:Complex):
    '''return modulus of the complex number'''
    return round(math.sqrt(c.x ** 2 + c.y ** 2),2)

def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    return round(math.atan2(c.y,c.x),2)

def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    return round(p.r * math.cos(p.t),2)

def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    return round(p.r * math.sin(p.t),2)

def toPolar(c:Complex):
    '''return polar representation of complex number'''
    return Polar(modulus(c),arg(c))

def toComplex(p:Polar):
    '''return complex number from polar'''
    return Complex(abscissa(p),ordinate(p))

def mult(a:Complex, b:Complex):
    '''multiply complex numbers'''
    p1 = toPolar(a)
    p2 = toPolar(b)
    return toComplex(p1 * p2)

def power(c:Complex, a:int):
    '''return complex number raised to power'''
    p = toPolar(c)
    return toComplex(p ** a)

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    return modulus(z1 - z2)

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    # print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)
