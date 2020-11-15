from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import getID
from .preprocess import *
import traceback

import os
from .inference import evaluate

# Create your views here.
i = 0
queue   = {}
results = {}
done    = {}

debug = True


class TestView(APIView):
    def get(self, request):
        content = {"Hello" : "world"}
        return Response(content)

    def post(self, request):
        content = {"this " :" is another message"}
        return Response(content)

class imageCaptions(APIView):
    def post(self, request):
        ID = None
        try:
            ID = request.data["ID"]
        except KeyError as e:
            return Response({"help" : "ID must be specified"})
        try:
            d = done[ID]
            result = results[ID]
        except KeyError as e:
            return Response({"help" : "ID is not valid or result is not valid", "done" : "no"})
        return Response({"result" : result, "done" : "yes"})

class Caption(APIView):
    def post(self, request):
        global i, results
        try:
            ID = getID()
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
            number_of_images = save_images(filename, ID)
            i += 1

            #results[ID] = ["Lorem ipsum"] * number_of_images
            results[ID] = []

            idPath = './parsed/' + str(ID)
            pictureNames = list(sorted(os.listdir(idPath)))

            for pName in pictureNames:
                picturePath = './parsed/' + str(ID) + '/' + pName
                currentPrediction = evaluate(picturePath)[:-1]
                results[ID].append(' '.join(currentPrediction))

            if debug:
                print(results[ID])
                print(ID)
            done[ID] = True

            return Response({"message" : "task have been submmited sucessfully",  "ID" : ID, "results": results}, status="200")

        except KeyError as e:
            traceback.print_exc()
            return Response({"help" : "mhtml must be included ! "}, status="400")

        except Exception as e:
            traceback.print_exc()
            return Response({"help" : "sorry the website couldn't be parsed"}, status="400")