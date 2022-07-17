from django.contrib import admin
from django.urls import path

from feed.views import ArchiveView, FavouriteView, FolderAlbumView, PostView, TrashView

urlpatterns = [
   path('post/add/', PostView.as_view({'post': 'add_post'})),
   path('post/get/all/',PostView.as_view({'get': 'get_all_post'})),
   path('post/get/<str:slug>/',PostView.as_view({'get': 'get_single_post'})),
   path('folder/get/',FolderAlbumView.as_view({'get': 'get_folder'})),
   path('album/get/',FolderAlbumView.as_view({'get': 'get_album'})),
   path('trashpost/get/<str:slug>/',TrashView.as_view({'get':'get_single_trash'})),
   path('trashpost/get/all/',TrashView.as_view({'get':'get_all_trash'})),
   path('trashpost/add/',TrashView.as_view({'post':'add_trash'})),
   path('trashpost/delete/<str:slug>/',TrashView.as_view({'get':'delete_trash'})),
   path('archivepost/get/<str:slug>/',ArchiveView.as_view({'get':'get_single_archive'})),
   path('archivepost/get/all/',ArchiveView.as_view({'get':'get_all_archive'})),
   path('archivepost/add/',ArchiveView.as_view({'post':'add_archive'})),
   path('archivepost/delete/<str:slug>/',ArchiveView.as_view({'get':'delete_archive'})),
   path('favouritepost/get/<str:slug>/',FavouriteView.as_view({'get':'get_single_favourite'})),
   path('favouritepost/get/all/',FavouriteView.as_view({'get':'get_all_favourite'})),
   path('favouritepost/add/',FavouriteView.as_view({'post':'add_favourite'})),
   path('favouritepost/delete/<str:slug>/',FavouriteView.as_view({'get':'delete_favourite'})),
]
