from django.db import models

class FundType(models.Model):
    name = models.CharField(max_length=50)

class FundState(models.Model):
    name = models.CharField(max_length=20)
    
    YELLOW = 0
    GREEN = 1
    ORANGE = 2
    RED = 3
    COLORS = (
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (ORANGE, 'Orange'),
        (RED, 'Red')
    )
    color = models.IntegerField(default=GREEN, choices=COLORS)

class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()

class Place(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Fund(models.Model):
    provider = models.ForeignKey(Provider)
    types = models.ManyToManyField(FundType)
    state = models.ForeignKey(FundState)
    place = models.ForeignKey(Place)
    amount = models.IntegerField()
    
    UNREVIEWED = 0
    ACCEPTED = 1
    REVIEW_STATES = (
        (UNREVIEWED, 'Unreviewed'),
        (ACCEPTED, 'Accepted'),
    )
    review_state = models.IntegerField(default=UNREVIEWED, choices=REVIEW_STATES)

