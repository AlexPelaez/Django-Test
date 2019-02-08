from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Current server location choices for users.
SERVER_LOCATIONS = (
		('E', 'North America East'),
		('W', 'North America West'),
	)
# UserProfile model contians main profile information for users.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	server = models.CharField(max_length=1, choices=SERVER_LOCATIONS, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True)
	description = models.CharField(max_length=100, default='', blank=True)
	city = models.CharField(max_length=100, default='', blank=True)
	wins = models.IntegerField(default=0)
	
def __str__(self):
	return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender = User)
