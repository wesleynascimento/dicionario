#!/usr/bin/env python

import matplotlib.pyplot as plt 
import numpy as np
import math

T={"Mercurio":0.241,"Venus":0.615,"Terra":1,"Marte":1.88,"Jupiter":11.86,"Saturno":29.5, "Urano":84.0, "Plutao":248.0}
R={"Mercurio":0.387,"Venus":0.723,"Terra":1,"Marte":1.523,"Jupiter":5.202,"Saturno":9.539, "Urano":19.18, "Plutao":39.44}

periodo=[t**2 for t in T.values()]
distancia=[d**3 for d in R.values()]



plt.figure(figsize=(8,5), dpi=96)
plt.axis([-1,20,-5,5])


ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.autoscale()
plt.xscale('log')
plt.yscale('log')
plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'$R^3$(UA)')
plt.ylabel(r'$T^2$ (anos)')

plt.title(r'Periodo $\times$ Semi-eixo', fontsize=12)
plt.plot(periodo,distancia, '-r')
plt.savefig("kpler.pdf", dpi=96)
