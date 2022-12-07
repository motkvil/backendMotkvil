from .models import SocialNetwork
from .serializers import SocialSerializer

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

class SocialViewset(APIView):

    def get(self, request):

        try:

            social = SocialNetwork.objects.all()
            serialized = SocialSerializer(social, many=True)

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