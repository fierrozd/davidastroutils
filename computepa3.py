import string as str
import numpy as np
from angles import *
import sys

#Code finds the SN-Galaxy offset and PA using ONE finder star at a time

galy = raw_input("Galaxy: ")
star = raw_input("  Star: ")
star_tar_ra = raw_input("E-W Offset from Star to target: ")
star_tar_dec= raw_input("N-S Offset from Star to target: ")

galy_ra, galy_dec = str.split(galy)
star_ra, star_dec = str.split(star)

galy_ra = float(galy_ra)
galy_dec= float(galy_dec)
star_ra = float(star_ra)
star_dec= float(star_dec)
star_tar_ra = float(star_tar_ra)
star_tar_dec= float(star_tar_dec)

star_tar_ra = arcs2d(star_tar_ra)
star_tar_dec= arcs2d(star_tar_dec)

a = AlphaAngle(d=galy_ra)
b = DeltaAngle(d=galy_dec)
c = AlphaAngle(d=star_ra)
d = DeltaAngle(d=star_dec)
e = AlphaAngle(d=star_tar_ra)
f = DeltaAngle(d=star_tar_dec)

print a
print b
print c
print d
print "----------"
print e
print f

ra_off = a-c-e
dec_off= b-d-f

print "----------"
print ra_off
print dec_off
print "----------"

ra_off = normalize(ra_off.arcs,-324000.0,324000.0)  #ra offset in deg, then normalize
#dec_off= normalize(dec_off.d,)
dec_off= dec_off.arcs

#separation = r2arcs(sep(d2r(ra1),d2r(dec1),d2r(ra2),d2r(dec2)))
#pa = r2d(bear(d2r(ra2),d2r(dec2),d2r(ra1),d2r(dec1)))
pa = r2d(bear(0,0,arcs2r(ra_off),arcs2r(dec_off)))

#print "sep: ", separation
print "pa:", pa
pa = normalize(pa,0,360)
print "pa:", pa
print "E",ra_off
print "N",dec_off

