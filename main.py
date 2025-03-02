import os
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from flask import Flask, render_template, request

# Download necessary NLTK data
nltk.download('vader_lexicon')

# File paths
TOXIC_FILE = os.path.join("datasets", "toxic.csv")
NON_TOXIC_FILE = os.path.join("datasets", "non_toxic.csv")

# Load datasets
def load_datasets():
    toxic_words = pd.read_csv(TOXIC_FILE)
    non_toxic_words = pd.read_csv(NON_TOXIC_FILE)
    return toxic_words, non_toxic_words

# Reduce toxic words in text
def reduce_toxicity(text, non_toxic_dict):
    words = text.split()
    cleaned_words = [non_toxic_dict.get(word.lower(), word) for word in words]
    return " ".join(cleaned_words)

# Analyze sentiment
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['compound'] > 0:
        return "Positive"
    elif sentiment_scores['compound'] < 0:
        return "Negative"
    else:
        return "Neutral"

# Initialize Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/analyze', methods=['POST'])
def analyze():
    # Load toxic and non-toxic datasets
    _, non_toxic_words = load_datasets()

    # Create a dictionary for toxic-to-neutral word mapping
    non_toxic_dict = dict(zip(non_toxic_words['toxic_word'], non_toxic_words['neutral_word']))

    # Get text input from the form
    text = request.form['text_input']

    # Reduce toxicity
    cleaned_text = reduce_toxicity(text, non_toxic_dict)

    # Analyze sentiment
    sentiment = analyze_sentiment(cleaned_text)

    # Return the result to the front-end
    return render_template('index.html', original_text=text, cleaned_text=cleaned_text, sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
