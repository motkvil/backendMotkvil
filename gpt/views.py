from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

import openai 
import os

# Create your views here.


class gptChat (APIView):

  def post(self,request):

    content = request.data['content']
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # response = openai.Model.list()
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages = [
        {
          "role": "user",
          "content": content
        }
      ]
    )

    print(response)

    return Response(
      status= status.HTTP_200_OK,
      data={
        'detail': response.choices[0].message
      }
    )

