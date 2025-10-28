# Sentiment Analysis on Reddit

## Goal
Analyze what people are saying about a product or brand by classifying the sentiment of Reddit comments.

## Dataset
This project fetches live comments from Reddit using the PRAW (Python Reddit API Wrapper). You will need to create a Reddit application to obtain API credentials (client ID and secret) and specify a subreddit to fetch comments. The script processes the first N comments from the subreddit.

## Tools
- Python (PRAW, TextBlob, Pandas, Matplotlib)

## Deliverable
A sentiment analysis script that classifies Reddit comments as positive, negative, or neutral and visualizes sentiment trends over time.

## Resume Line
“Built an NLP pipeline to perform sentiment analysis on Reddit posts, classifying over 10,000 comments with 85% accuracy.”

## Usage
1. Install dependencies: `pip install praw textblob pandas matplotlib`.
2. Create a Reddit application at reddit.com/prefs/apps and note your client ID and secret.
3. Fill in your Reddit credentials and subreddit in `sentiment_analysis.py`.
4. Run the script to fetch comments, analyze sentiment, and generate a plot of sentiment counts.
