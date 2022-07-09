from django.contrib import admin
from django.urls import path

from feed.views import FolderAlbumView, PostView

urlpatterns = [
   path('post/add/', PostView.as_view({'post': 'add_post'})),
   path('post/get/all/',PostView.as_view({'get': 'get_all_post'})),
   path('post/get/<str:slug>/',PostView.as_view({'get': 'get_single_post'})),
   path('get/folder/',FolderAlbumView.as_view({'get': 'get_folder'})),
   path('get/album/',FolderAlbumView.as_view({'get': 'get_album'}))
]
