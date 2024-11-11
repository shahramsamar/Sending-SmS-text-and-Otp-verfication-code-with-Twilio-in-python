from twilio.rest import Client
from dotenv import load_dotenv
import os 

load_dotenv()

account_sid = os.getenv('env_account_sid')
auth_token = os.getenv('env_auth_token')
phone_number = os.getenv('env_phone_number')

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12',
  body='hi',
  to='phone_number'
)

print("SMS has been sent")
print(message.sid)

