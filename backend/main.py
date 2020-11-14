from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from random import choice


ID_size = 32

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

imageCaptionPOSTParser = reqparse.RequestParser()
imageCaptionPOSTParser.add_argument("website", type=str, help="please include 'website' with source of the html to caption", required=True)

imageCaptionGETParser = reqparse.RequestParser()
imageCaptionGETParser.add_argument("ID", type=str, help="include ID that were give to you while submitting the job" , required=True)


def getRandomID():
    return "".join([choice("0123456789") for _ in range(ID_size)])

def get_parsed_html():
    return "here goes the parsed html website"

def submit_to_calculation():
    ID = getRandomID()
    return ID 


class imageCaptionTest(Resource):
    def get(self):
        return {"hello" : "world"}

    def post(self):
        args = parser.parse_args()
        return {"message" : "ok fine", "test" : "test"}, 201


class imageCaption(Resource):
    def get(self):
        request.get_json(force=True)
        args = imageCaptionGETParser.parser_args()
        return {"html" : get_parsed_html()}

    def post(self):    
        request.get_json(force=True)
        args = imageCaptionPOSTParser.parse_args()
        print(args)

        # submit to some queing system 
        ID = submit_to_calculation()

        return {"message" : "Sucessfully uploaded task to API", "ID" : ID}, 201


api.add_resource(imageCaptionTest, "/")
api.add_resource(imageCaption, "/api/caption")

if __name__ == "__main__":
    app.run(debug=True)
