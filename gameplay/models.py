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
    
    class Meta:
        unique_together = (("name","user"),)

class BatterOrder(models.Model):
    game=models.ForeignKey('Game')
    qposition=models.IntegerField(null=False)
    player=models.ForeignKey('Player')
    
    def __unicode__(self):
        return 'Position: '+self.qposition

class PitcherOrder(models.Model):
    game=models.ForeignKey('Game')
    qposition=models.IntegerField(null=False)
    player=models.ForeignKey('Player')
    
    def __unicode__(self):
        return 'Position: '+self.qposition

class Inning(models.Model):
    id=models.AutoField(primary_key=True)
    number=models.IntegerField(null=False)
    game=models.ForeignKey('Game')
    pitcher=models.ForeignKey('Player')
    def __unicode__(self):
        return 'Inning #: '+self.number+'; Pitcher: '+pitcher__name

class BatterScore(models.Model):
    inning=models.ForeignKey('Inning')
    # How many times has this player been at bat, 
    # inclusive of this time.
    turn=models.IntegerField(null=False)
    player=models.ForeignKey('Player')

    # If True => score=1.
    walk=models.BooleanField(default=False)
    # (W=1) ,1,2,3,4 
    score=models.IntegerField(null=False)
    def __unicode__(self):
        return self.score

class PitcherScore(models.Model):
    inning=models.ForeignKey('Inning')
    player=models.ForeignKey('Player')

    runsagainst=models.IntegerField(null=False)
    # num_sos=models.IntegerField -- This will always be 3 to end an inning
    
    # ERA = (# At bats)/(# Strikeouts (Ks))    
    # era=models.IntegerField(null=False)
    def __unicode__(self):
        return self.era
