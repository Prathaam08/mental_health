import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Generate sample data
np.random.seed(42)
sentiments = np.random.choice(["Positive", "Neutral", "Negative"], size=200, p=[0.4, 0.3, 0.3])
text_lengths = np.random.randint(5, 50, size=200)

# Create DataFrame
df = pd.DataFrame({
    "sentiment": sentiments,
    "text_length": text_lengths
})

# Bar & Pie Charts
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sentiment_counts = df["sentiment"].value_counts()
axes[0].bar(sentiment_counts.index, sentiment_counts.values, color=["green", "blue", "red"], edgecolor="black")
axes[0].set_title("Sentiment Distribution (Bar Chart)")
axes[0].set_xlabel("Sentiment")
axes[0].set_ylabel("Count")
axes[1].pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["green", "blue", "red"])
axes[1].set_title("Sentiment Distribution (Pie Chart)")
plt.show()

# Scatter Plot (Sentiment vs Text Length)
sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
df["sentiment_numeric"] = df["sentiment"].map(sentiment_mapping)
plt.figure(figsize=(8, 6))
plt.scatter(df["text_length"], df["sentiment_numeric"], c=df["sentiment_numeric"], cmap="coolwarm", alpha=0.7)
plt.title("Scatter Plot: Sentiment vs Text Length")
plt.xlabel("Number of Words in Text")
plt.ylabel("Sentiment Score (-1: Negative, 0: Neutral, 1: Positive)")
plt.show()

# Box Plot (Text Length Distribution per Sentiment)
plt.figure(figsize=(8, 6))
sns.boxplot(x=df["sentiment"], y=df["text_length"], hue=df["sentiment"], palette="coolwarm", legend=False)
plt.title("Box Plot: Text Length Distribution per Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Text Length (Word Count)")
plt.show()

# Word Cloud (Sample Data Words)
sample_text = "happy great amazing sad terrible boring excited fun emotional neutral random text positive vibes" * 10
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(sample_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud: Most Common Words")
plt.show()
