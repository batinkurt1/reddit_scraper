import email
import requests
import base64

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
import os



from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


api_url = "https://api.pushshift.io"

abs_dir = os.path.dirname(__file__)


with open(abs_dir+"/keywords.txt") as fp:
    keywords = [r.strip() for r in fp.readlines()]
with open(abs_dir+"/subreddits.txt") as fp:
    subreddits = [r.strip() for r in fp.readlines()]





emaillist = []
post_links = []
comment_links = []
numberofposts = 0
numberofcomments = 0

for keyword in keywords:
    for subreddit in subreddits:
        params = {"q": keyword,
                  "after": "7d",
                  "subreddit": subreddit,
                  "size": 100}
        res = requests.get(
            f"{api_url}/reddit/search/comment", params=params)
        if res.status_code==200:
            for data in res.json()["data"]:
                comment_links.append( keyword + ": " + "https://www.reddit.com"+data["permalink"])
        res = requests.get(
            f"{api_url}/reddit/search/submission", params=params)
        if res.status_code==200:
            for data in res.json()["data"]:
                post_links.append(keyword + ": " + "https://www.reddit.com"+data["permalink"])


numberofposts = len(post_links)
numberofcomments = len(comment_links)

emaillist.extend(post_links)
emaillist.extend(comment_links)

emaillist = list(set(emaillist))

with open("email_credentials.txt") as fp:
    sender_email, sender_password = [r.strip() for r in fp.readlines()]

with open("email_recepients.txt") as fp:
    emailrecepients = [r.strip() for r in fp.readlines()]

week = f"{datetime.date.today()}-{datetime.date.today()-datetime.timedelta(days=7)}"

subject = f"[{week}] Automated Reddit Scraper: Scraping cybersec subreddits to find this week's related news"

postlist="\n ".join(emaillist)
body = f"""I have scraped {len(subreddits)} subreddits, {numberofposts} posts, and {numberofcomments} comments to bring you this week's related news. \n 
Below, you can find the results. \n""" + postlist


message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))



SCOPES=['https://www.googleapis.com/auth/gmail.send']

creds=None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    service = build('gmail', 'v1', credentials=creds)
    for recepient in emailrecepients:
        message["To"] = recepient
        text = message.as_string()
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'raw': encoded_message
        }
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
except HttpError as error:
    print("an error occured")