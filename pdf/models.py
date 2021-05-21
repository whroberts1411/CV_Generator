from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50,default='')
    summary = models.TextField(max_length=2000)
    degree = models.TextField(max_length=500)
    school = models.TextField(max_length=400)
    university = models.TextField(max_length=500)
    previous_work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)

    def __str__(self):

        return self.name
