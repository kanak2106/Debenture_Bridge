# python-whatsapp-bot
This is a Whatsapp Chatbot that responds with messages when they are requested.

# Usage
1. Download and install Python3.

2. Clone or fork this repository (project).
    ```
    $ git clone https://github.com/aham-18113/whatsapp-bot.git

    $ cd python-whatsapp-bot
    ```

2. Create a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) inside this project directoy e.g.,
    ```
    python -m venv whatsapp-bot-venv
    ```
    Then activate that environment:
    ```
    Windows: whatsapp-bot-venv\Scripts\activate

    Mac: $ source whatsapp-bot-venv/bin/activate
    ```

4. Install the following dependencies: `twilio, flask, requests`.
    ```
    $ pip install twilio flask requests
    ```

5. Run the Flask application  
    Start by setting (exporting) the FLASK_APP environment variable
    ```
    Windows: set FLASK_APP=bot.py
    Mac: $ export FLASK_APP=bot.py
    ```
    Run this command afterwards:
    ```
    python -m flask run
    ```

6. Test the chatbot. 

    a. Download [ngrok](https://ngrok.com/download). From your CLI (terminal or CMD), navigate to the ngrok directory and run this command:

        $ ngrok http 5000
    
    Copy the URL where you see `Forwarding`. It will look like this `https://066cbc59.ngrok.io`.
    

    b. Create an account on [Twilio](https://www.twilio.com) and navigate to the [Whatsapp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox). Follow the instructions from Twilio to get a test whatsapp account.
    At the end of the setup, paste the url you copied earlier into the input field with the label `WHEN A MESSAGE COMES IN`. At the end of the URL, add '`/bot`' and hit save.

# Technologies Used
- Python, Flask framework
- Twilio
- ngrok
