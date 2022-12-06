1. Before using Gmail API in local machine, make sure to have the key from the Google Cloud Project. That is given under `Gmail API/credentials.json`. 
2. Install the Google Client Library for python by running this command in the local terminal to the virtual environment, `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
3. Run `python quickstart.py` to authenticate your local terminal to the email. The email is `team0neapr@gmail.com`. 
- Make sure to go through the safety notification. You will pass it if it says that the authentication flow has passed. 
4. After authenticated, run the `send_emails.py` to send the email to respective individuals. 