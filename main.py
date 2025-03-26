

from dash import dcc, html, Input, Output, State
import dash
import plotly.express as px
import pandas as pd
import tweepy
import praw
from textblob import TextBlob
import re
import os
from dotenv import load_dotenv
from collections import Counter
from wordcloud import WordCloud
import base64
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Load environment variables
load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)  
    text = re.sub(r"#", "", text)  
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  
    return text.lower()

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

# Fetch Twitter data
def collect_twitter_data(keyword, count=100):
    try:
        client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        query = f"{keyword} lang:en -is:retweet"
        response = client.search_recent_tweets(query=query, max_results=min(count, 100), tweet_fields=["text", "created_at"])
        return [{"text": tweet.text, "timestamp": tweet.created_at} for tweet in response.data] if response.data else []
    except Exception as e:
        print(f"Error collecting Twitter data: {e}")
        return []

# Fetch Reddit data
def collect_reddit_data(keyword, count=100):
    try:
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)
        subreddit = reddit.subreddit(keyword.replace(" ", ""))
        return [{"text": submission.title + " " + submission.selftext, "timestamp": pd.to_datetime(submission.created_utc, unit='s')} for submission in subreddit.top(limit=count)]
    except Exception as e:
        print(f"Error collecting Reddit data: {e}")
        return []

# Generate word cloud
def generate_word_cloud(text_series):
    words = " ".join(text_series)
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="coolwarm").generate(words)
    
    # Convert image to base64
    img = BytesIO()
    wordcloud.to_image().save(img, format="PNG")
    img.seek(0)
    encoded_image = base64.b64encode(img.getvalue()).decode()
    
    return f"data:image/png;base64,{encoded_image}"

# Dash App Layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sentiment Analysis Dashboard", style={'textAlign': 'center'}),
  
    html.Div([
       dcc.Input(
          id="keyword",
          type="text",
          placeholder="Enter keyword...",
          style={
              'padding': '12px',
              'borderRadius': '10px',
              'border': '1px solid #ccc',
              'width': '250px',
              'fontSize': '16px',
              'outline': 'none',
              'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'
          }  # ✅ Closing the style dictionary properly here
        ),  
        html.Button(
          "Analyze",
           id="analyze",
           n_clicks=0,
           style={
              'padding': '12px 20px',
              'borderRadius': '10px',
              'border': 'none',
              'backgroundColor': '#007bff',
              'color': 'white',
              'fontSize': '16px',
              'cursor': 'pointer',
              'marginLeft': '10px',
              'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)',
              'transition': '0.3s ease'
            }
        )
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '10px', 'marginBottom': '20px'}),
    
    dcc.Graph(id="bar_pie_chart"),
    dcc.Graph(id="scatter_box_chart"),
    
    html.Div([
        html.H3("Word Cloud"),
        html.Img(id="wordcloud", style={'width': '80%', 'display': 'block', 'margin': 'auto'})
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])

# Callback function for updating graphs
@app.callback(
    [Output("bar_pie_chart", "figure"), Output("scatter_box_chart", "figure"), Output("wordcloud", "src")],
    [Input("analyze", "n_clicks")],
    [State("keyword", "value")]
)
def update_graph(n_clicks, keyword):
    if not keyword:
        return px.bar(), px.box(), ""

    # Fetch data
    twitter_data = collect_twitter_data(keyword, count=100)
    reddit_data = collect_reddit_data(keyword, count=100)
    all_data = twitter_data + reddit_data

    if not all_data:
        return px.bar(), px.box(), ""

    df = pd.DataFrame(all_data)
    df["clean_text"] = df["text"].apply(clean_text)
    df["sentiment"] = df["clean_text"].apply(analyze_sentiment)
    
    # **Compute Text Length (Word Count)**
    df["text_length"] = df["clean_text"].apply(lambda x: len(x.split()))

    # Sentiment Count
    sentiment_counts = df["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["sentiment", "count"]

    # Bar Chart
    bar_fig = px.bar(sentiment_counts, x="sentiment", y="count", 
                     title="Sentiment Analysis", labels={'sentiment': 'Sentiment', 'count': 'Count'},
                     color="sentiment",
                     color_discrete_map={"Positive": "blue", "Neutral": "gray", "Negative": "red"})

    # Pie Chart
    pie_fig = px.pie(sentiment_counts, names="sentiment", values="count", title="Sentiment Distribution")

    # **Combine Bar & Pie Chart**
    combined_fig = make_subplots(rows=1, cols=2, subplot_titles=("Bar Chart", "Pie Chart"),
                                 specs=[[{"type": "bar"}, {"type": "pie"}]])

    for trace in bar_fig["data"]:
        combined_fig.add_trace(trace, row=1, col=1)
    for trace in pie_fig["data"]:
        combined_fig.add_trace(trace, row=1, col=2)

    # Scatter Plot (Text Length vs. Sentiment)
    scatter_fig = px.scatter(df, x="text_length", y="sentiment",
                             title="Text Length vs. Sentiment",
                             labels={"text_length": "Text Length (Word Count)", "sentiment": "Sentiment"},
                             color="sentiment",
                             color_discrete_map={"Positive": "blue", "Neutral": "gray", "Negative": "red"},
                             opacity=0.6)

    # Box Plot (Sentiment Distribution Over Time)
    # df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["hour_bin"] = (pd.to_datetime(df["timestamp"]).dt.hour // 2) * 2  # Groups hours into 2-hour intervals

    # Fix: Use jittering and ensure numerical sentiment spread
    df["sentiment_numeric"] = df["sentiment"].map({"Positive": 1, "Neutral": 0, "Negative": -1})

    box_fig = px.box(df, x="hour_bin", y="sentiment_numeric",
                 title="Sentiment Distribution Over Time (2-Hour Intervals)",
                 labels={"hour_bin": "Time (2-Hour Intervals)", "sentiment_numeric": "Sentiment Score (-1 to 1)"},
                 points="all",  # Show all points
                 notched=True,   # Add notches for better visualization
                 boxmode="overlay",
                 color="sentiment",
                 color_discrete_map={"Positive": "blue", "Neutral": "gray", "Negative": "red"})




    # **Merge Scatter & Box Plot**
    scatter_box_fig = make_subplots(rows=1, cols=2, subplot_titles=("Scatter Plot (Text Length vs. Sentiment)", "Box Plot (Sentiment Over Time)"),
                                    specs=[[{"type": "scatter"}, {"type": "box"}]])

    for trace in scatter_fig["data"]:
        scatter_box_fig.add_trace(trace, row=1, col=1)
    for trace in box_fig["data"]:
        scatter_box_fig.add_trace(trace, row=1, col=2)

    # Word Cloud
    wordcloud_img = generate_word_cloud(df["clean_text"])

    return combined_fig, scatter_box_fig, wordcloud_img


if __name__ == "__main__":
    app.run(debug=True)
