# Sentiment Analysis from Twitter & Reddit

## Overview
This project collects and analyzes sentiment from **Twitter and Reddit** discussions based on a user-provided keyword. It applies **sentiment analysis** using **TextBlob**, visualizes the data using various graphs, and generates a **word cloud** to display frequently used words.

---
## Features
- Collects **real-time Twitter** data using **Tweepy (Twitter API v2)**
- Fetches **Reddit posts** using **PRAW (Python Reddit API Wrapper)**
- **Cleans text** by removing URLs, special characters, and mentions
- **Applies sentiment analysis** using **TextBlob** (Positive, Neutral, Negative)
- **Generates visualizations**:
  - **Bar Chart & Pie Chart** (Sentiment Distribution)
  - **Scatter Plot** (Sentiment vs. Text Length)
  - **Box Plot** (Text Length per Sentiment Category)
  - **Word Cloud** (Most Common Words in Discussions)
- Provides an **interactive menu** to visualize graphs multiple times

---
## Setup & Installation
### 1. **Clone the Repository**

### 2. **Install Required Dependencies**
```sh
   pip install tweepy praw textblob wordcloud seaborn matplotlib python-dotenv
```

### 3. **Set Up API Keys Securely**

#### Option 1: Using Environment Variables
For **Windows (Command Prompt or PowerShell)**:
```sh
   setx TWITTER_BEARER_TOKEN "your_twitter_api_key"
   setx REDDIT_CLIENT_ID "your_reddit_client_id"
   setx REDDIT_CLIENT_SECRET "your_reddit_client_secret"
   setx REDDIT_USER_AGENT "your_reddit_user_agent"
```
For **Mac/Linux (Bash or Zsh)**:
```sh
   export TWITTER_BEARER_TOKEN="your_twitter_api_key"
   export REDDIT_CLIENT_ID="your_reddit_client_id"
   export REDDIT_CLIENT_SECRET="your_reddit_client_secret"
   export REDDIT_USER_AGENT="your_reddit_user_agent"
```

#### Option 2: Using a `.env` File (Recommended for Local Development)
1. **Install dotenv**:
   ```sh
   pip install python-dotenv
   ```
2. **Create a `.env` file** in the project folder and add:
   ```sh
   TWITTER_BEARER_TOKEN=your_twitter_api_key
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=your_reddit_user_agent
   ```
3. **Modify Python Code to Load Environment Variables**:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()
   TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
   ```

---
## How to Run the Script
```sh
   python main.py
```
1. Enter a keyword to analyze sentiment from Twitter & Reddit.
2. The script collects **real-time data**, cleans it, and performs **sentiment analysis**.
3. Various charts and a word cloud will be displayed.
4. After initial visualization, an interactive menu allows re-displaying any chart.

---
## Data Processing & Visualization
### 1️⃣ **Bar & Pie Chart (Sentiment Distribution)**
- **Bar Chart**: Shows the count of **Positive, Neutral, and Negative** discussions.
- **Pie Chart**: Displays sentiment **distribution percentage**.

### 2️⃣ **Scatter & Box Plot (Text Length Analysis)**
- **Scatter Plot**: Shows the **relationship between text length and sentiment**.
- **Box Plot**: Displays **text length distribution** for each sentiment category.

### 3️⃣ **Word Cloud**
- Visualizes the **most frequently used words** in discussions.
- Helps identify **trends** and common topics around the keyword.

---
## Example Output
### **Sentiment Summary:**
```
Positive    42
Neutral     35
Negative    23
```
### **Sample Word Cloud:**
📌 *A visualization of the most common words in analyzed discussions.*

### **Sample Scatter Plot:**
📊 *Shows the variation in sentiment scores based on text length.*

