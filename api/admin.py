from django.contrib import admin
from .models import PartyModel,EntryModel

# Register your models here.
admin.site.register(PartyModel)
admin.site.register(EntryModel)
