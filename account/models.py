from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
# UserProfile model extending built-in User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True) #  Optional to avoid migration error
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

# Signal to auto-create or update the profile whenever a User is created or saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            name=instance.get_full_name(),
            email=instance.email,
        )
    else:
        instance.profile.save()    


