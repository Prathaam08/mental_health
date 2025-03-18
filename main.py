


# import tweepy  # type: ignore
# import praw # type: ignore
# import pandas as pd # type: ignore # type: ignore
# from textblob import TextBlob # type: ignore
# import matplotlib.pyplot as plt # type: ignore
# from wordcloud import WordCloud # type: ignore
# import re

# # Twitter API credentials (use environment variables for security)
# TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMaayQEAAAAA2wCzLMGx%2BjNhGGpE7RV4vJhoMZ4%3DwDgSseJrVmHJSV4IwDMhWRiV5yaJTkekHJa5Fk8v6n65q9ixMj"

# # Reddit API credentials
# REDDIT_CLIENT_ID = "_npLrcJhEmvLr9rfZvGqxg"
# REDDIT_CLIENT_SECRET = "LPlX5i1ZszkRnO_H_x-TT4DhdIrKFw"
# REDDIT_USER_AGENT = "u/Ill_Confection_3139"

# # Clean text function
# def clean_text(text):
#     text = re.sub(r"http\S+", "", text)  # Remove URLs
#     text = re.sub(r"@[A-Za-z0-9_]+", "", text)  # Remove mentions
#     text = re.sub(r"#", "", text)  # Remove hashtags
#     text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  # Remove special characters
#     return text

# # Sentiment analysis function
# def analyze_sentiment(text):
#     analysis = TextBlob(text)
#     if analysis.sentiment.polarity > 0:
#         return "Positive"
#     elif analysis.sentiment.polarity == 0:
#         return "Neutral"
#     else:
#         return "Negative"

# # Collect Twitter data using API v2
# def collect_twitter_data_v2(keyword, count=100):
#     try:
#         client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
#         query = f"{keyword} lang:en -is:retweet"
#         response = client.search_recent_tweets(
#             query=query, max_results=min(count, 100), tweet_fields=["text"]
#         )
#         return [tweet.text for tweet in response.data] if response.data else []
#     except Exception as e:
#         print(f"Error collecting Twitter data: {e}")
#         return []

# # Collect Reddit data
# def collect_reddit_data(subreddit_name, count=100):
#     try:
#         reddit = praw.Reddit(
#             client_id=REDDIT_CLIENT_ID,
#             client_secret=REDDIT_CLIENT_SECRET,
#             user_agent=REDDIT_USER_AGENT,
#         )
#         subreddit = reddit.subreddit(subreddit_name)
#         return [
#             submission.title + " " + submission.selftext
#             for submission in subreddit.top(limit=count)
#         ]
#     except Exception as e:
#         print(f"Error collecting Reddit data: {e}")
#         return []

# # Main function
# def main():
#     # Get user inputs
#     twitter_keyword = input("Enter the Twitter keyword: ")
#     subreddit_name = input("Enter the subreddit name: ")

#     print("Collecting Twitter data...")
#     twitter_data = collect_twitter_data_v2(twitter_keyword, count=100)
#     if not twitter_data:
#         print("No Twitter data collected.")
    
#     print("Collecting Reddit data...")
#     reddit_data = collect_reddit_data(subreddit_name, count=100)
#     if not reddit_data:
#         print("No Reddit data collected.")
    
#     if not twitter_data and not reddit_data:
#         print("No data collected from either source. Exiting.")
#         return

#     # Combine and preprocess data
#     all_data = twitter_data + reddit_data
#     df = pd.DataFrame({"text": all_data})
#     df["clean_text"] = df["text"].apply(clean_text)
#     df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

#     # Sentiment analysis summary
#     sentiment_counts = df["sentiment"].value_counts()
#     print("Sentiment Summary:")
#     print(sentiment_counts)

#     # Visualize sentiment distribution
#     sentiment_counts.plot(kind="bar", title="Sentiment Distribution", color=["green", "blue", "red"])
#     plt.xlabel("Sentiment")
#     plt.ylabel("Count")
#     plt.show()

