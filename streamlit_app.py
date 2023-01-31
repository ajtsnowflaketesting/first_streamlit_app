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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered this fruit:&', fruit_choice)

streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruits loads list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for choosing', add_my_fruit)

#This will not work correctly
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
