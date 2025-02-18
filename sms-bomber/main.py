import os
import logging
import requests
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from the .env file
load_dotenv()

# Retrieve Fast2SMS API credentials
fast2sms_api_key = os.getenv('FAST2SMS_API_KEY')
recipient_phone = os.getenv('RECIPIENT_PHONE_NUMBER')

# Check if all necessary environment variables are available
if not all([fast2sms_api_key, recipient_phone]):
    logger.error("Missing required environment variables. Please check your .env file.")
    exit(1)

def send_sms(to_phone, message):
    """
    Sends SMS message using Fast2SMS API.
    Args:
        to_phone (str): The phone number to send the SMS to.
        message (str): The message content to send.
    """
    try:
        url = "https://www.fast2sms.com/dev/bulkV2"
        headers = {
            "authorization": fast2sms_api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "route": "q",  # For transactional messages
            "message": message,
            "language": "english",
            "flash": 0,
            "numbers": to_phone
        }

        response = requests.post(url, headers=headers, data=payload)
        response_data = response.json()

        if response_data.get("return"):
            logger.info(f"Message sent successfully to {to_phone}")
        else:
            logger.error(f"Failed to send message: {response_data}")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to send a series of test messages.
    """
    message = "This is a test message!"
    
    for i in range(5):  # Send 5 test messages
        logger.info(f"Attempt {i+1}/5:")
        send_sms(recipient_phone, message)

if __name__ == "__main__":
    main()
