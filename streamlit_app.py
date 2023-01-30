import streamlit
import pandas

streamlit.title ('My Parents New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text (':-) Omega 3 & Blueberry oatmeal')
streamlit.text ('@#Kale, Spinach & Rocket Smoothie ')
streamlit.text ('8-9 Hard-boiled Free-Ranch Egg')
streamlit.text ('Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a picklist here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Get Fruit values response normalizaed and stored  into columns 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display table with fruit advice response normalized in column values.
streamlit.dataframe(fruityvice_normalized)
