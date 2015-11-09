from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Drive is actually a UserProfile
# In settings.py :  (app.className)
#    AUTH_PROFILE_MODULE = 'driver.Driver'
class Driver(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birthday = models.DateField()
    name  = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #driver, new = Driver.objects.get_or_create(user=instance)
        Driver.objects.get_or_create(user=instance)

# We want to create a profile every time 
# a User instance is created by registering a post_save handler, 
# this way every time we create a user Django will create his profile too:
post_save.connect(create_user_profile, sender=User)

