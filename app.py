# import flask dependencies
from flask import Flask, request, make_response, jsonify
from connector import *
import requests
from transfers import *

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!, welcome to beanstalk application'

# function for responses
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    #print(req)

    # fetch action from json
    action = req.get('queryResult').get('action')
    query=req.get('queryResult').get('queryText')
    #print(action)
    d=req.get('queryResult').get('parameters')
    intent=req.get('queryResult').get('intent').get('displayName')
    entity1=d[action]
    entity2=None
    try:
        entity2=d['state']
    except:
        pass
        #print("exception")
    # return a fulfillment response
    if entity2=="" or entity2==" ":
        entity2=None
    #print(entity2+"shiva")
    conn=None
    resp=""
    ans=""
    midway="http://govtservicebot-env.gmbkdsizsc.us-east-2.elasticbeanstalk.com/midway.php?q="
    if(entity2!=None):
        conn=connector(intent,entity1,query,entity2)
    else:
        conn=connector(intent,entity1,query)
    if(intent=='service'):
        ans=conn.getsitelink()
        resp=midway+ans+"&t=0"
    elif(intent=='how'):
        ans=conn.getyoutubelink()
        resp=midway+ans+"&t=1"
    else:
        resp="sry, I did not get you and I am still learning."
    if(ans=="nope"):
        resp="sry, we cannot find the appropriate link in our database"
        print(resp)
        return jsonify({'fulfillmentText':resp})
    print(resp)
    return jsonify({
      "fulfillmentText": resp,
      "fulfillmentMessages": [
        {
          "card": {
            "title": entity1,
            "imageUri": "",
            "buttons": [
              {
                "text": "Click here",
                "postback": resp
              }
            ]
          }
        }
      ]})
    #return "webhook"

# create a route for webhook
'''@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))'''
@app.route('/transfer', methods=['GET'])
def transfer():
    #req=request.get_json(force=True)
    trans=transfers()
    #trans.dotransfer()
    pwd=request.args['pwd']
    if pwd=='kumar123':
        trans.dotransfer()
        return "success"
    else:
        return "failed"    
# run the app
if __name__ == '__main__':
   app.run()
