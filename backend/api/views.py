from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import getID
from .preprocess import *

# Create your views here.
i = 0

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
            global i
        #try:
            # parse white chars
            mhtml = request.data['mhtml'].replace("\\r\\n", "\n")
            mhtml = mhtml.replace("\\t", "\t")
            mhtml = mhtml.replace("\\\"", "\"")
            mhtml = mhtml.replace("\\\"", "\"")
            mhtml = mhtml.replace("\\\'", "\'")

            data = {"mhtml" : mhtml}
            filename = f"img{i}.mth"
            
            f = open(filename, "w")
            f.write(data['mhtml'])
            save_images(filename)
            i += 1

            return Response({"message" : "task have been submmited sucessfully", 
                            "ID" : getID()}, status="200")

       # except Exception as e:
            return Response({"help" : "mhtml must be included ! "}, status="400")
