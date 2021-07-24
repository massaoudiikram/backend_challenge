from flask import Flask
from flask_restful import Api, Resource

import application
app = Flask(__name__)
api = Api(app)
                                                                                                            
class GitHub(Resource):
    def get(self):

        res = application.trending_repos()
        return res

api.add_resource(GitHub, "/trending_language")

if __name__ == "__main__":
	app.run(debug=True)