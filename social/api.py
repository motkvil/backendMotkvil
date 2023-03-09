from .models import SocialNetwork, NewsModel, ViewsModel, VisitModel
from .serializers import SocialSerializer, ViewsSerializer, NewsSerializer, VisitSerializer
from user.models import CustomUser

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

class SocialViewset(APIView):

    def get(self, request):

        try:

            social = SocialNetwork.objects.all()
            serialized = SocialSerializer(social, many=True)

            print(request.user.id)

            forwarded = request.META.get('HTTP_X_FORWARDER_FOR')
            if forwarded:
                ip = forwarded.split(',')[0]
                print('IF IP: ', ip)
            else:
                ip = request.META.get('REMOTE_ADDR')
                print('ELSE IP: ', ip)


            return Response(
                status = status.HTTP_200_OK,
                data = {
                    "multipass" : True,
                    "data" : serialized.data
                }
            )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def post(self, request):

        data = request.data
        serialized = SocialSerializer(data=data)

        print('Data ======>', data)

        if serialized.is_valid():
            serialized.save()

            return Response(
                status = status.HTTP_200_OK,
                data={
                    "multipass":True,
                    "data": {
                        "article": serialized.data,
                    }
                }
            )
                
        else:
            return Response(
                status = status.HTTP_400_BAD_REQUEST,
                data={
                    "multipass":False,
                    "detail": serialized.errors
                }
            )


class NewsView(APIView):


    def get(self,request):

        try:

            news = NewsModel.objects.all()
            serialized = NewsSerializer(news, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass':True,
                    'data': serialized.data
                }
            )

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'multipass':False
                }
            )

    def post(self,request):

        try:

            data = request.data
            user = request.user

            serialized = NewsSerializer(data=data)

            if serialized.is_valid():
                serialized.save()


                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'user': user.username,
                        'data': serialized.data
                    }
                )
            
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'multipass':False,
                        'detail': serialized.errors
                    }
                )
                
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class ViewsView(APIView):

    def get(self,request):

        try:

            serialized = ViewsSerializer(ViewsModel.objects.all(), many=True)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass':True,
                    'data': serialized.data
                }
            )
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self,request):

        try:


            user = request.user
            view = ViewsModel.objects.create()
            print(view)
            if user.id is not None:
                view.user.add(CustomUser.objects.get(id=user.id))
                view.save()
            
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass':True,
                    'data': view.title
                }
            )

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class ViewVisit(APIView):

    def get(self,request):

        try:

            data = VisitModel.objects.all()
            serialized = VisitSerializer(data, many=True)
            

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass':True,
                    'data': serialized.data
                }
            )

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def post(self,req):
        try:

            print(req.data['ip'])
            data = req.data

            

            serialized = VisitSerializer(data=data)
            if serialized.is_valid():

                new = data['ip']
                current = VisitModel.objects.all()
                print(current)

                for item in current:
                    print(item.ip)
                    if item.ip == new:
                        print("Borrando registro duplicado")
                        item.delete()
                
                    
                serialized.save()

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'multipass':True,
                        'data': "I got you!"
                    }
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'multipass':False,
                        'data': "Serialized no es valido"
                    }
                )
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )







