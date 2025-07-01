# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables with fallback defaults

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', 
    default="http://localhost:5050/"
    )


# Function to perform GET requests
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    request_url = backend_url + endpoint + "?" + params.rstrip("&")
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {}


# Function to analyze review sentiment using external API
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    print(f"Analyzing sentiment for: {text}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Sentiment analysis failed: {e}")
        return {"sentiment": "unknown"}


# Function to submit a review via POST
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.RequestException as e:
        print(f"Post review failed: {e}")
        return {"status": "error"}
