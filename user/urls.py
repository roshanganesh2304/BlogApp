from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('user',UserView,basename="user"),
router.register('profile',ProfileView,basename="profile"),
router.register('post',PostView,basename="post")

urlpatterns=[
   
]+router.urls