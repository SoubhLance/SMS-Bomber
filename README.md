# SMS Bomber

A simple SMS Bombing tool built using Python. This tool sends a large number of SMS messages to a given phone number. **Note**: Use this tool responsibly and legally. Do not use it to cause harm, harassment, or break any terms of service agreements.

## Important 🚨 Notes⚠️:
### This tool is strictly for educational purposes only. It is not intended for malicious use or to cause harm in any way. Please use it responsibly and ensure that it complies with legal regulations and terms of service. The author is not responsible for any misuse of this tool.
- Do not use this tool for malicious purposes. Sending unsolicited messages may be illegal in your country.
- Always respect the privacy and consent of others.
- The `.env` file is not visible on GitHub due to security concerns. Ensure you store your keys and sensitive data in this file securely.

---

## Features
- Send multiple SMS messages to a given phone number.
- Configurable number of messages to send.
- Uses external services to send SMS.

---

## Data Structures Used

1. **Dictionary**: For storing configuration settings like API keys, phone number, and message content.
2. **List**: Used to maintain a list of message content or phone numbers for future modifications.
3. **String**: Used to represent phone numbers and messages.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SoubhLance/SMS-Bomber.git
cd SMS-Bomber
```
2. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```
3. Directory Structure📂:
```bash
   msg-bomber/
   ├── main.py
   ├── .env
   ├── .gitignore
   └── README.md
```

4. Set up the environment file `(.env)`:
- Create a `.env` file in the root directory of the project
- Add sensitive information such as API keys in this file. This file is `ignored` in the repository for security reasons.
Example: 
```ini
API_KEY
TWILIO_ACCOUNT_SID="your_api_key_here"
TWILIO_AUTH_TOKEN=="your_api_key_here"
TWILIO_PHONE_NUMBER="+1XXXXXXXXXX" 
RECIPIENT_PHONE_NUMBER="++12XXXXXXXX"

```
## Usage
- Ensure that you have a valid API key from a service that allows sending SMS.
- Set up your `.env` file with the appropriate credentials.
- Run the script:

```bash
python sms_bomber.py

```
### You will be prompted to enter the target phone number and the number of messages to send.

## ScreenShot
   ![WhatsApp Image 2025-02-18 at 19 23 38_962318e9](https://github.com/user-attachments/assets/47493daf-a5c2-45db-8882-d8b0b43cfd15)

## Contributing
  If you have any improvements or suggestions, feel free to fork the repository and submit a pull request. Contributions are always welcome!

## License
  This project is open-source and available under the MIT License.
  ```CSHARP
    You can copy this and paste it into your `README.md` file!
```

## Support

If you have any questions, issues, or need assistance with this project, feel free to reach out!

- Email : [studysadhu2022@gmail.com](mailto:studysadhu2022@gmail.com)




