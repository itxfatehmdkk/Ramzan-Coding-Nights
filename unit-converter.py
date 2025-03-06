import streamlit as st # Importing the streamlit library for building web apps

# Function to convert units bases on predefined conversions factors or farmulas
def convert_units(value,unit_from,unit_to):

    conversions ={
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,   # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000     # 1 kilogram = 1000 grams

    }

    key = f"{unit_from}_{unit_to}" # Generate a key bases on th input and out put units
 
#logic to convert the units 
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported" # Return this message if the conversion is not supported
    
st.title("Unit Converter") # Title of the web app

value = st.number_input("Enter the value:", min_value=1.0, step=1.0) # User Input field to enter the value to be converted

unit_from = st.selectbox("Convert from:",["meters","kilometers","grams","kilograms"])  # User Input field to select the unit to convert from


unit_to = st.selectbox("Convert to:",["meters","kilometers","grams","kilograms"])    # User Input field to select the unit to convert to

if st.button("Convert"):  # Button to trigger the conversion
    result = convert_units (value, unit_from, unit_to)  # Call the convert_units function to convert the units
    st.write(f"Converted value: {result}")   # Display the converted value
