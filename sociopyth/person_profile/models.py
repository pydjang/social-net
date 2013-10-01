from django.db import models

GENDER = (
	('M', 'Male'),
	('F', 'Female')
)

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	job_title=models.CharField(max_length=30)
	gender=models.CharField(max_length=1, choices=GENDER)

	def __unicode__(self):
        return u"%s" % self.first_name

