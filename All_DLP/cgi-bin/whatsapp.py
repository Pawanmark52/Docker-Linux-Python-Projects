#!/usr/bin/env python3
import cgi
import cgitb
from twilio.rest import Client
import json

# Enable CGI error reporting
cgitb.enable()

# Get form data
form = cgi.FieldStorage()
account_sid = 'Enter your Twilio Account SID here'  # Be cautious with hardcoding sensitive information
auth_token = 'Enter your Twilio Auth Token here'  # Be cautious with hardcoding sensitive information
twilio_whatsapp_number = 'Enter your Twilio WhatsApp number here'  # Be cautious with hardcoding sensitive information
recipient_number = form.getvalue('recipient_number')
message_body = form.getvalue('message_body')

# Set the content type to application/json
print("Content-Type: application/json\n")

response = {}

if not all([account_sid, auth_token, twilio_whatsapp_number, recipient_number, message_body]):
    response['error'] = 'All fields are required.'
else:
    try:
        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # Send WhatsApp message
        message = client.messages.create(
            body=message_body,
            from_=f'whatsapp:{twilio_whatsapp_number}',
            to=f'whatsapp:{recipient_number}'
        )
        response['message'] = 'Message sent successfully!'
        response['sid'] = message.sid
    except Exception as e:
        response['error'] = str(e)

# Output the result as JSON
print(json.dumps(response))

