from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profession(Base):
    name = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)

class ReferalCode(Base):
    refer_code =  models.CharField(max_length=150, null=True, blank=True)

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=150, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    finger_print = models.CharField(max_length=500, null=True, blank=True)
    pass_code = models.CharField(max_length=10,null=True,blank=True)
    user_face = models.CharField(max_length=500, null=True, blank=True)
    user_storage = models.FloatField(default=0.0)
    dark_mode = models.BooleanField(default=False)
    notification = models.BooleanField(default=True)
    referal_code = models.ForeignKey(ReferalCode, null=True, on_delete=models.CASCADE)
    referal_count = models.PositiveIntegerField(default=5)

class ReferalUser(Base):
    refer_to = models.ForeignKey(CustomUser,blank=True, null=True, on_delete=models.CASCADE,related_name="Refer_to")
    refer_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE,related_name="Refer_By")
    refer_by_without_register = models.CharField(max_length=100,null=True,blank=True)
    refer_code = models.ForeignKey(ReferalCode, null=True, on_delete=models.CASCADE)

class LogsTable(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    event_name =  models.CharField(max_length=150, null=True, blank=True)