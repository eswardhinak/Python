a = float(input("A?"))
b = float(input("B?"))
c = float(input("C?"))
import math

e = ((-1*b + (math.sqrt((b**2) - 4*a*c)))/(2*a))
f = ((-1*b - (math.sqrt((b**2) - 4*a*c)))/(2*a))
print ("x = " + repr(e), repr(f))
input("Press<enter>")
