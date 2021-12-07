# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy


def Q1a():
	return Configuration()
	
def Q1b_f():
	return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
		setParameter('xAxisColor', [1, 1, 0]). \
		setParameter('yAxisColor', [0,1,1]). \
		display()
		
def Q2b():
	# Ecriture en utilisant le chaînage
	return Configuration().add(
			Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
			) 

def Q2c():
	# Ecriture en utilisant le chaînage
	return Configuration().add(
			Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
			)

def Q3a():
	return Configuration().add(
		Wall({'position': [1, 1, 0], 'width':7, 'height':2.6, "orientation": 20})
	)   

def Q4a():
	# Ecriture en utilisant des variables : A compléter
	wall1 = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "orientation": 0})
	wall2 = Wall({'position': [7, 0, 0], 'width': 7, 'height': 2.6, "orientation": 90})
	wall3 = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "orientation": 90})
	wall4 = Wall({'position': [-wall1.parameters["thickness"], 7, 0], 'width': 7+wall1.parameters["thickness"], 'height': 2.6, "orientation": 0})
	house = House({'position': [0, 0, 0], 'orientation': 0})
	house.add(wall1).add(wall3).add(wall4).add(wall2)
	return Configuration().add(house)   
	
def Q5a():  
	# Ecriture avec mélange de variable et de chaînage    
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
	return Configuration().add(opening1).add(opening2)
	
def Q5b():  
	# Ecriture avec mélange de variable et de chaînage   
	section = Section({'width':7, 'height':2.6})
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	
	print(section.canCreateOpening(opening1))
	print(section.canCreateOpening(opening2))    
	print(section.canCreateOpening(opening3))
	return Configuration()    
	
def Q5c1():      
	section = Section({'width':7, 'height':2.6})
	opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
	#sections = section.createOpening(opening1)
	sections = section.createNewSections(opening1)
	configuration = Configuration()
	for x in sections:
		configuration.add(x)    
	return configuration     
	
def Q5c2():      
	section = Section({'width':7, 'height':2.6})
	opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
	#sections = section.createNewSections(opening2)
	sections = section.createNewSections(opening2)
	configuration = Configuration()
	for section in sections:
		configuration.add(section)    
	return configuration    

def Q5d():      
	wall = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "thickness": 0.4, "orientation": 0})
	wall.add( Opening({'position': [2, 0.1, 0], 'width':0.9, 'height': 2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) )
	wall.add( Opening({'position': [4, 0.1, 1.2], 'width':1.25, 'height': 1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) )
	configuration = Configuration()
	configuration.add(wall)
	return configuration
	
def Q6():  
	wall = Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "thickness": 0.4, "orientation": 0})
	#wall.add( Opening({'position': [2, 0.1, 0], 'width':0.9, 'height': 2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) )
	#wall.add( Opening({'position': [4, 0.1, 1.2], 'width':1.25, 'height': 1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) )
	wall.add(Door({'position': [2.1, 0.1, 0.3], 'width':0.9, 'height': 2.15, 'thickness':0.2, 'color': [1, 0, 0]}))
	#wall.add( Door({'position': [2.1, 0.1, 0.1], 'width':0.8, 'height': 2, 'thickness':0.2, 'color': [1, 0, 0]}) )
	#wall.add( Window({'position': [4.05, 0.1, 1.25], 'width':1.2, 'height': 0.95, 'thickness':0.2, 'color': [0.9, 0.9, 1]}) )
	configuration = Configuration()
	configuration.add(wall)
	return configuration  
 
def main():
	# Enlever un des commentaires pour la question traitée
	
	#configuration = Q1a()
	# configuration = Q1b_f()
	#configuration = Q2b()
	#configuration = Q2c()
	#configuration = Q3a()
	#configuration = Q4a()
	#configuration = Q5a()
	#configuration = Q5b()
	#configuration = Q5c1()
	#configuration = Q5c2() 
	#configuration = Q5d()
	#configuration = Q6()
	configuration.display()
		 
# Calls the main function
if __name__ == "__main__":
	#main() 
	
	doors = [ Door({'position': [2.1, 0.1, 0.1], 'width':0.8, 'height': 2, 'thickness':0.2, 'color': [1, 0, 0]}) ]
	house = House().add(
		Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "thickness": 0.4, "orientation": 0})\
		.add(doors[0])
		.add(Window({'position': [4.05, 0.1, 1.25], 'width':1.2, 'height': 0.95, 'thickness':0.2, 'color': [0.9, 0.9, 1]}))
	).add(
		Wall({'position': [7, 0, 0], 'width': 7, 'height': 2.6, "thickness": 0.4, "orientation": 90})
	).add(
		Wall({'position': [0, 0, 0], 'width': 7, 'height': 2.6, "thickness": 0.4, "orientation": 90})
	).add(
		Wall({'position': [-0.4, 7, 0], 'width': 7+0.4, 'height': 2.6, "thickness": 0.4, "orientation": 0})
	)
	
	configuration = Configuration()
	configuration.add(house).display(doors)
	
