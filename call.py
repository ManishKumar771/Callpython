import os
import time
from datetime import datetime

# =============================================================================
# 1. MAKING PHONE CALLS
# =============================================================================

# Method 1: Using Twilio API (Recommended - Professional)
def make_phone_call_twilio():
    """
    Make a phone call using Twilio API
    Requires: pip install twilio
    """
    try:
        from twilio.rest import Client
        
        # Your Twilio credentials (get from twilio.com)
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        twilio_phone_number = 'your_twilio_phone_number'
        
        client = Client(account_sid, auth_token)
        
        call = client.calls.create(
            to='+1234567890',  # Recipient's phone number
            from_=twilio_phone_number,
            url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL for call instructions
        )
        
        print(f"Call initiated with SID: {call.sid}")
        return call.sid
        
    except Exception as e:
        print(f"Error making call: {e}")
