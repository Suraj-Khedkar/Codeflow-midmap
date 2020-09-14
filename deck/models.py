from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Event(models.Model):
    userid = models.IntegerField(default=0)
    event_name = models.CharField(max_length=250)
    due_date = models.DateField('date published')
    description = models.CharField(max_length=500)
    importance = models.IntegerField(default=0)
    urgency = models.IntegerField(default=0)
    approx_time = models.IntegerField(default=0)
    completion = models.IntegerField(default=0)
    parent_id = models.IntegerField(default=0)




