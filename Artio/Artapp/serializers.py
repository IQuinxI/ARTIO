from rest_framework import serializers
from .models import Poste, LikedPosts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = ('Titre', 'LikeCount', 'Comment', 'Date', 'Art', 'profile')

class LikedSerializer(serializers.ModelSerializer):
    class Meta:

        model = LikedPosts
        fields = '__all__'


