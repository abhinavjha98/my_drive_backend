
from django.http import request
from django.shortcuts import render
from account.models import CustomUser, Profession
from account.serializers import ProfessionSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from feed.models import Album, Folder, Post, PostImage
from feed.serializers import AlbumSerializer, FolderSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from account.utils import get_tokens_for_user, register_user, validate_data
from rest_framework.parsers import MultiPartParser, FileUploadParser


# Create your views here.
class PostView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def add_post(self,request):
        try:
            user = request.user
            data = request.data
            title = data.get("title",None)
            post_type = data.get("post_type",None)
            folder_name = data.get("folder_name",None)
            album_name = data.get("album_name",None)
            places = data.get("places",None)
            things = data.get("things",None)
            multiple_files = request.FILES
            media_files = multiple_files.getlist("media_file")
            post = Post(
                    user=user,
                    post_type=post_type,
                    title=title,
                    folder_name=folder_name,
                    album_name=album_name,
                    places=places,
                    things=things,
                )
            post.save()


            if len(media_files) >= 1:
                    for i in range(len(media_files)):
                        
                        post_image = PostImage(
                            post=post,
                            image=media_files[i],
                        )
                        post_image.save()
            else:
                pass
            return Response(
                    data={'status': True, 'message': 'post added successfully'}, 
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST)

    def get_all_post(self,request):
        user = request.user
        post_object = Post.objects.filter(user=user)
        res = PostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

    def get_single_post(self,request,**kwargs):
        slug = kwargs.get("slug")
        user = request.user
        post_object = Post.objects.filter(user=user,id=int(slug))
        res = PostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

class FolderAlbumView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def get_folder(self,request):
        user = request.user
        folder_object = Folder.objects.filter(user=user)
        res = FolderSerializer(folder_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

    def get_album(self,request):
        user = request.user
        album_object = Album.objects.filter(user=user)
        res = AlbumSerializer(album_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )
