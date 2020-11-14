from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import getID

# Create your views here.

class TestView(APIView):
    def get(self, request):
        content = {"Hello" : "world"}
        return Response(content)

    def post(self, request):
        content = {"this " :" is another message"}
        return Response(content)

class Caption(APIView):
    def get(self, request):
        print(request)
        return Response({"lol" : "lol"})


    def post(self, request):
        try:
            data = {"mhtml" : request.data['mhtml']}
            print(data['mhtml'])

            return Response({"message" : "task have been submmited sucessfully", 
                            "ID" : getID()})

        except Exception as e:
            return Response({"help" : "mhtml must be included ! "})
