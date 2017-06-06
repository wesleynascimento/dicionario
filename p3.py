#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
import math

class Planeta:
	def __init__(self, nome, massa, x,y):
		self.nome=nome
		self.massa=massa
		self.x=x
		self.y=y
		
	def distancia(self):
		return math.sqrt(self.x**2+self.y**2)
	
	def forca(self):
		G=6.67408*10**(-11)
		ms=1.98892*10**(30)
		return ((G*ms*self.massa)/(self.distancia())**2)
	
	def periodo(self):
		return math.sqrt(self.distancia()**3)

	def operacao(self, outro):
		return math.sqrt((self.x-outro.x)**2+(self.y-outro.y)**2)
	
	
nome=raw_input('Informe o nome do planeta:\n')
nome1=raw_input('Informe o nome do planeta do segundo:\n')
massa=input('Informe a massa:\n')
massa1=input('Informe a massa do segundo:\n')
x=input('Informe a posição do primeiro em x:\n')		
y=input('Informe a posição do primeiro em y:\n')
x1=input('Informe a posição do segundo em x:\n')		
y1=input('Informe a posição do segundo em y:\n')


p=Planeta(nome, massa, x, y)
p1=Planeta(nome1,massa1,x1,y1)

print "Distância do Planeta ao Sol", p.distancia()
print "Força de Atração Gravitacional entre o Planetas e o Sol \n 1:", p.forca(),"\n2:",p1.forca()	
print "Período de oscilação do Planeta\n 1:", p.periodo(),"\n2:",p1.periodo()
print "Distancia entre os planetas:",p.operacao(p1)
