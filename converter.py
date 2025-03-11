import streamlit as st #using streamlit library

#Function to convert units based on pre defined functions
def convert_units(value, unit_from, unit_to):

    conversions ={
     "meters_kilometers":0.001,
     "kilometers_meters":1000,
     "grams_kilograms":0.001,
     "kilograms_grams":1000,
    }

    key  =    f"{unit_from}_{unit_to}" #Generate a ley based on the input and output units
    #logic to convert units
    if  key  in  conversions:
        #Convert value from the input to output
        conversions  =   conversions[key]
        return value * conversions
 
    else:
        return "Conversion not supported"# return the excepted value if function not run

st.title("Unit  Converter")      # title of the app

value = st.number_input("Enter value", min_value=0.0)# input value

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])# To convert from 

unit_to = st.selectbox("Convert to:",["meters", "kilometers", "grams", "kilograms"])#to convert in 

if st.button("Convert"):# button to start conversion
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")