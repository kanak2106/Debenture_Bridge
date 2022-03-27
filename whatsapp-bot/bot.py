from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hi' in incoming_msg:
        # return a gesture or hello to sender
        msg.body(" Hey! I'm from debenture bridge. Nice to see you here. \nPlease verify yourself as:- \nOption 1: Lender \nOption 2: Borrower")
        responded = True

    # lender
    if 'lender' in incoming_msg:
        msg.body("Thank you for your response. \nPlease specify your concern. \n1: I want to lend money. \n2: I want to know the status of the given loan. \n3: I have not received my amount back. \n4: I want to know more about your services. \n5: Others")
        responded = True
    if '1' in incoming_msg:
        msg.body("Sure! \nPlease visit our website and register yourself as a lender and it's a cakewalk. If you feel any queries feel free to text me.")
        responded = True
    if '2' in incoming_msg:
        msg.body("Your loan will be returned at 12% interest till the end of the coming October(as your borrower promised).")
        responded = True
    if '3' in incoming_msg:
        msg.body("Shall connect you to an expert soon.")
        responded = True
    if '4' in incoming_msg:
        msg.body("Sure! \nWe would love to guide you. Please visit (www.debenture-bridge.com) or type your specific question.")
        responded = True
    if '5' in incoming_msg:
        msg.body("Please specify.")
        responded = True

    # borrower
    if 'borrower' in incoming_msg:
        msg.body("Thank you for your response. \nPlease specify your concern. \na: I want to borrow some amount of money. \nb: I want to know the status of my borrowed money. \nc: Facing some technical issues in returning the amount. \nd: I want to know more about your services. \ne: Others")
        responded = True
    if 'a' in incoming_msg:
        msg.body("Sure! \nPlease visit our website and register yourself as a borrower and it's a cakewalk. If you feel any queries feel free to text me.")
        responded = True
    if 'b' in incoming_msg:
        msg.body("You have 2 months left to pay the borrowed amount with 12% interest (as you as a borrower promised)")
        responded = True
    if 'c' in incoming_msg:
        msg.body("Shall connect you to an expert soon.")
        responded = True
    if 'd' in incoming_msg:
        msg.body("Sure! \nWe would love to guide you. Please visit (www.debenture-bridge.com) or type your specific question.")
        responded = True
    if 'e' in incoming_msg:
        msg.body("Please specify.")
        responded = True
    
    # if 'quote' in incoming_msg:
    #     # return a quote
    #     r = requests.get('https://api.quotable.io/random')
    #     if r.status_code == 200:
    #         data = r.json()
    #         quote = f'{data["content"]} ({data["author"]})'
    #     else:
    #         quote = 'I could not retrieve a quote at this time, sorry.'
    #     msg.body(quote)
    #     responded = True

    if not responded:
        msg.body("Sorry for inconvenience. We'll reach you soon")

    return str(resp)

if __name__ == "__main__":
    app.run()