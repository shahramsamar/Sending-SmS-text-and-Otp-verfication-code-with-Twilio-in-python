# Sending SMS Text and OTP Verification Code with Twilio in Python 

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Twilio](https://img.shields.io/badge/Twilio-SMS-red)

 This repository provides a Python-based implementation for sending SMS text messages and OTP (One-Time Password) verification codes using the Twilio API. Perfect for integrating two-factor authentication (2FA) or SMS notifications in your Python applications. 

 ## 📜 Features 

- **Send SMS Text Messages**: Easily send SMS to any mobile number. 
- **Generate OTP Codes**: Securely generate and send OTP codes. 
- **OTP Verification**: Validate OTP codes entered by the user. 
## 📋 Prerequisites 

 Before running the project, ensure you have: 

1. Python 3.6 or higher. 
 2. A [Twilio](https://www.twilio.com) account with:
   - Account SID 
   - Auth Token 

 ### Twilio Setup 

1. Sign up on [Twilio](https://www.twilio.com/try-twilio) and obtain your credentials (Account SID and Auth Token).
2. 2. Verify the phone numbers you want to use for sending and receiving SMS messages in the Twilio Console. 

 ## 🚀 Installation 

 1. **Clone the repository**: 
   ```bash 
         git clone https://github.com/shahramsamar/Sending-SmS-text-and-Otp-verfication-code-with-Twilio-in-python
         cd Sending-SmS-text-and-Otp-verfication-code-with-Twilio-in-python 
          ``` 

 2. **Install dependencies**: 
   ```bash 
   pip install -r requirements.txt
   ``` 

## ⚙️ Configuration 

1. Export your Twilio credentials as environment variables: 
    ```bash 
    export TWILIO_ACCOUNT_SID='your_account_sid' 
    export TWILIO_AUTH_TOKEN='your_auth_token'
    ``` 

 2. In `send_sms.py`, set the `from_` parameter to your Twilio phone number: 
    ```python 
    from_="your_twilio_phone_number" 
    ``` 

 ## 📝 Usage 

 ### Sending an SMS Message 

 To send a simple SMS text message: 

 ```python 
 from send_sms import send_text_message 

 # Replace with recipient's phone number and your message 
 recipient = "+1234567890" 
 message = "Hello! This is a test message from Twilio." 

 send_text_message(recipient, message) 
 ``` 

 ### Sending and Verifying an OTP 

 To send and verify an OTP code: 

 ```python 
 from otp_verification import send_otp, verify_otp 

 # Replace with recipient's phone number 
 recipient = "+1234567890" 

 # Send OTP 
 otp_code = send_otp(recipient) 
 print(f"OTP sent to {recipient}") 

 # Prompt user to enter the OTP received 
 user_otp = input("Enter the OTP you received: ") 

 # Verify OTP 
 if verify_otp(otp_code, user_otp): 
     print("✅ OTP verification successful!") 
 else: 
     print("❌ OTP verification failed.") 
 ``` 

 ## 📁 Project Structure 

 - `send_sms.py`: Contains the `send_text_message` function to send SMS messages. 
 - `otp_verification.py`: Contains functions for OTP generation, sending, and validation. 
 - `requirements.txt`: Lists required Python packages. 
 - `README.md`: Project documentation. 

 ## ⚠️ Important Notes 

 - **Twilio Trial Account**: If you're using a Twilio trial account, you can only send SMS to verified phone numbers. 
 - **SMS Charges**: Twilio charges per SMS message sent. Check Twilio's pricing page for details. 

 ## 🛠️ Troubleshooting 

 1. **Invalid Phone Numbers**: Ensure the phone numbers are in the correct format (E.164 format). 
 2. **Twilio API Errors**: Verify your Twilio credentials and ensure your phone numbers are verified (if using a trial account). 
 3. **Environment Variables**: If you face issues with environment variables, consider hardcoding the values temporarily for testing. 

 ## 🧑‍💻 Author 

 Developed by [Shahramsamar](https://github.com/shahramsamar). For any questions or support, reach out at [shahramsamar2010@gmail.com](mailto:shahramsamar2010@gmail.com). 

 ## 📜 License 

 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 

 ## 🙌 Acknowledgements 

 - [Twilio API Documentation](https://www.twilio.com/docs/usage/api) - For providing SMS and OTP functionality. 
 - [Python Requests Library](https://requests.readthedocs.io/) - For seamless HTTP requests to Twilio's API. 

 --- 
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")

 Happy coding! 🚀 

