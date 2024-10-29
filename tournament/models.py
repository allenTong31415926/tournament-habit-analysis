from django.db import models


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=255)
    format = models.IntegerField(choices=[(1, 'round_robin'), (2, 'single_elimination'), (3, 'double_elimination')])
    sports = models.IntegerField(choices=[(1, 'baseball'), (2, 'basketball'), (3, 'tennis'), (4, 'karate')])
    team_player = models.IntegerField(choices=[(1, 'team'), (2, 'player')])

    def __str__(self):
        return self.name
