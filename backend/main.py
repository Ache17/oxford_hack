from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from random import choice


ID_size = 32

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
parser = reqparse.RequestParser()

app.config["CORS_HEADERS"] = "Content-Type"

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
    @cross_origin()
    def get(self):
        return {"hello" : "world"}

    @cross_origin()
    def post(self):
        args = parser.parse_args()
        return {"message" : "ok fine", "test" : "test"}, 201


class imageCaption(Resource):
    @cross_origin()
    def get(self):
        request.get_json(force=True)
        args = imageCaptionGETParser.parser_args()
        return {"html" : get_parsed_html()}

    @cross_origin()
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
