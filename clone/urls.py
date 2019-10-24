from django.urls import path

from .views import *
from . import views
# from . import api_views

urlpatterns = [
    path("PostGetAll/page/<page_num>", PostGetAll.as_view()),
    path("posts", PostView.as_view()),
    path("posts/<id>", PostView.as_view()),
    path("postQuery/<id>", PostQuery.as_view()),
    ]
