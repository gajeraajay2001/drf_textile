from rest_framework import serializers
from .models import PartyModel,EntryModel

class PartySerializers(serializers.ModelSerializer):

    class Meta:
        model = PartyModel
        fields = "__all__"

class EntrySerializers(serializers.ModelSerializer):
    # party = serializers.PrimaryKeyRelatedField(queryset=PartyModel.objects.all())

    class Meta:
        model = EntryModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        party_id = representation['party']
        party_name = PartyModel.objects.get(party_id=party_id).party_name
        representation['party'] = {'party_id': party_id, 'party_name': party_name}
        return representation
