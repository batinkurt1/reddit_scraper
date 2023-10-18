# reddit_scraper

## Overview

The Reddit Scraper is a Python script that allows you to scrape Reddit data based on keywords and subreddits and then send an email with the collected data. This script is useful for monitoring specific topics or discussions on Reddit and sharing them via email.

## Prerequisites

Before using this script, you need to ensure that you have the following prerequisites in place:

1. **Python Environment:** Make sure you have Python 3.x installed on your system.

2. **Required Python Libraries:** You can install the required Python libraries by running the following command:

pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client requests

3. **API Credentials:**
- You need Google API credentials (`credentials.json`) to send emails using Gmail API. You can follow the Google API documentation to obtain these credentials.
- Create a `token.json` file for storing your Google API token after authorization.

4. **Input Data Files:**
- Create the following input data files in the same directory as the script:
  - `keywords.txt`: List of keywords to search for on Reddit, one keyword per line.
  - `subreddits.txt`: List of subreddits to search in, one subreddit per line.
  - `email_credentials.txt`: Your email address and password (Note: Using app-specific passwords is recommended for Gmail).
  - `email_recepients.txt`: List of email recipients, one email address per line.

## Usage

1. Clone or download the repository to your local machine.

2. Make sure you have the required input data files (`keywords.txt`, `subreddits.txt`, `email_credentials.txt`, `email_recepients.txt`) and the necessary API credentials (`credentials.json` and `token.json`) in the same directory as the script.

3. Run the script using the following command:

python reddit_scraper.py

4. The script will start scraping Reddit data based on the specified keywords and subreddits.

5. Once the scraping is complete, it will construct an email with the collected Reddit content and send it to the specified recipients.

## Important Notes

- Ensure the security of your API credentials (`credentials.json`) and token (`token.json`) files. Do not share them publicly.

- Customize the email subject and body in the script to fit your specific needs.

---

Enjoy using the script!
