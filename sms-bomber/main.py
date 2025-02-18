import os
import logging
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from the .env file
load_dotenv()

# Retrieve Twilio API credentials from the .env file
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
recipient_phone = os.getenv('RECIPIENT_PHONE_NUMBER')

# Check if all necessary environment variables are available
if not all([account_sid, auth_token, twilio_phone_number, recipient_phone]):
    logger.error("Missing required environment variables. Please check your .env file.")
    exit(1)

# Initialize Twilio Client
client = Client(account_sid, auth_token)

def send_sms(to_phone, message):
    """
    Sends SMS message using the Twilio API.
    Args:
        to_phone (str): The phone number to send the SMS to.
        message (str): The message content to send.
    """
    try:
        # Send SMS
        logger.info(f"Sending message to {to_phone}...")
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=to_phone
        )
        logger.info(f"Message sent successfully! SID: {message.sid}")
    except TwilioRestException as e:
        logger.error(f"Twilio error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to send a series of test messages.
    """
    message = 'This is a test message! It is SMS Sender not Bomber'
    
    for i in range(5):  # Send 5 test messages
        logger.info(f"Attempt {i+1}/5:")
        send_sms(recipient_phone, message)

if __name__ == "__main__":
    main()
