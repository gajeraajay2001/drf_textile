from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PartySerializers,EntrySerializers
from .models import PartyModel,EntryModel
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class PartyView(APIView):

    def get(self,request):
        partyList  = PartyModel.objects.all()
        serializer = PartySerializers(partyList,many = True)
        return Response({"message":"Parties List....","data":serializer.data,"success":True},status= status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PartySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Party Added Successfully....","success":True},status= status.HTTP_201_CREATED)
    

class PartyUpdateView(APIView):

    def patch(self, request,party_id, *args, **kwargs):
        try:
            party = PartyModel.objects.get(party_id =party_id)
            serializer = PartySerializers(party,data=request.data,partial = True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":"Party Updated Successfully....","success":True},status= status.HTTP_200_OK)
        except Exception as error:
            return Response({"message":"Invalid Party Id","success":False},status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request,party_id, *args, **kwargs):
        try:
            party = PartyModel.objects.get(party_id =party_id)
            party.delete()
            return Response({"message":"Party Deleted Successfully....","success":True},status= status.HTTP_200_OK)
        except Exception as error:
            return Response({"message":"Invalid Party Id","success":False},status= status.HTTP_400_BAD_REQUEST)
    

class EntryView(APIView):

    def get(self, request, *args, **kwargs):
        entry = EntryModel.objects.all()
        serializer = EntrySerializers(entry,many=True)
        return Response({"message":"Entry fecthed....","data":serializer.data,"success":True},status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = EntrySerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Entry Added...","data":serializer.data,"success":True},status=status.HTTP_201_CREATED)