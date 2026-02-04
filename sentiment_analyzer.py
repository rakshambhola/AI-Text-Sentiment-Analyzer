import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') #downloading pretained model 

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    compound = score['compound']

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_sentiment(text)
    print("Sentiment:", result)
