from django.db import models

class Question(models.Model):
	firstname = models.TextField(max_length=20)
	lastname = models.TextField(max_length=20)
	activity = models.TextField(max_length=20)
	language = models.TextField(max_length=20)
	class Meta:
		db_table = 'question'
