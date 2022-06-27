from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . models import User, Profile, Poste, LikedPosts
from rest_framework.views import APIView
from jsonmerge import merge
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import datetime
from .forms import ProfileForm
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.core.files import File
import json
from .serializers import PostSerializer, LikedSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.forms.models import model_to_dict
from django.core.files.base import ContentFile
# Create your views here.
class index(APIView):
    def get(self, request):
        # users = serializers.serialize('json', User.objects.all())
        return Response("Hello")
        # return Response(merge(profiles, poste))

        #
        # profiles = serializers.serialize('json', Profile.objects.all())
        #
        # return JsonResponse([profiles, users], safe=False)
class getProfiles(APIView):
    def get(self, request):
        profiles = serializers.serialize('json', Profile.objects.all())
        return Response(profiles)





class getPoste(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request):
        poste = serializers.serialize('json', Poste.objects.all())
        return Response(poste)
    def post(self, request):
        return Response("Hello")
    def options(self, request):
        pass

class setPoste(APIView):
    def put(self, request, id):
        poste = Poste.objects.filter(id=id).first()
        # form = ProfileForm(data)
        # form.is_bound()
        poste.LikeCount = request.data["LikeCount"]
        # poste.LikeCount = 25
        poste.save()

        liked = LikedPosts()
        liked.Profile = Profile.objects.filter(id=request.data["profile_id"]).first()
        liked.Poste = poste
        liked.save()
        return Response({"message": request.data})



logger = logging.getLogger("myLogger")
@api_view(['POST', 'GET'])
def test(request, id):
    if request.method == 'POST':
        profile = Profile()
        # logger.error(request.data)
        Profile(SubCount = 12, Comment=None, state="Active", user_id=User.objects.get(id=5))
        profile.save()
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


@api_view(['POST', 'GET', 'PUT'])
@parser_classes([JSONParser])
def updateProfile(request, id):
    if request.method == "PUT":
        profile = Profile.objects.filter(id=id).first()
        profile.SubCount = request.data["SubCount"]
        profile.save()



        return Response({"message": request.data})

    if request.method == "GET":
        profile = serializers.serialize('json', Profile.objects.filter(id=id))
        return Response (profile)
    return Response({"message": "Bienvenue"})



class getUser(APIView):
    def get(self, request, id):
        user = serializers.serialize('json',Profile.objects.filter(id=id))
        return Response(user)
class detail(APIView):

    def get(self, request, id):
        user = User.objects.get(id=id)
        profile = Profile.objects.get(user=id)
        return render(request, 'detail.html', {'profile': profile, 'user': user})
#
# class getLikedPost(APIView):
#     def get(self, request, id):

class SetProfile(APIView):
    def post(self, request):
        profile = Profile()

        if Profile.objects.filter(user=request.data["user"]).exists():
            return Response(False)
        profile.user = request.data["user"]
        profile.password = request.data["password"]
        profile.SubCount = 0
        profile.state = "Connected"
        profile.save()
        return Response(True)

class Auth(APIView):
    def post(self, request):
        profile = Profile.objects.filter(user=request.data["user"], password=request.data["password"])
        if profile.exists():

            return Response({"resp" : True, "Id" : profile.values_list('id', flat=True)[0]})
        else:
            return Response({"resp": False, "Id": ""})

class CreatePost(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format = None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiLikedPosts(APIView):
    def get(self, request, id):
        liked = LikedPosts.objects.filter(Profile=id)
        if liked.exists():
            return Response({"resp": True, "data": serializers.serialize('json', liked)})
        return Response({"resp": False, "data": ""})

    def post(self, request, id):
        liked = LikedPosts()
        serializer = LikedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

