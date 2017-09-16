#Created by: Alireza Teimoori
#Created on: 15 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit0-04
#This program is hello world but with 3 buttons

import ui

def english_touch_up_inside(sender):
	view['hello_world_lable'].text=("Hello, World!")
	
def french_touch_up_inside(sender):
	view['hello_world_lable'].text=("Bonjour, le monde!")

def persian_touch_up_inside(sender):
	view['hello_world_lable'].text=("Salam, Donya!")
					
view = ui.load_view()
view.present('sheet')
