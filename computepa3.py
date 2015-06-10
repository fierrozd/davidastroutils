import string as str
import numpy as np
from angles import *
import sys

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

star_tar_ra = star_tar_ra/3600.
star_tar_dec= star_tar_dec/3600.

ra_off = (star_tar_ra+star_ra-galy_ra)*np.cos(galy_dec/180.*np.pi)*3600.  #Galaxy--> SN Offset
dec_off= (star_tar_dec+star_dec-galy_dec)*3600.          #Galaxy--> SN Offset

#pa = r2d(bear(d2r(ra2),d2r(dec2),d2r(ra1),d2r(dec1)))
pa = r2d(bear(0,0,arcs2r(ra_off),arcs2r(dec_off)))

#print "sep: ", separation
print "pa:", pa
pa = normalize(pa,0,360)
print "pa:", pa
print "E",ra_off
print "N",dec_off
