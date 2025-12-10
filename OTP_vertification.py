import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("env_account_sid")
auth_token = os.getenv("env_auth_token")
phone_number = os.getenv("env_phone_number")
verify_sid = os.getenv("env_verify_sid")

client = Client(account_sid, auth_token)

otp_verification = client.verify.services(verify_sid).verifications.create(
    to=phone_number, channel="sms"
)

print(otp_verification.status)
otp_code = input("Please enter your OTP sent to you:")

otp_verification_check = client.verify.services(verify_sid).verification_checks.create(
    to=phone_number, code=otp_code
)
print(otp_verification_check)
