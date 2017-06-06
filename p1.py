#!/usr/bin/env python
import matplotlib.pyplot as plt 
import numpy as np
h=10**(-9)

class Derivada:
	def __init__(self,x,f):
		self.x=x
		self.f=f
		
	def derivada(self):
		if self.f=="seno":
			return((np.sin(self.x+h)-np.sin(self.x))/h)
		if self.f=="cosseno":
			return((np.cos(self.x+h)-np.cos(self.x))/h)	
			
x=input('x :\n')
funcao=raw_input('seno / cosseno?\n')
f1=Derivada(x,funcao)
print "Derivada de " ,funcao ,"no ponto " ,x," e :", f1.derivada()
