from django.db import models
from django.contrib.auth.models import User

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
    remarks = models.TextField(blank=True, default="")
    fund = models.ForeignKey("mainapp.Fund")

    def __str__(self):
        return str(self.type) + ": " + str(self.remarks)

class BufferItem(models.Model):
    type = models.ForeignKey(ItemType)
    remarks = models.TextField(blank=True, default="")
    fund = models.ForeignKey("mainapp.Buffer")

    def __str__(self):
        return str(self.type) + ": " + str(self.remarks)

class AbstractFund(models.Model):
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
        if self.provider:
            return str(self.provider) + " - " + str(self.place)
        else:
            return str(self.place)

    class Meta:
        abstract = True

class Fund(AbstractFund):
    pass

class Buffer(AbstractFund):
    fund = models.OneToOneField(Fund, null=True, blank=True, default=None)

class AdminUser(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
