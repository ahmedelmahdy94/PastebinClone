from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .pagination import Pagination
import decimal
from datetime import date

import uuid
# Create your views here.

# get all Posts from database sperate in pages in each page 5 post
class PostGetAll(APIView):
    def get(self, request, page_num):
        page = int(page_num)
        posts = Posts.objects.filter(Active=True).order_by('create_date')
        print(len(list(posts)))

        page_number = request.GET.get('page', page)
        paginate_result = Pagination.do_paginate(posts, page_number)
        posts = paginate_result[0]


        serializer = PostSerializer(posts, many=True)
        # print(serializer)
        return Response({
            "status": "200",
            "message": "All active Posts",
            "Posts": serializer.data

        })
#
#
class PostView(APIView):
    # create new post
    #  json file example
    #  {
    #     "name": "mahdi",
    #     "content": "my name is ahmed elmahdi",
    #     "Active": "True"
    # }

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):
            # print(serializer)
            serializer.save(user = self.request.user)
        else:
            return Response({
                "status": "400",
                "message": "Bad Request",

            })
        return Response({
            "status": "200",
            "message": "Post successfuly created",
            "Post": serializer.data
        })

    # update post data by post id
    #  json file example
    #  {
    #     "name": "mahdi",
    #     "content": "my name is ahmed elmahdi",
    #     "Active": "True
    # }
    def put(self, request, id):
        post = get_object_or_404(Posts, pk=id)
        print(id)
        if post or post is not None:
            data = request.data
            serializer = PostSerializer(
                instance=post, data=data, partial=True)
            if serializer.is_valid(raise_exception=False):
                post_saved = serializer.save()
            else:
                return Response({"status": "400","message": "Bad Request"})
            return Response({
                "status": "200",
                "message": "Post successfuly updated",
                "Post ": serializer.data
            })
        else:
            return Response({"detail": "Not found."})

    # suspend post by post id
    def delete(self, request, id):
        post = get_object_or_404(Posts, pk=id)
        if post or post is not None:
            post.Active = False
            post.save()
            return Response({'status': "200", 'message': "Post successfuly suspend"})
        else:
            return Response({ "detail": "Not found."})

#  get specific post by post id
class PostQuery(APIView):
    def get(self, request, id):
        post = get_object_or_404(Posts, pk=id)
        if post or post is not None:
            serializer = PostSerializer(post)
            return Response({'status': "200", 'Post': serializer.data})
        else:
            return Response({"detail": "Not found."})
