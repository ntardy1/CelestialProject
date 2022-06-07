
# Reading the CSV of Solar System Data

# Importing Libraries
import csv
import math

from numpy import long

# Declaring necessary variables
data = []
allLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Opening the CSV file and reading its data
file = open(r"C:\Users\laten\Desktop\Projects\Python\STEMProject\planetData.csv")
csv_read = csv.reader(file)

# In order to work with the CSV data, turn it into nested lists
# This turns data into a list of lists
for element in csv_read:
    data.append(element)

labels = data[0]
data = data[1:len(data)]

class createBodies:
    def __init__(self, list):
        self.name = list[0]
        for elem in labels:
            for char in elem:
                if all(char != letter for letter in allLetters):
                    newElem = elem[0:elem.index(char)]
                    break
                else:
                    newElem = elem
            setattr(self, newElem, list[labels.index(elem)])


# If I get the chance, turn the stuff below into a loop (although, it does currently work)

mercury = createBodies(data[0])
venus = createBodies(data[1])
earth = createBodies(data[2])
mars = createBodies(data[3])
jupiter = createBodies(data[4])
saturn = createBodies(data[5])
uranus = createBodies(data[6])
neptune = createBodies(data[7])
pluto = createBodies(data[8])

# Correcting planetary masses
mercury.Mass = mercury.Mass * (10**24)
venus.Mass = venus.Mass * (10**24)
earth.Mass = earth.Mass * (10**24)
mars.Mass = mars.Mass * (10**24)
jupiter.Mass = jupiter.Mass * (10**24)
saturn.Mass = saturn.Mass * (10**24)
uranus.Mass = uranus.Mass * (10**24)
neptune.Mass = neptune.Mass * (10**24)
pluto.Mass = pluto.Mass * (10**24)

# Correcting orbital velocities (geting them to units of m/s instead of km/s)
mercury.OrbitalVelocity = mercury.OrbitalVelocity * 1000
venus.OrbitalVelocity = venus.OrbitalVelocity * 1000
earth.OrbitalVelocity = earth.OrbitalVelocity * 1000
mars.OrbitalVelocity = mars.OrbitalVelocity * 1000
jupiter.OrbitalVelocity = jupiter.OrbitalVelocity * 1000
saturn.OrbitalVelocity = saturn.OrbitalVelocity * 1000
uranus.OrbitalVelocity = uranus.OrbitalVelocity * 1000
neptune.OrbitalVelocity = neptune.OrbitalVelocity * 1000
pluto.OrbitalVelocity = pluto.OrbitalVelocity * 1000


'''
if all(x not in mystr for x in mylist):
    print mystr

'''


