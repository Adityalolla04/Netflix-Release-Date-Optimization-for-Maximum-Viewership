import streamlit as st
import pandas as pd
import datetime

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('netflix_titles.csv')

data = load_data()

# Ensure the "date_added" column exists and handle missing values
if "date_added" not in data.columns:
    data["date_added"] = None

# Set up the Streamlit interface
st.title("Netflix Release Date Optimization")
st.markdown(
    "This app helps optimize Netflix release dates for maximum viewership by providing season and title-based insights."
)

# Sidebar filters
st.sidebar.header("Filter Options")
title_filter = st.sidebar.text_input("Search for a Title:")
season_filter = st.sidebar.selectbox(
    "Select Season:",
    ["All", "Winter", "Spring", "Summer", "Fall"]
)

# Helper function to determine season based on release date
def get_season(date_str):
    if pd.isna(date_str):
        return "Unknown"
    try:
        month = datetime.datetime.strptime(date_str, "%B %d, %Y").month
    except ValueError:
        return "Unknown"
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Fall"
    return "Unknown"

# Add a season column to the data
data["season"] = data["date_added"].apply(lambda x: get_season(x) if x else "Unknown")

# Filter the data
filtered_data = data.copy()

if title_filter:
    filtered_data = filtered_data[
        filtered_data["title"].str.contains(title_filter, case=False, na=False)
    ]

if season_filter != "All":
    filtered_data = filtered_data[filtered_data["season"] == season_filter]

# Display results
st.header("Filtered Netflix Titles")
st.write(
    f"Displaying {len(filtered_data)} titles matching your filters."
)
st.dataframe(filtered_data[["title", "type", "release_year", "season", "date_added"]])

# Add a summary chart
st.header("Seasonal Distribution of Titles")
season_counts = data["season"].value_counts()
st.bar_chart(season_counts)