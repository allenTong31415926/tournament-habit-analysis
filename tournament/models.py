from django.db import models

class Tournament(models.Model):
    class Format(models.IntegerChoices):
        ROUND_ROBIN = 1, 'round_robin'
        SINGLE_ELIMINATION = 2, 'single_elimination'
        DOUBLE_ELIMINATION = 3, 'double_elimination'

    class Sports(models.IntegerChoices):
        BASEBALL = 1, 'baseball'
        BASKETBALL = 2, 'basketball'
        TENNIS = 3, 'tennis'
        KARATE = 4, 'karate'

    class TeamPlayer(models.IntegerChoices):
        TEAM = 1, 'team'
        PLAYER = 2, 'player'

    name = models.CharField(max_length=255)
    format = models.IntegerField(choices=Format.choices)
    sports = models.IntegerField(choices=Sports.choices)
    team_player = models.IntegerField(choices=TeamPlayer.choices)

    def __str__(self):
        return self.name

    @classmethod
    def get_sport_enum(cls, sport_name):
        """Helper method to convert sport name to enum integer."""
        try:
            return cls.Sports[sport_name.upper()].value
        except KeyError:
            return None  # Returns None if sport_name is invalid
