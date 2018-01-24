# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your models here.


class UserManager(models.Manager):
    def validate_user(self, first_name, last_name, email):
        user = User.objects.create_user(first_name='Naruto', last_name='Uzumaki', email='SAAASSSSUUUKKKEE@hokage.com'),
        user = User.objects.create_user(first_name='Sasuke', last_name='Uchia', email='Iwilldestroykonoha@alone.com'),
        user = User.objects.create_user(first_name='Raito', last_name='Yagami', email='godofthenewworld@kira.com'),
        user = User.objects.create_user(first_name='L', last_name='Ryuzaki', email='youarekira@sweets.com'),
        user = User.objects.create_user(first_name='Dean', last_name='Winchester', email='Imbatman@notgay.com'),
        user = User.objects.create_user(first_name='Castiel', last_name='Winchester', email='iloveyou@dean.com'),
        user = User.objects.create_user(first_name='Sam', last_name='Winchester', email='notafraidoffeelings@salads.com'),
        user = User.objects.create_user(first_name='Gabriel', last_name='Winchester', email='ilovesamsquatch@sweettooth.com')
        user.save(first_name, last_name, email)
        return user
   
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    #age = models.IntegerField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    
   

    
   
   