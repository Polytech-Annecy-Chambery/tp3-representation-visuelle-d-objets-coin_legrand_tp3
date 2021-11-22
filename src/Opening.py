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
			[0, 0, t],           
			[0, 0, 0],             
			[w, 0, 0],             
			[w, 0, t],           
			# derriere pbas        
			[0, t, t],           
			[w, t, t],           
			[w, t, 0],             
			[0, t, 0]              
		]
		
		self.faces = []
		for i in range(0, len(self.vertices), 8):
			self.faces += [
				[0+i, 3+i, 2+i, 1+i], # devant   
				[4+i, 7+i, 6+i, 5+i], # derriere 
				[0+i, 1+i, 7+i, 4+i], # gauche   
				[2+i, 3+i, 5+i, 6+i], # droite   
				[1+i, 2+i, 6+i, 7+i], # haut     
				[3+i, 0+i, 4+i, 5+i],  # bas     
			]
		
	# Draws the faces                
	def draw(self):        
		# A compléter en remplaçant pass par votre code
		gl.glPushMatrix()
		gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
		
		gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
		for face in self.faces:
			gl.glBegin(gl.GL_QUADS) 
			gl.glColor3fv(self.parameters['color'])
			for pointInd in face: 
				gl.glVertex3fv(self.vertices[pointInd])
			gl.glEnd()
		
		gl.glPopMatrix()
