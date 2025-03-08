# import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List af available timezone
TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "American/New_york",
    "Europe/London",
    "Asia/tokyo",
    "Australia/sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# app title
st.title("Time Zone App")

# Create multiselect widget for selecting timezones
selected_timezone = st.multiselect("Select timezons", TIME_ZONE, default=["UTC","Asia/Karachi"]) 

# Display of selected timezones
st.subheader("Selected Timezones")
for tz in selected_timezone:

    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    # Display the current time for each selected time zone
    st.write(f"**{tz}**: {current_time}")

#vCreate a subheader for converting time between timezone
st.subheader("Convert Time Across Time Zones")

# Create a time input widget for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# Create a selectbox for selecting the timezone to convert from  
from_tz = st.selectbox("From Timezone",TIME_ZONE, index=0)

#Crate a selectbox for selecting the timezone to convert to 
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)

# Create a butto trigger the the time conversion 
if st.button("Convert Time"):
    
    # Combine the current time with the selcgted timezome
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    #Display the converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")

