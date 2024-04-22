from django.db import models
import uuid

# Create your models here.
class PartyModel(models.Model):
    party_id = models.UUIDField(primary_key=True,default= uuid.uuid4,editable=False,unique=True)
    party_name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.party_name
    
class EntryModel(models.Model):
    party = models.ForeignKey(PartyModel, on_delete=models.CASCADE, null=False)
    chalan_number = models.CharField(max_length=50,blank=False)
    bill_number  = models.CharField(max_length=50,blank=False)
    rate = models.IntegerField(null=False,blank=False)
    tax = models.IntegerField(null=True,default=0)
    gst = models.IntegerField(null=False,blank=False)
    total = models.IntegerField(null=False,blank=False)