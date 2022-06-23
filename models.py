from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=80)
    subject=models.CharField(max_length=250)
    message=models.CharField(max_length=1000)
    class Meta:
        db_table="contact"
        
class schedule(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    time=models.CharField(max_length=80)
    date=models.CharField(max_length=250)
    pic=models.ImageField(upload_to='image/',default="")
    message=models.CharField(max_length=1000)
    class Meta:
        db_table="schedule"
        
class apt(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=80)
    date=models.CharField(max_length=250)
    time=models.CharField(max_length=80)
    subject=models.CharField(max_length=250)
    message=models.CharField(max_length=1000)
    class Meta:
        db_table="apt"

class mail(models.Model):
    email=models.CharField(max_length=80)
    class Meta:
        db_table="mail"
        
class blog(models.Model):
    title=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='image/',default="")
    description=models.CharField(max_length=1000)
    poston=models.CharField(max_length=100)
    postby=models.CharField(max_length=100)
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title