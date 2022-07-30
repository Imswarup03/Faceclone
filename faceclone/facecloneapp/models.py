from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# after creating your model *1, python manage.py makemigrations **2,python manage.py migrate
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    status = models.CharField(max_length=300,blank=True)
    location = models.CharField(max_length=300,blank=True)
    pic = models.ImageField(upload_to='pics',blank=True)

    def __str__(self):
        return self.user.username