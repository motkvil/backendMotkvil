from .models import Service
from .serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser
from rest_framework.decorators import APIView


class ServiceView(APIView):

    def get(self, request):

        myServices = Service.objects.all()
        serialized = ServiceSerializer(myServices, many=True)

        try:

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass': True,
                    'data':serialized.data
                }
            )

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


    def post(self, request):

        data = request.data
        userRequest = request.user
        serialized = ServiceSerializer(data=data)

        if userRequest.id is None:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'multipass': False,
                    'data': 'Inicia Sesión'
                }
            )

        else:

            if serialized.is_valid():
                serialized.save()

                user = CustomUser.objects.get(id=request.user.id)
                service = Service.objects.get(id=serialized.data['id'])

                service.teachers.add(user)
                service.save()

                return Response(
                    status = status.HTTP_200_OK,
                    data={
                        "multipass":True,
                        "data": serialized.data
                    }
                )

            else:
                return Response(
                    status = status.HTTP_400_BAD_REQUEST,
                    data={
                        "multipass":False,
                        "data": serialized.errors
                    }
                )


class MyServicesView(APIView):
    
    def get(self,request):

        try:

            user = request.user
            services = Service.objects.filter(teachers=user.id)

            serialized = ServiceSerializer(services, many=True)

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
                    'multipass':False,
                    'data': 'No bi'
                }
            )




