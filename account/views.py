from django.shortcuts import render
from account.models import CustomUser, Profession
from account.serializers import ProfessionSerializer, UserSerializer
from django.contrib.auth import authenticate, login
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
class UserAuthView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def signup(self,request):
        try:
            data = request.data
            validate, msg = validate_data(data)
            if validate:
                user = register_user(data)
                
                if not user:
                    return Response(
                        data={'status': False, 'message': "User already exists"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
 
                token = get_tokens_for_user(user)
                return Response(
                    data={'status': True, 'message': 'Authentication successfull', 'token': token}, 
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    data={'status': False, 'message': msg}, 
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST)

    def login(self,request):
        emailid = request.data.get('emailid')
        password = request.data.get('password')
        try:
            username = CustomUser.objects.get(email=emailid)
        except Exception:
            return Response(
                    data={'status': False, 'message': 'It seems that you have entered an incorrect Username'}, 
                    status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response(
                    data={'status': False, 'message': 'It seems that you have entered an incorrect Username or Password'}, 
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            token = get_tokens_for_user(user)
            return Response(
                    data={'status': True, 'message': 'Authentication successfull', 'token': token}, 
                    status=status.HTTP_200_OK)
                    
    def get_profession(self,request):
        dt = Profession.objects.all()
        res = ProfessionSerializer(dt, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )


class UserAuthenticateView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_user_profile(self,request):
        """
        Get my profile
        """
        try:
            user = request.user
            # TODO check user login status for consecutive days.
            data = UserSerializer(user, context={"request": request}).data
            return Response(
                        data={'status': True, 'data': data}, 
                        status=status.HTTP_200_OK
                    )
        except Exception as e:
            return Response(
                        data={'status': True, 'message': str(e)}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )

    def update_profile(self,request):
        user = request.user
        data = request.data
        first_name = data.get("f_name",None)
        last_name = data.get("l_name",None)
        dob = data.get("dob",None)

        if first_name:
            user.first_name = first_name
            user.save()
        if last_name:
            user.last_name = last_name
            user.save()
        if dob:
            user.dob = dob
            user.save()
        return Response(
            data={'status': True, 'data': "Updated Successfully"}, 
            status=status.HTTP_200_OK
        )
    
    def update_profile_image(self,request):
        parser_classes = [MultiPartParser, FileUploadParser]
        user = request.user
        data = request.data
        profile_image = data.get("profile_image", None)
        print(profile_image)
        if profile_image:
            user.profile_photo = profile_image
            user.save()
            return Response(
            data={'status': True, 'data': "Updated Successfully"}, 
            status=status.HTTP_200_OK
        )
        else:
            return Response(
            data={'status': False, 'data': "No image found"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
        
