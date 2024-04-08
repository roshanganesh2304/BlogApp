from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="profile_images",null=True)
    dob=models.DateField()
    phone=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    followed_by=models.ManyToManyField(User,related_name="follower")

    def followed_users(self):
        return self.followed_by.all()

class Posts(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=800)
    image=models.ImageField(upload_to="post_images",null=True)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    liked_by=models.ManyToManyField(User,related_name="user")

    def fetch_comments(self):
        return self.comments_set.all()
    
    def liked_users(self):
        return self.liked_by.all()
    
    def like_count(self):
        return self.liked_by.all().count()

class Comments(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
