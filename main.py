

import tweepy 
import praw
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import seaborn as sns
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")


# Clean text function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)  # Remove mentions
    text = re.sub(r"#", "", text)  # Remove hashtags
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  # Remove special characters
    return text

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Collect Twitter data using API v2
def collect_twitter_data(keyword, count=100):
    try:
        client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        query = f"{keyword} lang:en -is:retweet"
        response = client.search_recent_tweets(query=query, max_results=min(count, 100), tweet_fields=["text"])
        return [tweet.text for tweet in response.data] if response.data else []
    except Exception as e:
        print(f"Error collecting Twitter data: {e}")
        return []

# Collect Reddit data
def collect_reddit_data(keyword, count=100):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        subreddit_name = keyword.replace(" ", "")  # Convert keyword to potential subreddit name
        subreddit = reddit.subreddit(subreddit_name)
        return [
            submission.title + " " + submission.selftext
            for submission in subreddit.top(limit=count)
        ]
    except Exception as e:
        print(f"Error collecting Reddit data: {e}")
        return []
    
# Function to create visualizations
def show_bar_pie_chart(df):
    sentiment_counts = df["sentiment"].value_counts()

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Bar Chart
    axes[0].bar(sentiment_counts.index, sentiment_counts.values, color=["green", "blue", "red"], edgecolor="black")
    axes[0].set_title("Sentiment Analysis of Discussions", fontsize=16, fontweight="bold")
    axes[0].set_xlabel("Sentiment Category", fontsize=14)
    axes[0].set_ylabel("Number of Posts", fontsize=14)
    axes[0].tick_params(axis="x", rotation=45)

    # Pie Chart
    sentiment_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["green", "blue", "red"], ax=axes[1])
    axes[1].set_title("Sentiment Distribution", fontsize=16, fontweight="bold")
    axes[1].set_ylabel("")  # Hide y-label

    plt.tight_layout()
    plt.show()

def show_scatter_box_chart(df):
    # Assign numeric values to sentiments for Scatter & Bubble Chart
    sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
    df["sentiment_numeric"] = df["sentiment"].map(sentiment_mapping)
    df["text_length"] = df["clean_text"].apply(lambda x: len(x.split()))  # Word count per post

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Scatter Plot (Sentiment vs Text Length)
    axes[0].scatter(df["text_length"], df["sentiment_numeric"], c=df["sentiment_numeric"], cmap="coolwarm", alpha=0.7)
    axes[0].set_title("Scatter Plot: Sentiment vs Text Length", fontsize=16, fontweight="bold")
    axes[0].set_xlabel("Number of Words in Text", fontsize=14)
    axes[0].set_ylabel("Sentiment Score (-1: Negative, 0: Neutral, 1: Positive)", fontsize=14)

    sns.boxplot(x=df["sentiment"], y=df["text_length"], ax=axes[1], hue=df["sentiment"], palette="coolwarm", legend=False)
    axes[1].set_title("Box Plot: Text Length Distribution per Sentiment", fontsize=16, fontweight="bold")
    axes[1].set_xlabel("Sentiment Category", fontsize=14)
    axes[1].set_ylabel("Number of Words in Text", fontsize=14)

    plt.tight_layout()
    plt.show()

def show_wordcloud(df, keyword):
    all_words = " ".join(df["clean_text"])
    wordcloud = WordCloud(width=900, height=400, background_color="white").generate(all_words)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Most Common Words in '{keyword}' Discussions", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()


# Main function
def main():
    # Get user inputs
    keyword = input("Enter the keyword for sentiment analysis: ").strip()

    print("Collecting Twitter data...")
    twitter_data = collect_twitter_data(keyword, count=100)
    
    print("Collecting Reddit data...")
    reddit_data = collect_reddit_data(keyword, count=100)

    if not twitter_data and not reddit_data:
        print("No data collected from either source. Exiting.")
        return


   # Combine data and analyze
    all_data = twitter_data + reddit_data
    df = pd.DataFrame({"text": all_data})
    df["clean_text"] = df["text"].apply(clean_text)
    df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

    # Sentiment analysis summary
    sentiment_counts = df["sentiment"].value_counts()
    print("Sentiment Summary:")
    print(sentiment_counts)

    show_bar_pie_chart(df)
    show_scatter_box_chart(df)
    show_wordcloud(df, keyword)


    # Menu for User to View Charts Again
    while True:
        print("\nWhat do you want to see again?")
        print("1. Bar & Pie Chart")
        print("2. Scatter & Box Chart")
        print("3. Word Cloud")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_bar_pie_chart(df)
        elif choice == "2":
            show_scatter_box_chart(df)
        elif choice == "3":
            show_wordcloud(df, keyword)
        elif choice == "4":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-4.")



if __name__ == "__main__":
    main()
