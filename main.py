import praw



with open('secrets.txt') as fp:
    client_id, client_secret, user_agent = [r.strip() for r in fp.readlines()]


with open("keywords.txt") as fp:
    keywords = [r.strip() for r in fp.readlines()]
with open("subreddits.txt") as fp:
    subreddits = [r.strip() for r in fp.readlines()]
with open("emaillist.txt") as fp:
    emailrecepients = [r.strip() for r in fp.readlines()]


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)



emaillist = []

for subreddit in subreddits:
    currentsub = reddit.subreddit(subreddit)

    for post in currentsub.top(time_filter="week"):
        submission = reddit.submission(
            url=f"https://www.reddit.com/r/{currentsub}/comments/{post.id}")
        
        submission.comments.replace_more(limit=0)

        for keyword in keywords:

            if f"https://www.reddit.com/r/{currentsub}/comments/{post.id}" in emaillist:
                continue

            if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
                emaillist.append(
                    f"https://www.reddit.com/r/{currentsub}/comments/{post.id}")

            for comment in submission.comments.list():
                if keyword in str(comment.body).lower():
                    emaillist.append(
                        f"https://www.reddit.com/r/{currentsub}/comments/{post.id}")


emaillist = list(set(emaillist))










"""submission = reddit.submission(
    url='https://www.reddit.com/r/blueteamsec/comments/vc2rt5')
submission.comments.replace_more(limit=0)
print(submission)
for comment in submission.comments.list():
    print(comment.body)"""


"""for link in posts_to_scrape:
    submission=reddit.submission(url=link)

    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue
    
        for keyword in keywords:
            if keyword in str(comment.body).lower():
                emaillist.append(link)
                break"""





# submission=reddit.submission(url='https://www.reddit.com/r/blueteamsec/comments/vc2rt5')
# print(submission)
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



"""for post in currentsub.hot(limit=3):
        posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
        for keyword in keywords:
            if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
                emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for post in currentsub.top(time_filter="week"):
        posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
        for keyword in keywords:
            if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
                emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for post in currentsub.top(time_filter="month"):
        posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
        for keyword in keywords:
            if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
                emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
    for post in currentsub.top(time_filter="year"):
        posts_to_scrape.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
        for keyword in keywords:
            if keyword in str(post.title).lower() or keyword in str(post.selftext).lower():
                emaillist.append(f"https://www.reddit.com/r/blueteamsec/comments/{post.id}")
"""
