import streamlit as st
import random
import time
import requests

# Constants
API_BASE_URL = "http://127.0.0.1:8000"
API_KEY = "1234567890"
DEFAULT_QUOTE = "The way to get started is to quit talking and begin doing. – Walt Disney"
DEFAULT_HUSTLES = [
    "Freelancing - Start offering your skills online!",
    "Start a dropshipping business",
    "Create and sell digital products",
    "Become a social media manager",
    "Start a blog or YouTube channel",
    "Offer virtual assistance services",
    "Create an online course",
    "Start a pet sitting service",
    "Become a personal shopper",
    "Do graphic design work",
    "Offer translation services",
    "Start a food delivery service",
    "Become a fitness trainer online",
    "Create and sell handmade crafts",
    "Start a photography business"
]

st.title("Money Making Machine")

def generate_money():
    """Generate a random amount of money between 1 and 1,000,000"""
    return random.randint(1, 1000000)

def fetch_from_api(endpoint):
    """Generic function to fetch data from API with error handling"""
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}?api_key={API_KEY}")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.RequestException:
        return None

def fetch_side_hustle():
    """Fetch side hustle ideas from the API or return a random default hustle"""
    try:
        result = fetch_from_api("side_hustles")
        if result and result.get("side_hustles"):
            return result.get("side_hustles")
        return random.choice(DEFAULT_HUSTLES)
    except:
        return random.choice(DEFAULT_HUSTLES)

def fetch_money_quotes():
    """Fetch motivational money quotes from the API"""
    result = fetch_from_api("money_quotes")
    if result:
        return result.get("money_quote")
    return DEFAULT_QUOTE

# Money Generator Section
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    with st.spinner("Counting your money..."):
        time.sleep(3)
        amount = generate_money()
        st.success(f"You made ${amount:,}!")

# Side Hustle Section
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    with st.spinner("Finding your next opportunity..."):
        idea = fetch_side_hustle()
        if idea:
            st.success(idea)
        else:
            st.success(random.choice(DEFAULT_HUSTLES))

# Motivation Section
st.subheader("Money Mastery Motivation")
if st.button("Get Inspired"):
    with st.spinner("Finding inspiration..."):
        quote = fetch_money_quotes()
        st.success(quote)


