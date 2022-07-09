from account.models import CustomUser
from feed.models import Album, Folder, Post, PostImage
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    folder_name = serializers.SerializerMethodField()
    album_name = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    media_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_user(self , obj):
        try:
            user = CustomUser.objects.get(id=obj.user.id)
            return user.username
        except :
            return None

    def get_folder_name(self,obj):
        try:
            folder_obj = Folder.objects.get(id=obj.folder.id)
            return folder_obj.folder_name
        except :
            return None

    def get_album_name(self,obj):
        try:
            album_obj = Album.objects.get(id=obj.folder.id)
            return album_obj.album_name
        except :
            return None

    def get_media_url(self,obj):
        
            image_urls = []
            post_obj = PostImage.objects.filter(post=obj.id)
            print(post_obj)
            if len(post_obj) == 0:
                return None
            else:
                for i in post_obj:
                    image_urls.append(i.image.url)

            return image_urls
        

class FolderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Folder
        fields = '__all__'

    def get_user(self , obj):
        try:
            user = CustomUser.objects.get(id=obj.user.id)
            return user.username
        except :
            return None

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    def get_user(self , obj):
        try:
            user = CustomUser.objects.get(id=obj.user.id)
            return user.username
        except :
            return None