"""
Python Program to create a simple API
to create a JSON based on the GET method data provided

Using flask framework and time module for generating timestamps

Usage:
Run the program.
for testing purposes, a local server is created and with the port default 5000

Sample Input: (from a web client, curl, etc)
http://127.0.0.1:5000/request/

http://127.0.0.1:5000/


Sample Output:
{
  "Page": "Request", 
  "Timestamp": 1653405094.7468941, 
  "User": "None"
}

{
  "Message": "Printed", 
  "Page": "Home", 
  "Timestamp": 1653405851.4336889
}
"""

from flask import *
import time

#creating app using Flask constructor and __name__ as argument
app=Flask(__name__)

#creating a decorator so that it calls when a specific type of GET call is generated.
#here it is the '/' home directory
@app.route('/',methods=['GET'])
def apiGet():
    data_set= {'Page':'Home','Message':'Printed','Timestamp':time.time()}
#returns a JSON 
    return jsonify(data_set)

#when the /request/ directory is called, it returns an according JSON 
@app.route('/request/',methods=['GET'])
def apiUserQuery():
    userQuery=str(request.args.get('user'))
    data_set= {'Page':'Request','User':f'{userQuery}','Timestamp':time.time()}
    return jsonify(data_set)  

#the created program runs before any other execution
if __name__=="__main__":
    #app.debug = True
    app.run()
