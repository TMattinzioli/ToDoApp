#This file is for all database stuff.
#To do database stuff, you have to run a class.

from django.db import models

class List(models.Model):
	item = models.CharField(max_length = 200)
	#CharField and BooleanField are data types.
	#CharField is a Character Field. We are adding characters.
	completed = models.BooleanField(default = False)
	#BooleanField is a True/False field. Set default as False.


	
	#Need this for admin page.
	def __str__(self):
		#.item refers to item above.
		return self.item + ' ' + str(self.completed)