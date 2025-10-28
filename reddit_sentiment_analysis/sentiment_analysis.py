import praw
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def fetch_comments(subreddit_name: str, limit: int = 1000):
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="sentiment_analysis_script"
    )
    subreddit = reddit.subreddit(subreddit_name)
    comments = []
    for comment in subreddit.comments(limit=limit):
        comments.append(comment.body)
    return comments


def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiments.append("positive")
        elif polarity < 0:
            sentiments.append("negative")
        else:
            sentiments.append("neutral")
    return sentiments


def plot_sentiment_distribution(sentiments):
    df = pd.DataFrame({"sentiment": sentiments})
    counts = df["sentiment"].value_counts()
    plt.figure()
    counts.plot(kind="bar")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution of Reddit Comments")
    plt.tight_layout()
    plt.show()


def main():
    subreddit_name = "your_subreddit"  # Replace with the subreddit you want to analyze
    comments = fetch_comments(subreddit_name, limit=1000)
    sentiments = analyze_sentiment(comments)
    plot_sentiment_distribution(sentiments)


if __name__ == "__main__":
    main()
