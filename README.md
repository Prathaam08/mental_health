# mental_health

4 Charts in One Page 1️⃣ Bar Chart - Number of positive, neutral, and negative posts
2️⃣ Pie Chart - Percentage of each sentiment
3️⃣ Scatter Plot - Sentiment spread against word count
4️⃣ Box Chart - Text Length Distribution per Sentiment

✅ Clearer Understanding

Scatter Plot helps see how short vs long posts relate to sentiment

Understanding the Scatter Plot: Sentiment vs. Text Length
The scatter plot visualizes the relationship between text length (number of words) and sentiment (Positive, Neutral, Negative).

Axes Explanation
X-Axis (Text Length)

Represents the number of words in a text (short to long).

Each dot represents a single post/tweet.

Y-Axis (Sentiment Score)

Sentiments are represented as:

1 (Positive)

0 (Neutral)

-1 (Negative)

The position of each dot on the y-axis tells you whether the post was classified as positive, neutral, or negative.

What the Scatter Plot Shows
Cluster of Neutral Posts (around 0 sentiment)

Likely shorter posts, as they stay near the lower x-values.

This suggests neutral posts are mostly short messages.

Positive and Negative Sentiments Spread Out

Positive (1) and Negative (-1) sentiments are spread across different text lengths.

Some longer texts express strong sentiments, meaning people tend to elaborate when they feel strongly (either positive or negative).

Possible Outliers

If a few dots are far apart from the main cluster, those might be unusual cases where someone wrote a very long post but kept a neutral tone (or vice versa).



This box plot represents the distribution of text length across different sentiment categories (Positive, Neutral, and Negative). Here's how to interpret it:

Key Components of the Box Plot
Boxes (Interquartile Range - IQR)

Each box represents the middle 50% of the text lengths for each sentiment.

The lower boundary (bottom of the box) is the 25th percentile (Q1).

The upper boundary (top of the box) is the 75th percentile (Q3).

The line inside the box is the median (50th percentile, Q2).

Whiskers

These extend from the box to show the range of non-outlier values.

They typically extend to 1.5 times the IQR beyond Q1 and Q3.

Outliers (Dots outside whiskers)

Any individual points beyond the whiskers are considered outliers, meaning those text lengths are significantly different from the rest.

What the Plot Tells Us
Positive Sentiment (leftmost box)

The median text length is around the lower half of the box.

The distribution is fairly spread out, with some outliers having very long text lengths.

The range of text lengths is moderate to high.

Neutral Sentiment (middle box)

Appears very compressed (small IQR), meaning most neutral texts are very short.

Almost no long texts; outliers are short texts.

Negative Sentiment (rightmost box)

The median text length is higher than the neutral category.

The text length is more widely spread out, meaning people express negativity with short and long texts.

Some extreme outliers suggest very long negative posts.

Insights from the Box Plot
Neutral texts tend to be very short.

Negative and Positive texts have more variation, with negative ones sometimes being much longer.

People tend to write long posts when expressing strong sentiments (both positive and negative).