#     # Generate a word cloud
#     all_words = " ".join(df["clean_text"])
#     wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.title("Word Cloud of Discussions")
#     plt.show()

# if __name__ == "__main__":
#     main()




# import tweepy 
# import praw
# import pandas as pd
# from textblob import TextBlob
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# import re

# # Twitter API credentials (use environment variables for security)
# TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMaayQEAAAAA2wCzLMGx%2BjNhGGpE7RV4vJhoMZ4%3DwDgSseJrVmHJSV4IwDMhWRiV5yaJTkekHJa5Fk8v6n65q9ixMj"

# # Reddit API credentials
# REDDIT_CLIENT_ID = "_npLrcJhEmvLr9rfZvGqxg"
# REDDIT_CLIENT_SECRET = "LPlX5i1ZszkRnO_H_x-TT4DhdIrKFw"
# REDDIT_USER_AGENT = "u/Ill_Confection_3139"

# # Clean text function
# def clean_text(text):
#     text = re.sub(r"http\S+", "", text)  # Remove URLs
#     text = re.sub(r"@[A-Za-z0-9_]+", "", text)  # Remove mentions
#     text = re.sub(r"#", "", text)  # Remove hashtags
#     text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  # Remove special characters
#     return text

# # Sentiment analysis function
# def analyze_sentiment(text):
#     analysis = TextBlob(text)
#     if analysis.sentiment.polarity > 0:
#         return "Positive"
#     elif analysis.sentiment.polarity == 0:
#         return "Neutral"
#     else:
#         return "Negative"

# # Collect Twitter data using API v2
# def collect_twitter_data_v2(keyword, count=100):
#     try:
#         client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
#         query = f"{keyword} lang:en -is:retweet"
#         response = client.search_recent_tweets(
#             query=query, max_results=min(count, 100), tweet_fields=["text"]
#         )
#         return [tweet.text for tweet in response.data] if response.data else []
#     except Exception as e:
#         print(f"Error collecting Twitter data: {e}")
#         return []

# # Collect Reddit data
# def collect_reddit_data(subreddit_name, count=100):
#     try:
#         reddit = praw.Reddit(
#             client_id=REDDIT_CLIENT_ID,
#             client_secret=REDDIT_CLIENT_SECRET,
#             user_agent=REDDIT_USER_AGENT,
#         )
#         subreddit = reddit.subreddit(subreddit_name)
#         return [
#             submission.title + " " + submission.selftext
#             for submission in subreddit.top(limit=count)
#         ]
#     except Exception as e:
#         print(f"Error collecting Reddit data: {e}")
#         return []

# # Main function
# def main():
#     # Get user inputs
#     twitter_keyword = input("Enter the Twitter keyword: ")
#     subreddit_name = input("Enter the subreddit name: ")

#     print("Collecting Twitter data...")
#     twitter_data = collect_twitter_data_v2(twitter_keyword, count=100)
#     if not twitter_data:
#         print("No Twitter data collected.")
    
#     print("Collecting Reddit data...")
#     reddit_data = collect_reddit_data(subreddit_name, count=100)
#     if not reddit_data:
#         print("No Reddit data collected.")
    
#     if not twitter_data and not reddit_data:
#         print("No data collected from either source. Exiting.")
#         return

#     # Combine and preprocess data
#     all_data = twitter_data + reddit_data
#     df = pd.DataFrame({"text": all_data})
#     df["clean_text"] = df["text"].apply(clean_text)
#     df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

#     # Sentiment analysis summary
#     sentiment_counts = df["sentiment"].value_counts()
#     print("Sentiment Summary:")
#     print(sentiment_counts)

#     # Visualize sentiment distribution
#     plt.figure(figsize=(8, 5))
#     sentiment_counts.plot(kind="bar", color=["green", "blue", "red"])
#     plt.title("Sentiment Analysis of Discussions", fontsize=14)
#     plt.xlabel("Sentiment Categories", fontsize=12)
#     plt.ylabel("Number of Posts", fontsize=12)
#     plt.xticks(rotation=0)
#     for i, count in enumerate(sentiment_counts):
#         plt.text(i, count + 1, str(count), ha='center', fontsize=10)
#     plt.tight_layout()
#     plt.show()

