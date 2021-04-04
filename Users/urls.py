
from django.urls import path
from .views import PostUser

urlpatterns = [
    path('create_user/',PostUser.as_view()),
]
