from django.db import models

class ItemType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Item(models.Model):
    type = models.ForeignKey(ItemType)
    amount = models.IntegerField(default=0)
    items = models.ForeignKey("mainapp.Fund")

    def __str__(self):
        return str(self.amount) + " of " + str(self.type)

class Fund(models.Model):
    provider = models.ForeignKey(Provider, null=True, blank=True, default=None)
    place = models.ForeignKey(Place)
    
    PROVIDED = 0
    NEEDED = 1
    URGENTLY_NEEDED = 2
    FUND_STATES = (
        (PROVIDED, 'Provided'),
        (NEEDED, 'Needed'),
        (URGENTLY_NEEDED, 'Urgently Needed'),
    )
    state = models.IntegerField(default=NEEDED, choices=FUND_STATES)

    UNREVIEWED = 0
    ACCEPTED = 1
    REVIEW_STATES = (
        (UNREVIEWED, 'Unreviewed'),
        (ACCEPTED, 'Accepted'),
    )
    review_state = models.IntegerField(default=UNREVIEWED, choices=REVIEW_STATES)
    
    def __str__(self):
        return str(self.provider) + " - " + str(self.place)
