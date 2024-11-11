from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
phone_number = os.getenv('PHONE_NUMBER')

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12',
  body='hi',
  to='phone_number'
)

print("SMS has been sent")
print(message.sid)

