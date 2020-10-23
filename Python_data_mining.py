
#THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM AN API ENDPOINT
from flask import Flask
import requests
app = Flask(__name__)

#GET REQUEST

@app.route('/readHello')
def getRequestHello():
        #response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDqvy2NJkLllhXPQgVRBwR6Kyf8JXWpW3M")
        response = response = requests.get("http://api.open-notify.org/astros.json")
        response_json = response.json() 
        response_code = response.status_code
        response_message = response_json['message']
        response_people = response_json['people']
        response_number = response_json['number']

        container = [response_message, response_people, response_number]
        for side in container:
            if side == response_people:
                    for person in side:
                            for cell in person:
                                    print(cell)
                                    print(" ")                                    
                            print(person)
                            print("  ")
                    print(" ----------------")
                    print(side)
                    print("----------------")
	return str(response_code)


#POST REQUEST
@app.route('/createHello', methods = ['POST'])
def postRequestHello():
	return "I see you sent a POST message :-)"
#UPDATE REQUEST
@app.route('/updateHello', methods = ['PUT'])
def updateRequestHello():
	return "Sending Hello on an PUT request!"

#DELETE REQUEST
@app.route('/deleteHello', methods = ['DELETE'])
def deleteRequestHello():
	return "Deleting your hard drive.....haha just kidding! I received a DELETE request!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
