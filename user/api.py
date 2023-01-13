from .models import CustomUser
from .serializers import UserSerializer, CustomUserSerializer

from django.contrib.auth.models import User

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

class UserViewset(APIView):

    def get(self, request):

        try:


            try:

                requestUser = request.user
                requestUser.is_superuser
                serialized = UserSerializer(requestUser)

                perfil = CustomUser.objects.get(id=requestUser.id)
                perfilSerialized = CustomUserSerializer(perfil)

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "detail": "User detected",
                        "data": serialized.data,
                        "profile": perfilSerialized.data,
                        "isAdmin": requestUser.is_superuser
                    }
                )
                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            

                

            
        except:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )


    def post(self, request):

        #1 Crear usuario nuevo
        #2 Relacionar con perfil
        #3 Guardar IP en el perfil
        
        forwarded = request.META.get('HTTP_X_FORWARDER_FOR')
        if forwarded:
            ip = forwarded.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        data = request.data
        print(data)
        serialized = UserSerializer(data=data)


        if serialized.is_valid():
            serialized.save()
            user = User.objects.get(username=data['username'])
            user.set_password(data['password'])
            user.save()

            perfil = CustomUserSerializer(data={'location':ip})
            if perfil.is_valid():
                perfil.save()


            return Response(
                status = status.HTTP_200_OK,
                data={
                    "multipass":True,
                    "data": {
                        "User":serialized.data ,
                        "perfil": perfil.data
                    }
                }
            )
                
        return Response(
            status = status.HTTP_400_BAD_REQUEST,
            data={
                "multipass":False,
                "detail": serialized.errors
            }
        )


