#Leia os seguintes textos: 
#https://medium.com/@kshitijvijay271199/flask-on-google-colab-f6525986797b
#https://hackersandslackers.com/flask-routes/
#
#Após executar este código, vão ser impressas as linhas abaixo:
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Running on http://[código randomico].ngrok.io
# * Traffic stats available on http://127.0.0.1:4040
#a url da 2 linha poderá ser acessada direto do navegador, 
#será exibida uma página escrito: "Hello, World!".
#
#Teste ainda as urls (execute mais de uma vez a última URL):
#http://[código randomico].ngrok.io
#http://[código randomico].ngrok.io/hi
#http://[código randomico].ngrok.io/hi/rachel
#http://[código randomico].ngrok.io/hi/joe
#http://[código randomico].ngrok.io/classify
#http://[código randomico].ngrok.io/classify?student=joe

from flask import Flask
from flask import request
from flask import jsonify
import requests
import numpy as np
import random

def ml_classifier(student):
  classes = ["A","B","C","D"]
  return random.choice(classes)

app = Flask(__name__)

@app.route('/')
@app.route('/hi')
@app.route('/hi/<album>/<id>')
def hi(album = None, id):
  if (param is None):
    return "Hi! How are you?!"
  elif (param != "joe"):
    return "Hi, I'm {}. How are you?!".format(param.capitalize())
  else:
    return "How you doin'?"

@app.route('/student/classify', methods = ['POST', 'GET'])
def classify_student(student):
  student = request.args.get('student')
  student = request.args.get('genero')
  student = request.args.get('cor')
  if ((student is None) or (len(student) == 0)):
    return jsonify({"error": "Invalid Student."})
  else:
    student_class = ml_classifier(student)
    student_json = {"student_name": student,
                    "student_class": student_class,
                    "response_time": now()}
    return jsonify(student_json)
    
app.run()
