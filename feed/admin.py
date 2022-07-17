from calendar import c
from django.contrib import admin
from feed.models import Album, ArchivePost, DeleteTrashPost, FavouritePost, Folder, Post, PostImage, TrashPost, UserShare
from feed.serializers import AlbumSerializer
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','post_type',)
    search_fields = ('user__username','places','things','title')
    list_filter = ('places','things')

class FolderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','folder_name',)
    search_fields = ('user__username','folder_name')
    list_filter = ('folder_name',)

class AlbumAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','album_name',)
    search_fields = ('user__username','folder_name')
    list_filter = ('album_name',)

class PostImageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('post','image',)
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

class ArchivePostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','post',)
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

class FavouritePostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','post',)
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

class TrashPostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','post',)
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

class UserShareAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('post','shared_by','shared_to')
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

class DeleteTrashPostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','post',)
    search_fields = ('post__title','post__places','post__places')
    list_filter = ('post__user__username',)

admin.site.register(Post,PostAdmin)
admin.site.register(Folder,FolderAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(PostImage,PostImageAdmin)
admin.site.register(TrashPost,TrashPostAdmin)
admin.site.register(ArchivePost,ArchivePostAdmin)
admin.site.register(FavouritePost,FavouritePostAdmin)
admin.site.register(UserShare,UserShareAdmin)
admin.site.register(DeleteTrashPost,DeleteTrashPostAdmin)