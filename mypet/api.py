from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloMyPet(APIView):
    def get( self, request):

        try:


            users = User.objects.all()

            if len(users) == 0:

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'multipass': True,
                        'detail':'No hay usuarios registrados'
                    }
                )
            else:

                is_owner = False

                for element in users:
                    if element.is_superuser:
                        is_owner = True

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'multipass': True,
                        'detail':'Hay usuarios en la db',
                        'owner' : is_owner
                    }
                )

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'multipass': True,
                    'detail':'Ok'
                }
            )



        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'multipass': False,
                    'detail':'Bad request'
                }
            )

    def post(self,request):

        try:

            user = request.user

            if user.id is None:

                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'multipass':False,
                        'detail':'Primero debes iniciar sesión'
                    }
                )

            else:

                users = User.objects.all()

                owner = False

                for elements in users:

                    if elements.is_superuser:
                        owner = True
                        

                if owner:

                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            'multipass': False,
                            'detail':'¡Already have an owner!'
                        }
                    )
                else:

                    newSuperuser = User.objects.get(id=user.id)
                    print('ASIGNANDO OWNER', newSuperuser)

                    newSuperuser.is_superuser = True
                    newSuperuser.is_staff = True
                    newSuperuser.save()

                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            'multipass': True,
                            'detail':'¡You got me!'
                        }
                    )
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'multipass': False,
                    'detail':'Bad request'
                }
            )

    def delete(self,request):

        try:

            user = request.user

            if user.id is None:

                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'multipass':False,
                        'detail':'Primero debes iniciar sesión'
                    }
                )

            else:
                        
                newSuperuser = User.objects.get(id=user.id)
                print('ELIMINAR OWNER', newSuperuser)

                newSuperuser.is_superuser = False
                newSuperuser.is_staff = False
                newSuperuser.save()

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'multipass': True,
                        'detail':'¡Good bye, Owner!'
                    }
                )
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'multipass': False,
                    'detail':'Bad request'
                }
            )


