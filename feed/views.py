
from django.http import request
from django.shortcuts import render
from account.models import CustomUser, Profession
from account.serializers import ProfessionSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from feed.models import Album, ArchivePost, FavouritePost, Folder, Post, PostImage, TrashPost
from feed.serializers import AlbumSerializer, ArchivePostSerializer, FavouritePostSerializer, FolderSerializer, PostSerializer, TrashPostSerializer
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

class TrashView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def add_trash(self,request):
        user = request.user
        data = request.data
        post_id = data.get('post_id')
        post = Post.objects.get(id=int(post_id))
        trash_post = TrashPost(
            user = user,
            post = post
        )
        trash_post.save()
        return Response(
                    data={'status': True, 'message': 'post moved to trash successfully'}, 
                    status=status.HTTP_200_OK
                )
    
    def get_single_trash(self,request,**kwargs):
        slug = kwargs.get("slug")
        user = request.user
        post_object = TrashPost.objects.filter(user=user,id=int(slug))
        res = TrashPostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

    def get_all_trash(self,request):
        user = request.user
        post_object = TrashPost.objects.filter(user=user)
        res = TrashPostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

class ArchiveView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def add_archive(self,request):
        user = request.user
        data = request.data
        post_id = data.get('post_id')
        post = Post.objects.get(id=int(post_id))
        archive_post = ArchivePost(
            user = user,
            post = post
        )
        archive_post.save()
        return Response(
                    data={'status': True, 'message': 'post moved to trash successfully'}, 
                    status=status.HTTP_200_OK
                )
    
    def get_single_archive(self,request,**kwargs):
        slug = kwargs.get("slug")
        user = request.user
        post_object = ArchivePost.objects.filter(user=user,id=int(slug))
        res = ArchivePostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

    def get_all_archive(self,request):
        user = request.user
        post_object = ArchivePost.objects.filter(user=user)
        res = ArchivePostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

class FavouriteView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def add_favourite(self,request):
        user = request.user
        data = request.data
        post_id = data.get('post_id')
        post = Post.objects.get(id=int(post_id))
        favourite_post = FavouritePost(
            user = user,
            post = post
        )
        favourite_post.save()
        return Response(
                    data={'status': True, 'message': 'post moved to trash successfully'}, 
                    status=status.HTTP_200_OK
                )
    
    def get_single_favourite(self,request,**kwargs):
        slug = kwargs.get("slug")
        user = request.user
        post_object = FavouritePost.objects.filter(user=user,id=int(slug))
        res = FavouritePostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

    def get_all_favourite(self,request):
        user = request.user
        post_object = FavouritePost.objects.filter(user=user)
        res = FavouritePostSerializer(post_object, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )
