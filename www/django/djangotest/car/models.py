from django.db import models

CAR_CHOICES = (
	('D','Domestic'),
        ('I','Import'),
)

class Car(models.Model):
	name = models.CharField(max_length=200)
 	slug = models.SlugField(unique=True)
        make = models.ForeignKey('Make')
   	locality = models.CharField(max_length=1, choices=CAR_CHOICES)
	description = models.TextField(blank=True)
        image1 = models.ImageField(upload_to="images/carthumbs/")

	def __unicode__(self):
		return self.name


class Make(models.Model):
	name = models.CharField(max_length=200)
 	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

