from __future__ import unicode_literals

import datetime
import django
from django import forms
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    time_creation = models.DateTimeField(django.utils.timezone.now())
    displayPref = models.IntegerField(default=1)
    emailInvite = models.BooleanField(default=False)
    emailDelete = models.BooleanField(default=False)
    emailStart = models.BooleanField(default=False)
    emailStop = models.BooleanField(default=False)
    showHint = models.BooleanField(default=True)
    mturk = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    code = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    sequence = models.TextField(default="")
    cur_poll = models.IntegerField(default=1)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
