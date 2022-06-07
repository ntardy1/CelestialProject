
# Creating a working (and accurate) model of the Solar System

# Importing libraries
from vpython import *

# Disabling module messages from appearing in the command window
# insert code here

# Importing variables from solarSystemSetup
from solarSystemSetup import mercury
from solarSystemSetup import venus
from solarSystemSetup import earth
from solarSystemSetup import mars
from solarSystemSetup import jupiter
from solarSystemSetup import saturn
from solarSystemSetup import uranus
from solarSystemSetup import neptune
from solarSystemSetup import pluto

# Setting constants
G = 6.67*(10**-11) # Newtonian Gravitation Constant
sunMass = 1988500 * (10**24)

# Establishing planetary bodies and labels
# Labels are critical for viewing planet positions
Sun = sphere(pos=vec(0,0,0), radius=(1.39 * 10**6), color=color.yellow)
sunLabel = label(pos=Sun.pos, text='Sun', yoffset=10, height=10, font='Calibri')

planetMercury = sphere(pos=vec(float(mercury.DistancefromSun) * (10**6),0,0), radius=float(mercury.Diameter)/2)
planetMercuryLabel = label(pos=planetMercury.pos, text='Mercury', yoffset=10, height=10, font='Calibri')

planetVenus = sphere(pos=vec(float(venus.DistancefromSun) * (10**6),0,0), radius=float(venus.Diameter)/2)
planetVenusLabel = label(pos=planetVenus.pos, text='Venus', yoffset=10, height=10, font='Calibri')

planetEarth = sphere(pos=vec(float(earth.DistancefromSun) * (10**6),0,0), radius=float(earth.Diameter)/2, make_trail = True)
planetEarthLabel = label(pos=planetEarth.pos, text='Earth', yoffset=10, height=10, font='Calibri')

planetMars = sphere(pos=vec(float(mars.DistancefromSun) * (10**6),0,0), radius=float(mars.Diameter)/2)
planetMarsLabel = label(pos=planetMars.pos, text='Mars', yoffset=10, height=10, font='Calibri')

planetJupiter = sphere(pos=vec(float(jupiter.DistancefromSun) * (10**6),0,0), radius=float(jupiter.Diameter)/2)
planetJupiterLabel = label(pos=planetJupiter.pos, text='Jupiter', yoffset=10, height=10, font='Calibri')

planetSaturn = sphere(pos=vec(float(saturn.DistancefromSun) * (10**6),0,0), radius=float(saturn.Diameter)/2)
planetSaturnLabel = label(pos=planetSaturn.pos, text='Saturn', yoffset=10, height=10, font='Calibri')

planetUranus = sphere(pos=vec(float(uranus.DistancefromSun) * (10**6),0,0), radius=float(uranus.Diameter)/2)
planetUranusLabel = label(pos=planetUranus.pos, text='Uranus', yoffset=10, height=10, font='Calibri')

planetNeptune = sphere(pos=vec(float(neptune.DistancefromSun) * (10**6),0,0), radius=float(neptune.Diameter)/2)
planetNeptuneLabel = label(pos=planetNeptune.pos, text='Neptune', yoffset=10, height=10, font='Calibri')

dwarfPlanetPluto = sphere(pos=vec(float(pluto.DistancefromSun) * (10**6),0,0), radius=float(pluto.Diameter)/2)
dwarfPlanetPlutoLabel = label(pos=dwarfPlanetPluto.pos, text='Pluto', yoffset=10, height=10, font='Calibri')

# Establishing planetary momentums
# This will become important for using the Gravitational Force to create rotation
earthMomentum = vec(0,float(earth.OrbitalVelocity * earth.Mass),0) # currently dealing with OverFlow Error w/ mass

delta_t = 1
while True:
    rate(525600) # number of seconds in a 60th of a year, so that the simulation will run a year worth of movements in a minute (I.R.L)
    r = planetEarth.pos - Sun.pos
    earthGravityForce =  (G * earth.Mass * sunMass)/((mag(r) * (10**6))**2)
    earthMomentum = mag(earthMomentum) + earthGravityForce * delta_t
    planetEarth.pos = planetEarth.pos + (mag(earthMomentum)/earth.Mass) * delta_t
    planetEarthLabel = planetEarth.pos

