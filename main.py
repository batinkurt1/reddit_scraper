#from bs4 import BeautifulSoup
#import requests
#import re

# file=requests.get('https://www.reddit.com/r/blueteamsec/hot')
#soup = BeautifulSoup(file.text, 'html.parser')
# for tag in soup.find_all(string=re.compile("journey")):
#    print(tag.name)


import praw
from praw.models import MoreComments
with open('secrets.txt') as fp:
    client_id,client_secret,user_agent=fp.readlines()

emaillist=[]
keywords=["vmray","any.run","cape","intezer"]
reddit = praw.Reddit(client_id=client_id,
                   client_secret=client_secret,
                   user_agent=user_agent)

blueteamsec=reddit.subreddit("blueteamsec")

posts_to_scrape=[]

for post in blueteamsec.hot(limit=3):
    posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for keyword in keywords:
        if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
            emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
for post in blueteamsec.top(time_filter="week"):
    posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for keyword in keywords:
        if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
            emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
for post in blueteamsec.top(time_filter="month"):
    posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for keyword in keywords:
        if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
            emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
for post in blueteamsec.top(time_filter="year"):
    posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for keyword in keywords:
        if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
            emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")


posts_to_scrape=list(set(posts_to_scrape))






for link in posts_to_scrape:
    submission=reddit.submission(url=link)
    
    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
    
        for keyword in keywords:
            if keyword in str(comment.body).lower():
                emaillist.append(link)
                break



#submission=reddit.submission(url='https://www.reddit.com/r/blueteamsec/comments/vc2rt5')
#print(submission)
""" for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
    print(comment.body)
    if len(comment.replies)!=0:
        pass """




""" def reply_checker(comment):
    if type(comment) == MoreComments:
        continue
    print(comment.body)
    if len(comment.replies)!=0:
        pass """
    
emaillist=list(set(emaillist))

print(emaillist)

