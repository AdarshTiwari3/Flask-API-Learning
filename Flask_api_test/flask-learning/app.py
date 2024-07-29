from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask! This is Adarsh'

if __name__ == '__main__': #this will run the server, main function
    app.run(debug=True) #debug=True will restart the server whenever we make changes