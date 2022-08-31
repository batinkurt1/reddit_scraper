import smtplib
import ssl
import email
import requests

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
import os

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
                comment_links.append("https://www.reddit.com"+data["permalink"])
        res = requests.get(
            f"{api_url}/reddit/search/submission", params=params)
        if res.status_code==200:
            for data in res.json()["data"]:
                post_links.append("https://www.reddit.com"+data["permalink"])

numberofposts = len(post_links)
numberofcomments = len(comment_links)


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

text = message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        for recepient in emailrecepients:
            message["To"] = recepient
            server.sendmail(sender_email, recepient, text)
