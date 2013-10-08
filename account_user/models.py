from django.db import models

# Create your models here.
class Account_User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    meals_offered = models.IntegerField(max_length=2)
    currently_offering = models.BooleanField(default=False)
    currently_seeking = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

class Schedule(models.Model):
    WEEKDAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('August', 'H-August'),
    )
    username = models.ForeignKey(Account_User)
    weekday = models.CharField(max_length=30, choices=WEEKDAYS, default='Monday')
    time_start = models.TimeField()
    time_end = models.TimeField()