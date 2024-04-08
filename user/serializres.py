from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    

class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    followed_users=UserSerializer(read_only=True,many=True)
    class Meta:
        model=UserProfile
        exclude=["followed_by"]
    def create(self, validated_data):
        user=self.context.get('user')
        return UserProfile.objects.create(user=user,**validated_data)



class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    datetime=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        fields="__all__"

    def create(self, validated_data):
        post=self.context.get('post')
        user=self.context.get('user')
        return Comments.objects.create(user=user,post=post,**validated_data)
class PostSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    datetime=serializers.CharField(read_only=True)
    fetch_comments=CommentSerializer(read_only=True,many=True)
    liked_users=UserSerializer(read_only=True,many=True)
    like_count=serializers.IntegerField(read_only=True)
    class Meta:
        model=Posts
        exclude=('liked_by',)


