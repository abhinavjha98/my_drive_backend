from django.db import models

from account.models import Base,CustomUser

POST_CHOICES = (
    ('image', 'image'),
    ('video', 'video'),
    ('story', 'Story')
)

# Create your models here.

class Album(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, null=True)

class Folder(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100, null=True)

class Post(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    post_type = models.CharField(max_length=100, choices=POST_CHOICES, default='image')
    folder_name = models.ForeignKey(Folder,null=True, on_delete=models.CASCADE)
    album_name = models.ForeignKey(Album,null=True, on_delete=models.CASCADE)
    places = models.CharField(max_length=100, null=True)
    things = models.CharField(max_length=100, null=True)

class PostImage(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media_files')
    image = models.FileField(max_length=250, upload_to='post/', null=True)

class TrashPost(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='trash')

class ArchivePost(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='archive')

class FavouritePost(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favourite')

class UserShare(Base):
    shared_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='shared_by_me')
    shared_to = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='shared_with_me')
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
