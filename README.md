🎭 Sentiment Analysis with Toxic Words Reduction

Sentiment Analysis with Toxic Words Reduction

Overview

A modern Flask-based web application that analyzes sentiment while neutralizing toxic words. The system replaces offensive words with neutral alternatives and determines sentiment using the VADER (Valence Aware Dictionary for Sentiment Reasoning) lexicon.

Features

Cleanses text by replacing toxic words with neutral alternatives.

Analyzes sentiment with NLTK's SentimentIntensityAnalyzer.

Interactive web-based UI powered by Flask.

Displays original text, cleaned text, and sentiment results.

Technologies Used

Python – Core language.

Flask – Web framework for the UI.

Pandas – Handles data operations.

NLTK – Enables sentiment analysis.

Installation Guide

1. Clone the Repository

git clone https://github.com/104Dhanaraj/Sentiment-Analysis-with-toxic-words-reduction.git
cd Sentiment-Analysis-with-toxic-words-reduction

2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Download NLTK Data

python -c "import nltk; nltk.download('vader_lexicon')"

Usage Guide

1. Run the Flask Application

python app.py

The application starts at http://127.0.0.1:5000/.

2. Enter Text for Analysis

Open the web interface.

Enter text in the input field.

Click Submit to get the cleaned text and sentiment results.

Code Breakdown

1. Importing Required Libraries

os – Manages file paths.

pandas – Reads and processes CSV files.

nltk.sentiment.SentimentIntensityAnalyzer – Analyzes sentiment.

nltk – Downloads required NLP resources.

Flask – Handles web interactions.

2. Loading Data

load_datasets() reads toxic and non-toxic words into Pandas DataFrames.

3. Reducing Toxicity

reduce_toxicity(text, non_toxic_dict) replaces toxic words with neutral alternatives.

4. Sentiment Analysis

analyze_sentiment(text) determines if text is Positive, Negative, or Neutral using VADER.

5. Flask Web Application

Route: / → Renders the main interface (index.html).

Route: /analyze → Processes text input and displays results.

6. Running the Application

Executing app.py launches Flask in debug mode for live updates.


