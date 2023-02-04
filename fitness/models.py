from django.db import models

# creating the users
class custom_user(models.Model):
    email = models.EmailField(max_length=200,primary_key=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email
class indoor_activities(models.Model):
    event_name=models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='static/images')
    target = models.CharField(max_length=100)
    prize_pool = models.CharField(max_length=100)
    max_players = models.CharField(max_length=100)
    event_id = models.CharField(max_length=100)
    bet = models.CharField(max_length=100)


    def __str__(self):
        return self.event_name
    