from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Game(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField(null=False, default=datetime.now())
    location=models.CharField(max_length=255,blank=False)
    user=models.ForeignKey(User)
    def __unicode__(self):
        return 'Date: '+self.date+'; Location: '+self.location

class Player(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank=False)
    games=models.ManyToManyField(Game)
    user=models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class Inning(models.Model):
    id=models.AutoField(primary_key=True)
    number=models.IntegerField(null=False)
    game=models.ForeignKey('Game')
    pitcher=models.ForeignKey('Player')
    def __unicode__(self):
        return 'Inning #: '+self.number+'; Pitcher: '+pitcher__name

class Score(models.Model):
    inning=models.ForeignKey('Inning')
    batter=models.ForeignKey('Player')
    score=models.IntegerField(null=False)
    def __unicode__(self):
        return self.score
