import re

def calcNeededSurface(l, w, h):
    sides = [l*w, w*h, h*l]
    extra = min(sides)
    return 2*sides[0] + 2*sides[1] + 2*sides[2] + extra

def loadSizes():
    f = open('input.txt')
    for l in f:
        first_x = l.find('x')
        sec_x = l.find('x', first_x+1)
        l, w, h = int(l[:first_x]), int(l[first_x+1:sec_x]), int(l[sec_x+1:])
        yield l, w, h

def calcSum():
    sum = 0
    for l, w, h in loadSizes():
        sum += calcNeededSurface(l, w, h)
    return sum

def calcRibon():
    sum = 0
    for l, w, h in loadSizes():
        sum += min([2*l+2*w, 2*l+2*h, 2*w+2*h]) + l*w*h
    return sum

#print calcNeededSurface(2,3,4)
print calcSum()
print calcRibon()
