import math


def Rectangular_Prism():
    global SA
    w = float(eval(input("What's the width\n")))
    l = float(eval(input("What's the length\n")))
    h = float(eval(input("What's the height\n")))
    HWSide = h * w
    WLSide = w * l
    LHSide = l * h
    SA = (HWSide + WLSide + LHSide) * 2
def Triangular_Prism():
    global SA
    l = float(eval(input("What's the length\n")))
    h = float(eval(input("What's the height\n")))
    b = float(eval(input("What's the base\n")))
    s2 = float(eval(input("What's another side of the triangle\n")))
    s3 = float(eval(input("What's a third side of the triangle\n")))
    SA = (b * h) + (l * (b + s2 + s3))


def Cylinder():
    global SA
    global SApi
    h = float(eval(input("What's the height\n")))
    r = float(eval(input("Whats the radius\n")))
    SApi = str(2 * math.pi * r * (r + h))
    SA = str(2 * r * (r + h))


def Trapezoidal_Prism():
    global SA
    a = float(eval(input("What is the left side of the trapezoid\n")))
    b1 = float(eval(input("What is the top side of the trapezoid\n")))
    c = float(eval(input("What is the right side of the trapezoid\n")))
    b2 = float(eval(input("What is the bottom side of the trapezoid\n")))
    h = float(eval(input("What's the height of the trapezoid\n")))
    p = a + b1 + c + b2
    l = float(eval(input("What's the length of the prism\n")))
    SA = ((b1 + b2) * h + p * l)


def Sphere():
    global SA
    global SApi
    r = float(eval(input("What's the radius\n")))
    SA = str(r**2 * 4)
    SApi = str(math.pi * 4 * r**2)


def Pyramid():
  global SA
  w = float(eval(input("What's the width\n")))
  l = float(eval(input("What's the length\n")))
  h = float(eval(input("What's the height\n")))
  SA = l*w+l*math.sqrt((w/2)**2+h**2)+w*math.sqrt((l/2)**2+h**2)


while True:
    Shape = input("What's the Shape\n").lower()
    if (Shape == "cube"):
        Rectangular_Prism()
    elif (Shape == "cylinder"):
      Cylinder()
    elif (Shape == "trapezoid"):
        Trapezoidal_Prism()
    elif (Shape == "sphere"):
        Sphere()
    elif (Shape == "pyramid"):
      Pyramid()
    else:
        exit()
    if (Shape == "cylinder" or Shape == "sphere"):
        print(SA + 'π -> ' + SApi)
    else:
        print(SA)
    continued = input("")
    if continued == "exit":
        exit()
