# main.py
"""
Sentiment analysis using Hugging Face's transformers pipeline.

Setup:
    pip install -r requirements.txt
"""

import sys

try:
    from transformers import pipeline
except ImportError:
    sys.exit(
        "Missing dependencies. Install them first:\n"
        "    pip install -r requirements.txt"
    )

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"


def analyze_sentiment(text_list):
    """Run sentiment analysis on a list of strings and print the results."""
    print("Loading model...")
    try:
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model=MODEL_NAME,
            truncation=True,
        )
    except Exception as e:
        sys.exit(
            f"Couldn't load model '{MODEL_NAME}'. "
            f"Check your internet connection.\nDetails: {e}"
        )

    print("\n--- Example Inputs and Outputs ---")
    for text in text_list:
        result = sentiment_pipeline(text)[0]
        print(f"Input: '{text}'")
        print(f"Output: Label: {result['label']}, Confidence: {result['score']:.4f}\n")


if __name__ == "__main__":
    sample_texts = [
        "I absolutely loved working on this AI integration task!",
        "The documentation was a bit confusing and hard to follow.",
        "The prototype runs perfectly without any secret API keys.",
    ]

    analyze_sentiment(sample_texts)
    