from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import getID
from .preprocess import *

# Create your views here.
i = 0
queue   = {}
results = {}

debug = True


class TestView(APIView):
    def get(self, request):
        content = {"Hello" : "world"}
        return Response(content)

    def post(self, request):
        content = {"this " :" is another message"}
        return Response(content)

class Caption(APIView):
    def get(self, request):

        ID = None
        try:
            ID = request.data["ID"]
        except KeyError as e:
            return Response({"help" : "ID must be specified"})

        try:
            result = results[ID]
        except KeyError as e:
            return Response({"help" : "ID is not valid or result is not valid", "done" : "no"})

        
        return Response({"result" : result, "done" : "yes"})


    def post(self, request):
        global i, results
        try:
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
            number_of_images = save_images(filename)
            i += 1

            ID = getID()
            results[ID] = ["Lorem ipsum"] * number_of_images

            if debug:
                print(ID)

            return Response({"message" : "task have been submmited sucessfully",  "ID" : ID}, status="200")

        except KeyError as e:
            return Response({"help" : "mhtml must be included ! "}, status="400")

        except Exception as e:
            return Response({"help" : "sorry the website couldn't be parsed"}, status="400")