#     # Generate a word cloud
#     all_words = " ".join(df["clean_text"])
#     wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.axis("off")
#     plt.title(f"Most Common Words in '{twitter_keyword}' and '{subreddit_name}' Discussions", fontsize=14)
#     plt.tight_layout()
#     plt.show()

# if __name__ == "__main__":
#     main()




import tweepy 
import praw
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Twitter API credentials (use environment variables for security)
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMaayQEAAAAA2wCzLMGx%2BjNhGGpE7RV4vJhoMZ4%3DwDgSseJrVmHJSV4IwDMhWRiV5yaJTkekHJa5Fk8v6n65q9ixMj"

# Reddit API credentials
REDDIT_CLIENT_ID = "_npLrcJhEmvLr9rfZvGqxg"
REDDIT_CLIENT_SECRET = "LPlX5i1ZszkRnO_H_x-TT4DhdIrKFw"
REDDIT_USER_AGENT = "u/Ill_Confection_3139"

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
def collect_twitter_data_v2(keyword, count=100):
    try:
        client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        query = f"{keyword} lang:en -is:retweet"
        response = client.search_recent_tweets(
            query=query, max_results=min(count, 100), tweet_fields=["text"]
        )
        return [tweet.text for tweet in response.data] if response.data else []
    except Exception as e:
        print(f"Error collecting Twitter data: {e}")
        return []

# Collect Reddit data
def collect_reddit_data(subreddit_name, count=100):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
        )
        subreddit = reddit.subreddit(subreddit_name)
        return [
            submission.title + " " + submission.selftext
            for submission in subreddit.top(limit=count)
        ]
    except Exception as e:
        print(f"Error collecting Reddit data: {e}")
        return []

# Main function
def main():
    # Get user inputs
    twitter_keyword = input("Enter the Twitter keyword: ")
    subreddit_name = input("Enter the subreddit name: ")

    print("Collecting Twitter data...")
    twitter_data = collect_twitter_data_v2(twitter_keyword, count=100)
    if not twitter_data:
        print("No Twitter data collected.")
    
    print("Collecting Reddit data...")
    reddit_data = collect_reddit_data(subreddit_name, count=100)
    if not reddit_data:
        print("No Reddit data collected.")
    
    if not twitter_data and not reddit_data:
        print("No data collected from either source. Exiting.")
        return

    # Combine and preprocess data
    all_data = twitter_data + reddit_data
    df = pd.DataFrame({"text": all_data})
    df["clean_text"] = df["text"].apply(clean_text)
    df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

    # Sentiment analysis summary
    sentiment_counts = df["sentiment"].value_counts()
    print("Sentiment Summary:")
    print(sentiment_counts)

    # Visualize sentiment distribution (Bar Chart)
    plt.figure(figsize=(8, 5))
    sentiment_counts.plot(kind="bar", color=["green", "blue", "red"])
    plt.title("Sentiment Analysis of Discussions", fontsize=14)
    plt.xlabel("Sentiment Categories", fontsize=12)
    plt.ylabel("Number of Posts", fontsize=12)
    plt.xticks(rotation=0)
    for i, count in enumerate(sentiment_counts):
        plt.text(i, count + 1, str(count), ha='center', fontsize=10)
    plt.tight_layout()
    plt.show()

    # Visualize sentiment distribution (Pie Chart)
    plt.figure(figsize=(8, 8))
    sentiment_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["green", "blue", "red"],
                          labels=sentiment_counts.index, legend=False)
    plt.title("Sentiment Distribution Pie Chart", fontsize=14)
    plt.ylabel("")  # Hides the default y-label
    plt.tight_layout()
    plt.show()

    # Generate a word cloud
    all_words = " ".join(df["clean_text"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Most Common Words in '{twitter_keyword}' and '{subreddit_name}' Discussions", fontsize=14)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
