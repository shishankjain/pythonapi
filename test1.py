from flask import Flask
from flask_restful import Resource, Api
 
app=Flask(__name__)
api= Api(app)

class HelloWorld (Resource):
  def __init__ (self):
    pass

  def get (self):
    return{
      "Hello": "World"
    }

if __name__ == "__main__":
  app.run(debug=True)