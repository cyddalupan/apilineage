from django.db import models

class MemberUser(models.Model):
	username = models.CharField(unique=True, max_length=255)
	password = models.CharField(unique=True, max_length=510)
	firstname = models.CharField(unique=True, max_length=255)
	middlename = models.CharField(unique=True, max_length=255)
	lastname = models.CharField(unique=True, max_length=255)
	parent_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username
