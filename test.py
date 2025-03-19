import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import sqlite3
import re
from fpdf import FPDF
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)  # Remove mentions
    text = re.sub(r"#", "", text)  # Remove hashtags
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  # Remove special characters
    return text

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Sample dataset
sample_data = [
    "I love this product! It's amazing and works perfectly.",
    "This is the worst experience I've ever had. Absolutely terrible!",
    "It's okay, not the best but not the worst either.",
    "Fantastic quality and great customer service! Highly recommend.",
    "I'm not sure how I feel about this. It's kind of meh.",
    "Horrible, just horrible. I regret buying this.",
    "Decent, but could be improved with a few changes.",
    "Absolutely wonderful! I'm so happy with my purchase.",
    "Not good, not bad, just neutral feelings about it.",
    "A bit disappointing, expected more for the price.",
    "This product exceeded my expectations. Worth every penny!",
    "Customer support was unhelpful and rude. Frustrating experience!",
    "An average product, nothing too special about it.",
    "Very high quality and durable. Would buy again!",
    "I'm torn. Some aspects are great, others not so much.",
    "Terrible product. Broke after one use!",
    "Satisfactory, but nothing groundbreaking.",
    "Outstanding service and quick delivery!",
    "Indifferent about this. It’s neither great nor terrible.",
    "For the price, I expected much better.",
    "Superb craftsmanship and attention to detail.",
    "Wouldn’t recommend. There are better alternatives out there.",
    "Love it! Exactly what I was looking for.",
    "Not as described. Very disappointed!",
    "Surprisingly good! Wasn't expecting such quality.",
    "Overhyped and overpriced.",
    "A game-changer! Can’t believe I lived without it.",
    "Really poor packaging. Product arrived damaged.",
    "Decent for casual use but not for professionals.",
    "Amazing! Will definitely buy again and recommend it to friends."
]

# Convert sample data to DataFrame
df = pd.DataFrame({"text": sample_data})
df["clean_text"] = df["text"].apply(clean_text)
df["sentiment"] = df["clean_text"].apply(analyze_sentiment)

# Save data to CSV for BI tools like Power BI or Tableau
df.to_csv("sentiment_analysis.csv", index=False)
print("Data exported to sentiment_analysis.csv")

# Save data to SQLite database for BI analysis
conn = sqlite3.connect("sentiment_analysis.db")
df.to_sql("sentiments", conn, if_exists="replace", index=False)
print("Data saved to SQLite database")

# Sentiment analysis summary
sentiment_counts = df["sentiment"].value_counts()
print("Sentiment Summary:")
print(sentiment_counts)

# Interactive visualization with Plotly
fig = px.bar(sentiment_counts, x=sentiment_counts.index, y=sentiment_counts.values,
             title="Sentiment Analysis of Sample Data", labels={'x': 'Sentiment', 'y': 'Count'},
             color=sentiment_counts.index, color_discrete_map={"Positive": "green", "Neutral": "blue", "Negative": "red"})
fig.show()




# Generate a word cloud


# Ensure all_words is not empty
all_words = " ".join(df["clean_text"].dropna())

# Use a default TrueType font available on Ubuntu
font_path = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

if not os.path.exists(font_path):
    print(f"Font not found: {font_path}")
else:
    print(f"Using font: {font_path}")

# Generate the WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white", font_path=font_path).generate(all_words)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words", fontsize=14)
plt.tight_layout()
plt.show()

# Generate PDF Report

def generate_pdf_report(sentiment_counts):
    pdf_filename = "sentiment_report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Sentiment Analysis Report")

    c.setFont("Helvetica", 12)
    y_position = height - 100

    for sentiment, count in sentiment_counts.items():
        c.drawString(100, y_position, f"{sentiment}: {count}")
        y_position -= 20  # Move down for next line

    c.save()
    print(f"PDF report generated: {pdf_filename}")

# Call function after sentiment analysis
generate_pdf_report(sentiment_counts)
