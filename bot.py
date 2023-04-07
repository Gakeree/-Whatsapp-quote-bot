from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/mybot', methods=['POST'])

def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp= MessagingResponse()
    msg = resp.message()
    responded= False
    if 'hi' in incoming_msg:
        #Return a gesture or hello to sender
        msg.body("Hello, I am your Bot")
        responded=True

    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data =r.json()
            quote = f'{data["content"]} ({data["author"]})'

        else:
            quote= 'Sorry I am unable to retrieve quote at this time, try later'
        msg.body(quote)
        responded= True


    if 'who are you' in incoming_msg:
        msg.body("Hi I am your Quote bot")
        responded=True

    if not responded:
       msg.body("Hi I can only tell about qoute and myself")
    return str(resp)

if __name__ =="__main__":
     app.run() 