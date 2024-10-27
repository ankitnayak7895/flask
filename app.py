# create a simple flask apllication
from flask import Flask,render_template  

# create the flask app

app=Flask(__name__)

# create the url

@app.route('/')
def home():
      return 'This is the flask page'

@app.route('/welcome')
def welcome():
      return '<h1> welcome to this page </h1>'

@app.route('/index')
def index():
      return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
      print(type(score))
      return "the score is:"+str(score) 

@app.route('/fail/<int:score>')
def fail(score):
      return 'the person is fail and the score is'+ str(score)

@app.route('/check/<int:score>')
def check(score):
      if score > 50:
            return 'the person is pass and the score is'+str(score)
      else:
            return 'the person is fail and the score is '+str(score)


if __name__=='__main__':
      app.run(debug=True)
      
