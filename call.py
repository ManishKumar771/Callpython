from twilio.rest import Client

# Twilio credentials (get from Twilio console)
account_sid = 'account_sid'
auth_token = 'your_auth'
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    twiml='<Response><Say>Hello, this is an automated call from Python!</Say></Response>',
    to='+91your_no.',     # Your phone number with country code
    from_='+12314344553'    # Your Twilio phone number
)

print(f"Call initiated! SID: {call.sid}")
