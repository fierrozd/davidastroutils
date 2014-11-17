import sys,os
import numpy as np
from angles import *

if len(sys.argv)<2:
    print "only argument: sextractor file name"
    sys.exit()
inname=sys.argv[1]
outname=open(inname+'.reg','w')

headercount,xcol,ycol,flux=0,None,None,None
f=open (inname,'r')
for l in f:  #find which column the coordinates are in
    if l.startswith('#'):
        if 'X_IMAGE' in l:
            xcol=int(l.split()[1])
        if 'Y_IMAGE' in l:
            ycol=int(l.split()[1])
        if 'ALPHA_SKY' in l:
            racol=int(l.split()[1])
        if 'DELTA_SKY' in l:
            decol=int(l.split()[1])
        if 'FLUX_AUTO' in l:
            flux=int(l.split()[1])
        headercount+=1
    else : break

posn = str(sys.argv[2])+' '+str(sys.argv[3])
ra1, dec1 = pposition(posn)
ra1 = h2d(ra1)
print "* Near: %s %s"%(ra1,dec1)

outname.write('''# Region file format: DS9 version 4.1                                            
                                               
global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1                                                
                                                          
image
''')

if flux:   #if flux exists
    cat = np.loadtxt(inname,skiprows=headercount, usecols=(xcol-1,ycol-1,flux-1,racol-1,decol-1))
    color=['yellow','green','blue','red']

    dis1= cat[:,0]  #xcol
    dis2= cat[:,1]  #ycol
    dist1= np.hypot(np.abs(dis1-248), np.abs(dis2-248))

#    ra1 = 22:31:50.812
#    dec1= -06:46:46.50
#   ra1 = 337.9827614
#   dec1= -6.7969411492
    dist2=[]

    for coord in cat:
        ra2  = coord[3] #racol
        dec2 = coord[4] #decol
        dist2.append(r2arcs(sep(d2r(ra1),d2r(dec1),d2r(ra2),d2r(dec2))))

    j = np.argsort(dist2)  #sort by coord distance
#   k = np.argsort(dist1)  #sort by image distance
#   l = np.argsort(cat.T)  #sort by flux column k[2]
#   print cat[j][:3]           #array sorted by coord distance, top 3
#   print cat[k[2]][::-1][:3]  #array sorted by image distance, descending, top 3

    i = 1
    for star in cat[j][:3]:
        print "Star %i: %s %s"%(i,star[3],star[4])
        print >> outname, "circle(%.3f,%.3f,%.3f) # text = {%i} color = %s"%(star[0],star[1],5,i,color[i])
        i += 1
else:     #if flux doesnt exist
    cat=np.loadtxt(inname,skiprows=headercount, usecols=(xcol-1,ycol-1))
    for star in cat:
        print >> outname,"circle(%.3f,%.3f,%.3f)"%(star[0],star[1],20)



