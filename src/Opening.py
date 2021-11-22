# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
	# Constructor
	def __init__(self, parameters = {}) :  
		# Parameters
		# position: mandatory
		# width: mandatory
		# height: mandatory
		# thickness: mandatory
		# color: mandatory        

		# Sets the parameters
		self.parameters = parameters

		# Sets the default parameters 
		if 'position' not in self.parameters:
			raise Exception('Parameter "position" required.')       
		if 'width' not in self.parameters:
			raise Exception('Parameter "width" required.')
		if 'height' not in self.parameters:
			raise Exception('Parameter "height" required.')
		if 'thickness' not in self.parameters:
			raise Exception('Parameter "thickness" required.')    
		if 'color' not in self.parameters:
			raise Exception('Parameter "color" required.')  
			
		# Generates the opening from parameters
		self.generate()  

	# Getter
	def getParameter(self, parameterKey):
		return self.parameters[parameterKey]
	
	# Setter
	def setParameter(self, parameterKey, parameterValue):
		self.parameters[parameterKey] = parameterValue
		return self        

	# Defines the vertices and faces        
	def generate(self):
		w = self.parameters['width'] ; h = self.parameters['height'] ; t = self.parameters['thickness']
		
		self.vertices = [ 
			# devant pgauche
			[0, 0, 0],
			[0, 0, h], 
			[0+t, 0, h],
			[0+t, 0, 0],
			# derriere pgauche
			[0, t, 0], 
			[0+t, t, 0], 
			[0+t, t, h],
			[0, t, h], 
			# devant phaut
			[0, 0, h-t],
			[0, 0, h], 
			[w, 0, h],
			[w, 0, h-t],
			# derriere phaut
			[0, t, h-t], 
			[w, t, h-t], 
			[w, t, h],
			[0, t, h], 	
			# devant pdroite
			[w, 0, 0],
			[w, 0, h], 
			[w-t, 0, h],
			[w-t, 0, 0],
			# derriere pdroite
			[w, t, 0], 
			[w-t, t, 0], 
			[w-t, t, h],
			[w, t, h],
			# devant pbas
			[0, 0, h-t],
			[0, 0, h], 
			[w, 0, h],
			[w, 0, h-t],
			# derriere pbas
			[0, t, h-t], 
			[w, t, h-t], 
			[w, t, h],
			[0, t, h]
		]
		self.faces = [ # sens anti-horaire
			[0, 3, 2, 1], # devant   pgauche
			[4, 7, 6, 5], # derriere pgauche
			[0, 1, 7, 4], # gauche   pgauche
			[2, 3, 5, 6], # droite   pgauche
			[1, 2, 6, 7], # haut     pgauche
			[3, 0, 4, 5],  # bas     pgauche
			
			[0, 3, 2, 1], # devant   pdoite
			[4, 7, 6, 5], # derriere pdoite
			[0, 1, 7, 4], # gauche   pdoite
			[2, 3, 5, 6], # droite   pdoite
			[1, 2, 6, 7], # haut     pdoite
			[3, 0, 4, 5],  # bas     pdoite
			
			[0, 3, 2, 1], # devant   phaut
			[4, 7, 6, 5], # derriere phaut
			[0, 1, 7, 4], # gauche   phaut
			[2, 3, 5, 6], # droite   phaut
			[1, 2, 6, 7], # haut     phaut
			[3, 0, 4, 5],  # bas     phaut
			
			[0, 3, 2, 1], # devant   pbas
			[4, 7, 6, 5], # derriere pbas
			[0, 1, 7, 4], # gauche   pbas
			[2, 3, 5, 6], # droite   pbas
			[1, 2, 6, 7], # haut     pbas
			[3, 0, 4, 5],  # bas     pbas
		]    
		
	# Draws the faces                
	def draw(self):        
		# A compléter en remplaçant pass par votre code
		pass
